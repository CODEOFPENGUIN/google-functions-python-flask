from flask import Blueprint, request
import sys
import os

from apps.youtubeApp.main import youtube

# 1. new_app.py 를 통하여 testApp 생성 후 main.py 에서 testMain def 작성시
# e.g. from apps.testApp.main import testApp
resources_apps = Blueprint('resources', __name__,)

# 2. testApp route 추가
# @resources_apps.route('/test')
# def testApp_handler():
#     return testMain(request) 

@resources_apps.route('/youtube')
def youtube_handler():
    return youtube(request)
