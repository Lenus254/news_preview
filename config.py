import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    API_KEY=os.environ.get('API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
