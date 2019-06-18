# -*-coding:utf-8 -*-
# @Author : Zhigang

def check_result(responseBody,checkPoint):
    """主要用于接口响应结果的检测
    :param responseBody: 响应结果
    :param checkPoint: 检查点
    :return: 错误信息，可为空，空则代表无错误
    """
    errorInfo={}
    for key,value in checkPoint.items():
        if key in responseBody:
            if value!=responseBody[key]:
                errorInfo[key]=responseBody[key]
    return errorInfo

if __name__=="__main__":
    responseBody={'username': 'yuzgtest18', 'code': '01'}
    checkPoint={"code":"01"}
    print (check_result(responseBody,checkPoint))