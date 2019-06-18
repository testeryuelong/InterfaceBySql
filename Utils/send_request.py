# -*-coding:utf-8 -*-
# @Author : Zhigang
import requests
import json

class SendHttpRequest(object):

    @classmethod
    def send_request(cls,url,method,paramsType,data=None,headers=None):
        if method=="post":
            if paramsType=="form":
                response=requests.post(url=url,data=json.dumps(data),headers=headers)
            elif paramsType=="json":
                response=requests.post(url=url,json=data,headers=headers)
        elif method=="get":
            # 此处待验证
            if paramsType=="url":
                new_url="%s%s" % (url,data)
                response=requests.get(url=new_url,params=data,headers=headers)
            elif paramsType=="params":
                response=requests.get(url=url,params=json.dumps(data),headers=headers)
        else:
            return "不能处理该请求方式，请及时更新"
        return response


if __name__=="__main__":
    requestUrl = "http://39.106.41.11:8080/register/"
    requestMethod = "post"
    paramsType = "form"
    requestData = {"username": "xxxe23sd", "password": "dflwe23sd", "email": "wcx@qq.com"}
    # requestUrl='http://39.106.41.11:8080/getBlogsContent/'
    # requestMethod="get"
    # paramsType="params"
    # requestData="2"
    response = SendHttpRequest.send_request (requestUrl, requestMethod, paramsType, requestData)
    print(response.status_code)
    print(response.json())