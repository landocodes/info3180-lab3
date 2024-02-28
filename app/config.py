import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = os.environ.get('MAIL_PORT')
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    # MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')

    MAIL_PORT = int(os.environ.get('MAIL_PORT'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', '').lower() in ['true', '1']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', '').lower() in ['true', '1']
