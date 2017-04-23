from flask import Response

from utils.serializer import obj_to_json


def succ_json(msg=""):
    """
    Lei, HUANG: 23:20 21/04/2017
    返回成功响应    
    使用方式:
    在router当中使用return succ_json(msg='成功')
    :param msg: 成功消息
    :return: 
    """
    resp = {'code': 0, 'msg': msg}
    return Response(obj_to_json(resp), mimetype='application/json')
