import logging.config

from invoke import Collection
from server.logging import LOGGING

from . import build, db

logging.config.dictConfig(LOGGING)
log = logging.getLogger(__name__)
log.debug("Logging is configured.")

namespace = Collection()
namespace.add_collection(db)
namespace.add_collection(build)
