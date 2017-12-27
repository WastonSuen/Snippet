# coding=utf-8
"""
@version: 2017/7/18 018
@author: Suen
@contact: sunzh95@hotmail.com
@file: interface.py
@time: 15:20
@note:  ??
"""

import hashlib
import json

import datetime

import bson
from mongoengine import QuerySet

from config import config


def encryptPwd(rawPwd):
    """
    密码加密闭包
    :param rawPwd: 
    :return: 
    """

    def md5Encrypt(raw, salt):
        m = hashlib.md5()
        m.update(raw)
        m.update(raw)
        m.update(salt)
        return m.hexdigest()

    return md5Encrypt(rawPwd, config.pwdSalt)



# 响应格式
handlers = {
    datetime.datetime: lambda o: str(o),
    bson.ObjectId: lambda o: str(o),
    QuerySet: lambda o: list(o)
}


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        handler = handlers.get(type(o), json.JSONEncoder.default)
        return handler(o)
