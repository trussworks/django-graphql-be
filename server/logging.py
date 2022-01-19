import json
import logging
import os


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        """ Custom formatter to output JSON

        :param record: logging.LogRecord object
        :return: JSON string
        """
        # Create a structured dict for our logging
        payload = self.make_dict(record)

        # If an exception happened, add the stack trace
        if hasattr(record, 'exc_info') and record.exc_info:
            payload['stack_trace'] = self.formatException(record.exc_info)

        # Convert the dict to a json string
        json_string = json.dumps(payload)
        message = record.getMessage()
        # Attach the JSON string to our formatted message
        return f"{record.levelname} {message} {json_string}"

    @staticmethod
    def make_dict(record: logging.LogRecord) -> dict:
        # Get the interpolated message
        message_str = record.getMessage()

        # Capture the user values passed in
        if isinstance(record.args, dict):
            user_payload = record.args
        else:
            user_payload = {'value': repr(record.args)}

        # Return a structured dict including these values
        return {
            'payload': user_payload,
            'version': '0.0.1',  # Schema version
            'meta': {
                'level': record.levelname,
                'name': record.name,
            }
        }


# Create a DictConfig for logging
# https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
LOGGING: dict = {
    'version': 1,
    'disable_existing_loggers': False,

    # Formatters define what how the log is FORMATTED
    'formatters': {
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'json': {
            '()': JsonFormatter,
        }
    },

    # Handlers define WHERE the log goes and which formatter to use
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': os.getenv('LOG_FORMAT', 'simple')
        },
    },

    # Loggers collect the messages and route them to handlers
    'root': {
        # root logger → console handler → json formatter
        'handlers': ['console'],
        'level': os.getenv('LOG_LEVEL', 'INFO'),
    },
    'loggers': {
        'django': {
            # django logger → console handler → json formatter
            'handlers': ['console'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
