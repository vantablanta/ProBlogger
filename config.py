import os 

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')    
    SQLALCHEMY_TRACK_MODIFICATIONS  = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.getenv("DATABASE_URL").replace('postgres://', 'postgresql://')

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =os.getenv("SQLALCHEMY_DATABASE_URI")

config_options = {
    'dev': DevConfig,
    'prod': ProdConfig
}