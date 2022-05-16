import os 

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')    
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

class ProdConfig(Config):
    """"""
    SQLALCHEMY_DATABASE_URI  = os.getenv("PROD_SQLALCHEMY_DATABASE_URI")

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI  = os.getenv("DEV_SQLALCHEMY_DATABASE_URI").replace('postgres://', 'postgresql://')



config_options = {
    'dev': DevConfig,
    'prod': ProdConfig
}