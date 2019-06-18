# -*-coding:utf-8 -*-
# @Author : Zhigang

from Utils.config_handler import ConfigParse
from Public.project_var import *
from Utils.db_handler import DB

def rely_data_analysis(case_id,rely_data_format,request_data):
    """
    对接口请求的依赖数据进行处理
    :param case_id: 对应的测试用例编号
    :param rely_data_format: 依赖的数据格式
    :param request_data: 未拼装的请求数据
    :return: 返回接口最终请求参数
    """
    databaseInfo=ConfigParse.getDatabaseConfig(configPath, "localmysql")
    db=DB(databaseInfo)
    rely_source_data= db.get_data_store(case_id)
    for key in rely_data_format:
        if key in rely_source_data:
            req_key=key.split(".")[-1]
            request_data[req_key]=rely_source_data[key]
    return request_data

if __name__=="__main__":
    case_id=1
    rely_data_format=["request.register.1.username","request.register.1.password"]
    request_data={"username":"","password":""}
    print (rely_data_analysis(case_id,rely_data_format,request_data))