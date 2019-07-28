from django.shortcuts import render,HttpResponse
import logging
logger = logging.getLogger('apis')

# Create your views here.
def test(requset):
    logger.info("欢迎访问")
    return HttpResponse("日志测试")