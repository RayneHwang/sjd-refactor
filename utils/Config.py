import os
from flask import json


class Config:
    def __init__(self, path):
        # print('cwd: ' + os.getcwd())
        f = open(path, encoding='utf-8')
        settings = json.load(f)
        self.database = settings['database']
        self.pool_size = self.database['pool_size']
        self.max_overflow = self.database['max_overflow']


if __name__ == '__main__':
    s = Config('../config.json')
    print(s.database)
