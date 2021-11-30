class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'proot'
    MYSQL_DB = 'gamepedia'

config = {
    'development': DevelopmentConfig
}
