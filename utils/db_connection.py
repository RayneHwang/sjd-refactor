from sqlalchemy import create_engine

from utils.Config import Config

databaseconfig = Config('./config.json').database
engine = create_engine(databaseconfig['url'], pool_size=databaseconfig['pool_size'],
                       max_overflow=databaseconfig['max_overflow'])
