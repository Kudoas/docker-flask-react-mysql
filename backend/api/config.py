class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@db:5432/cookle_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
