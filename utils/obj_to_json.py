from utils import alchemy_encoder
import json


def obj_to_json(obj):
    return json.dumps(obj, cls=alchemy_encoder.FlatObjectEncoder)
