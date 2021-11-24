from invoke import Collection
from . import db, build

ns = Collection()
ns.add_collection(db)
ns.add_collection(build)
