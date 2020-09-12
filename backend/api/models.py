import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'
    firstname = Column(String(100), nullable=False, primary_key=True)
    lastname = Column(String(100), nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.firstname + ' ' + self.lastname


def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                # this will fail on non-encodable values, like other classes
                json.dumps(data)
                if data is not None:
                    fields[field] = data
            except TypeError:
                pass
        # a json-encodable dict
        return fields
