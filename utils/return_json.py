import json

from flask import Response
from sqlalchemy.ext.declarative import DeclarativeMeta


class FlatObjectEncoder(json.JSONEncoder):
    """Simple, non-recursive json encoder"""

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def __obj_to_json(obj):
    """Simply convert flat SQLAlchemy objects into json"""
    return json.dumps(obj, cls=FlatObjectEncoder)


def return_json(obj):
    """return obj as"""
    return Response(__obj_to_json(obj), mimetype='application/json')


def error_json(code, msg):
    resp = {'status': 1, 'code': code, 'msg': msg}
    return Response(__obj_to_json(resp), mimetype='application/json')


def succ_json():
    resp = {'status': 0, 'msg': ''}
    return Response(__obj_to_json(resp), mimetype='application/json')
