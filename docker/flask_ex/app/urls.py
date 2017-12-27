# coding=utf-8
"""
@version: 2017/12/19 019
@author: Suen
@contact: sunzh95@hotmail.com
@file: urls
@time: 11:37
@note:  ??
"""
from app.test import test

register_module = [test]


def url_register(app, register_module=register_module):
    for mod in register_module: app.register_blueprint(mod)
