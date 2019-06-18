# -*-coding:utf-8 -*-
# @Author : Zhigang

from Utils.db_handler import DB
from Utils.config_handler import ConfigParse
from Public.project_var import *
from Action.rely_data_analysis import rely_data_analysis
from Utils.encrypt import encrypt
from Utils.send_request import SendHttpRequest
from Action.store_rely_data import store_rely_data
from Action.check_result import check_result

def main():
    databaseInfo=ConfigParse.getDatabaseConfig(configPath, "localmysql")
    db=DB(databaseInfo)
    # 每次执行前先将之前的测试结果和不必要的数据清空下
    db.empty_test_result()
    for api in db.get_api_list():
        requestApiId=api[request_api_id_index]
        apiName=api[request_api_name_index]
        testCaseName=api[request_api_test_case_name_index]
        requestUrl=api[request_url_index]
        requestMethod=api[request_method_index]
        requestParamsType=api[request_params_type_index]
        requestStatus=api[request_status_index]

        api_case_list=db.get_api_case_list(requestApiId)[0]
        case_id=api_case_list[test_case_id_index]
        requestData=eval(api_case_list[test_case_request_data_index])  # 读出来是字符串，需要转化为字典
        rely_data_format=api_case_list[test_case_rely_data_index]
        data_store_rule=eval(api_case_list[test_case_data_store_index])
        checkPoint=eval(api_case_list[test_case_check_point_index])
        if requestStatus==1 and rely_data_format:
            rely_data_format = eval(rely_data_format)  # 如果存在，读出来是字符串，需要转化为列表
            # 处理依赖数据，生成新的请求数据
            rely_case_id=rely_data_format[0].split(".")[2]
            # print (rely_case_id)
            requestData=rely_data_analysis(rely_case_id,rely_data_format,requestData)
        # 若是登录请求，还需要将密码进行加密
        if apiName=="login":
            requestData["password"]=encrypt(requestData["password"])

        # print (requestData)
        # 此时请求参数已全部处理完毕，接下来发送请求
        response=SendHttpRequest.send_request(requestUrl,requestMethod,requestParamsType,requestData)

        # 验证与检查点是否一致，一致则继续下面的请求，不一致则结束程序
        errorInfo=check_result(response.json(), checkPoint)
        if errorInfo:
            db.write_test_result(case_id,response.status_code,response.json(),"fail",errorInfo)
            return " %s 响应结果与检查点不一致,程序结束运行，请核对！" % testCaseName
        db.write_test_result(case_id, response.status_code, response.json(), "pass", errorInfo)

        # 将数据按照data_store格式存储在interface_data_store表中；
        if response.status_code==200 and response.json()["code"]=="00" and data_store_rule:
            store_rely_data(requestApiId,case_id,apiName,data_store_rule,requestData,response.json())
    return "程序运行成功，所有测试用例执行结束"


if __name__=="__main__":
    print (main())
