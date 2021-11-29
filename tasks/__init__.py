from invoke import Collection
from . import db, build

namespace = Collection()
namespace.add_collection(db)
namespace.add_collection(build)
