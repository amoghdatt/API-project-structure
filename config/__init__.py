class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    ENDPOINT = 'https://sandbox.followthefrog.com/v3/healthcheck'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENDPOINT = 'https://sandbox.followthefrog.com/v3/healthcheck'
