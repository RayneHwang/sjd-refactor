import os
from flask import json


def get_config():
    f = open('./config.json', encoding='utf-8')
    settings = json.load(f)
    return settings

