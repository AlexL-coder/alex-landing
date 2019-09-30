import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://AlexandrLucky:X21zp14AS@AlexandrLucky.mysql.pythonanywhere-services.com/AlexandrLucky$NEWS'
    SQLALCHEMY_POOL_TIMEOUT = 1000
    POSTS_PER_PAGE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = 'alblogrecovery@gmail.com'
    MAIL_PASSWORD = 'ALPass!@78'
    ADMINS = ['alblogrecovery@gmail.com']
    LANGUAGES = ['en', 'es']
    MAX_SEARCH_RESULTS = 50
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')