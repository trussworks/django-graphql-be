from invoke import Collection
from . import db, build
from .logging import *
import logging

logging.config.dictConfig(LOGGING)
log = logging.getLogger(__name__)
log.debug("Logging is configured.")

namespace = Collection()
namespace.add_collection(db)
namespace.add_collection(build)
