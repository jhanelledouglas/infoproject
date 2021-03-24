import os
####
class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY ='Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  
    #SQLALCHEMY_DATABASE_URI='postgresql://info:monique@localhost/info'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './app/static/img'
    #####3set DATABASE_URL=postgresql://project1:project1@localhost/project1

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
