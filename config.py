import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    SQLALCHEMY_TRACK_MODIFACTIONS = False

    @ staticmethod
    def init_app(app):
        app.logger.handlers = []
        # log to syslog
        import logging
        import sys
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        app.logger.addHandler(ch)
        pass


class DevelopmentConfig(Config):
    @ classmethod
    def init_app(cls, app):
        Config.init_app(app)

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    @ classmethod
    def init_app(cls, app):
        Config.init_app(app)

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-prod.sqlite')


class UnixConfig(ProductionConfig):
    @ classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'unix': UnixConfig
}
