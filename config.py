from dotenv import load_dotenv
import os
load_dotenv()
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']
myKeyword = os.environ['CLAVE']

DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}/{database}"

class Config:
    SECRET_KEY = myKeyword

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig
}