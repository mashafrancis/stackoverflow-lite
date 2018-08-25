import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'it is hard to guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
