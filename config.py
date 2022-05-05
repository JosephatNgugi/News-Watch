import os

class Config:
    """Parent configuration class"""
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    NEWS_API_BASE_URL = "http://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}"
    NEWS_SOURCES_API = "https://newsapi.org/v2/top-headlines/sources?category={}&api_Key={}"
    ARTICLES_QUERY_API = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    SECRET_KEY = os.environ.get('SECRET_KEY')


class prodConfig(Config):
    """
    Child production configuration class
    Args:
        Config: The parent configuration class
    """

    pass

class DevConfig(Config):
    """
    Child development configuration class

    Args:
        Config: The parent configuration class
    """
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': prodConfig
    }