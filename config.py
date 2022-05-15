import os 

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')    

class ProdConfig(Config):
    """"""

class DevConfig(Config):
    DEBUG = True



config_options = {
    'dev': DevConfig,
    'prod': ProdConfig
}