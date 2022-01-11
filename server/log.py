from datetime import datetime
import json
import logging
import traceback
import sys
import os

APP_NAME = 'hello world json logging'
APP_VERSION = 'git rev-parse HEAD'
LOG_LEVEL = logging._nameToLevel['INFO']


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        """ Custom formatter to output JSON

        :param record: logging.LogRecord object
        :return: JSON string
        """

        payload = self.make_dict(record)
        # If an exception happened, add the stack trace
        if hasattr(record, 'exc_info') and record.exc_info:
            payload['stack_trace'] = self.formatException(record.exc_info)

        # Return the json string
        json_string = json.dumps(payload)
        message = record.getMessage()
        return f"{record.levelname} {message} {json_string}"

    @staticmethod
    def make_dict(record: logging.LogRecord) -> dict:
        message_str = record.getMessage()
        if isinstance(record.args, dict):
            user_payload = record.args
        else:
            user_payload = {'value': repr(record.args)}
        return {
            'payload': user_payload,
            'version': '0.0.1',  # Schema version
            'meta': {
                'level': record.levelname,
                'name': record.name,
            }
        }


class JsonEncoderStrFallback(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError as exc:
            if 'not JSON serializable' in str(exc):
                return str(obj)
            raise


class JsonEncoderDatetime(JsonEncoderStrFallback):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S%z')
        else:
            return super().default(obj)


logging.basicConfig(
    format='%(json_formatted)s',
    level=LOG_LEVEL,
    handlers=[
        # if you wish to also log to a file -- logging.FileHandler(log_file_path, 'a'),
        logging.StreamHandler(sys.stdout),
    ],
)

_record_factory_bak = logging.getLogRecordFactory()


def record_factory(*args, **kwargs) -> logging.LogRecord:
    record = _record_factory_bak(*args, **kwargs)

    record.json_formatted = json.dumps(
        {
            'level': record.levelname,
            'unixtime': record.created,
            'thread': record.thread,
            'location': '{}:{}:{}'.format(
                record.pathname or record.filename,
                record.funcName,
                record.lineno,
            ),
            'exception': record.exc_info,
            'traceback': traceback.format_exception(*record.exc_info) if record.exc_info else None,
            'app': {
                'name': APP_NAME,
                'releaseId': APP_VERSION,
                'message': record.getMessage(),
            },
        },
        cls=JsonEncoderDatetime,
    )
    return record


logging.setLogRecordFactory(record_factory)
