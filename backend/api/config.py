class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@db:3306/cookle_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
