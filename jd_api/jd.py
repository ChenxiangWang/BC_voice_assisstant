#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx_sdk
def classify (text):
    url = 'https://aiapi.jd.com/jdai/garbageTextSearch'
    params = { 
        'appkey' : '4b8a17c7d465e45d10f068b65a53eacb',
        'secretkey' : '355a6d6589a7ae431e27aea257cf8995'
    }
    bodyStr = '{  "cityId":310000,  "text":' + text +'}' #body中的内容
    response = wx_sdk.wx_post_req( url, params, bodyStr=bodyStr )
    return response.text
