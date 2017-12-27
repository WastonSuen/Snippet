# coding=utf-8
"""
@version: 2017/12/19 019
@author: Suen
@contact: sunzh95@hotmail.com
@file: __init__.py
@time: 11:16
@note:  ??
"""

from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

from config import config
from app.urls import url_register


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)
    db.init_app(app)

    url_register(app)

    return app
