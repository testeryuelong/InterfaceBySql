# -*-coding:utf-8 -*-
# @Author : Zhigang

from Utils.config_handler import ConfigParse
from Utils.db_handler import DB
from Public.project_var import *

def store_rely_data(api_id,case_id,api_name,data_store_rule,request_data,response_data):
    store_data_dict={}
    for key,value in data_store_rule.items():
        if key=="request":
            for req_name in value:
                if req_name in request_data:
                    store_key=".".join(["request",api_name,str(case_id),req_name])
                    store_data_dict[store_key]=request_data[req_name]
        elif key=="response":
            for res_name in value:
                if res_name in response_data:
                    store_key=".".join(["response",api_name,str(case_id),res_name])
                    store_data_dict[store_key]=response_data[res_name]
    # 向数据库中写入数据
    databaseInfo = ConfigParse.getDatabaseConfig(configPath, "localmysql")
    db = DB(databaseInfo)
    db.write_data_store(api_id,case_id,store_data_dict)
    db.close_connect()


if __name__=="__main__":
    api_id=2
    case_id=2
    api_name="login"
    data_store_rule={"response":["userid","token"]}
    request_data={"username":"yuzgtest18","password":"yuzg123456","email":"wcx@qq.com"}
    response_data={'token': '0cf54609bf2200dd920bb1c56ec67dba', 'code': '00', 'userid': 32918, 'login_time': '2019-04-13 22:01:06'}
    store_rely_data(api_id,case_id,api_name,data_store_rule,request_data,response_data)
