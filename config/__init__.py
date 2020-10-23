class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    CFS_API_ENDPOINT = 'https://sandbox.followthefrog.com/v3/healthcheck'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    CFS_API_ENDPOINT = 'https://sandbox.followthefrog.com/v3/healthcheck'