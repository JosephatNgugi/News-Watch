
class Config:
    """Parent configuration class"""

    pass


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