#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib

import requests


def send_telephone(telephone,code):
    url = "http://v.juhe.cn/sms/send"
    params = {
        "mobile": telephone,  # 接受短信的用户手机号码
        "tpl_id": "187500",  # 您申请的短信模板ID，根据实际情况修改
        "tpl_value": "#code#="+code,  # 您设置的模板变量，根据实际情况修改
        "key": "624b3e495e5c03bfd565328369656191",  # 应用APPKEY(应用详细页查询)
}

    resp = requests.get(url,params=params)

    print(resp.json())
    if resp:
        return resp.json()
    else:
        return False

