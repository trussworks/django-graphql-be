from invoke import Collection  # type:ignore
from . import db

ns = Collection()
ns.add_collection(db)
