import sys
import json
from apis.youtubeApis import *
from common.response import *
from common.logger import *
from common.custom_exception import CustomException

# from common.mysql import getSample
from common.mysql import MysqlManager
# from common.class_test import TestClass
log = getLogger(__name__)


def esPos(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    try:
        json_obj = {}
        with MysqlManager() as mysql:
            sql = "select id, name, description from sample"
            json_obj = mysql.selectAll(sql)
            if isinstance(json_obj, CustomException) :
                res = failResponse({})
            else:
                res = successResponse(json_obj)
            sql = "insert into sample (id, name, description) values (1, 'test', 'desc22')"
            result = mysql.executeData(sql)
            log.info(result)
            args = 2, 'test23', 'desctest'
            sql = "insert into sample (id, name, description) values (%s, %s, %s)"
            result = mysql.executeData(sql, args)
            log.info(result)
    except Exception as e:
        log.error(e)
        return failResponse(e)
    return res
