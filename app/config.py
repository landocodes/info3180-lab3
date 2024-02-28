import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base Config Object"""
    DEBUG = True
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    # MAIL_PORT = os.environ.get('MAIL_PORT')
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    # MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = os.environ.get('MAIL_PORT', '25')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', '').lower() in ['true', '1']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', '').lower() in ['true', '1']
