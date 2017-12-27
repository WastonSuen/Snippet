#!/usr/bin/python
# coding=utf-8
"""
@version: 2017/7/21 021
@author: Suen
@contact: sunzh95@hotmail.com
@file: response
@time: 11:35
@note:  通用的响应API,适配flask Response响应
"""

import json

from common import interface
from flask import Response
from config import config


class BaseResponse(object):
    """
    >0 : successed, 0 means general, if specail, make the code > 0
    <0 : failed, -1 means general, if specail, make the code < -1
    """

    def __init__(self):
        self._current_user = None

    def _result(self, result, message, data, header={}):
        try:
            obj = dict(result=result, msg=message, data=data)
            resp = json.dumps(obj, cls=interface.JSONEncoder)
            return Response(response=resp, headers=header, mimetype='application/json')
        except Exception as e:
            config.logger.error(e, exc_info=True)
            return self.failed()

    def success(self, code=0, message=':)', data={}, header={}):
        return self._result(code, message, data, header)

    def failed(self, code=-1, message=':(', data={}, header={}):
        return self._result(code, message, data, header)

    def failedByParameter(self, errorParameter, data={}, header={}):
        msg = 'error parameter:{}'.format(errorParameter, header)
        return self.failed(-2, msg, data)

    def failedByUnauthenticated(self):
        return self.failed(-3, 'Unauthenticated')

    def failedByLogin(self):
        return self.failed(-4, 'username or pwd error')

    def reLogin(self):
        return self.failed(-5, 'login again')


res = BaseResponse()
