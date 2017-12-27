# coding=utf-8
"""
@version: 2017/12/19 019
@author: Suen
@contact: sunzh95@hotmail.com
@file: config.py
@time: 11:31
@note:  ??
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

from pymongo import MongoClient
import logging


class Config(object):
    # logging setting

    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(levelname)s - %(asctime)s - Process:%(process)d - thread:%(thread)d - %(filename)s - line:%(lineno)d - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    JSONIFY_MIMETYPE = 'application/json'

    DEBUG = True
    SECRET_KEY = ''
    pwdSalt = ""
    smsApiKey = ''

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True

    MONGODB_SETTINGS = [
        {'alias': 'default', 'db': 'suen', 'host': 'mongodb://192.168.2.154/suen', 'connect': False},
    ]
    MONGODB_CLIENT_DEFAULT = MongoClient(MONGODB_SETTINGS[0]['host'], connect=False)


class TestConfig(Config):
    DEBUG = False

    MONGODB_SETTINGS = [
        {'alias': 'default', 'db': 'suen', 'host': 'mongodb://127.0.0.1/suen', 'connect': False},
    ]
    MONGODB_CLIENT_DEFAULT = MongoClient(MONGODB_SETTINGS[0]['host'], connect=False)


from local_config import ProConfig

configDict = {
    'dev': DevConfig,  # 开发环境
    'test': TestConfig,  # 测试环境
    'pro': ProConfig,  # 生产环境
}

# TODO 需配置local_config并设置SUEN_ENV
config = configDict[os.getenv('SUEN_ENV') or 'dev']
