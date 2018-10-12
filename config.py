import logging

import redis

class Config(object):
    '''工程配置信息'''
    SECRET_KEY = 'supersaiyarenlovekillwa'

    # DEBUG = True
    # 数据库信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/news'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 配置session
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒
    # 默认日志的等级为debug
    LOG_LEVEL = logging.DEBUG



class DevelopmentConfig(Config):
    '''
    开发环境
    '''
    DEBUG = True
    # LOG_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    '''
    生产环境
    '''
    DEBUG = False
    LOG_LEVEL = logging.ERROR

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}