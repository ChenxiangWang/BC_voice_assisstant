#!/usr/bin/python
# -*- coding: utf-8 -*-
from . import wx_sdk
def classify_T (text):
    url = 'https://aiapi.jd.com/jdai/garbageTextSearch'
    params = { 
        'appkey' : '4b8a17c7d465e45d10f068b65a53eacb',
        'secretkey' : '355a6d6589a7ae431e27aea257cf8995'
    }
    bodyStr = '{  "cityId":310000,  "text":' + text +'}' #body中的内容
    response = wx_sdk.wx_post_req( url, params, bodyStr=bodyStr.encode("utf-8").decode("latin1") ) # TODO Try
    return response.text


def classify_V (fname):
    url = 'https://aiapi.jd.com/jdai/garbageVoiceSearch'
    params = { 
        'cityId' : '310000',
        'property' : '{"autoend":false,"encode":                                                                     {"channel":1,"format":"wav","sample_rate":16000,"post_process":0},"platform":"Linux","version":"0.0.0.1"}',
        'appkey' : '4b8a17c7d465e45d10f068b65a53eacb',
        'secretkey' : '355a6d6589a7ae431e27aea257cf8995'
    }
    speech_data = []
    with open(fname, 'rb') as speech_file:
        speech_data = speech_file.read()
    response = wx_sdk.wx_post_req( url, params,bodyStr=speech_data)
    return( response.text )encode("utf-8").decode("latin1")
