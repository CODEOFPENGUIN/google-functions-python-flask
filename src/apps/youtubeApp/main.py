import sys
import json
from apis.youtubeApis import *
from common.response import *
from common.logger import *

log = getLogger(__name__)


def youtube(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    url = request.args["url"]
    log.info(url)
    df = getSourceDataFrameSingle(url)
    rec_df = df.to_json(orient="records")
    json_obj = json.loads(rec_df)[0]
    res = successResponse(json_obj)
    return res
