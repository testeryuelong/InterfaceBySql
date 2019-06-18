# -*-coding:utf-8 -*-
# @Author : Zhigang

import os

# 项目路径
baseDir=os.path.dirname(os.path.dirname(__file__))

# 配置文件路径
configPath=os.path.join(baseDir,"Public","db_config_info.ini").replace("\\","/")

# interface_api字段位置
request_api_id_index=0
request_api_name_index=1
request_api_test_case_name_index=2
request_url_index=3
request_method_index=4
request_params_type_index=5
request_status_index=6
request_rely_db_index=7

# api_case_list字段位置
test_case_id_index=0
test_case_request_data_index=2
test_case_rely_data_index=3
test_case_reponse_code_index=4
test_case_reponse_data_index=5
test_case_data_store_index=6
test_case_check_point_index=7
test_case_active_index=8
test_case_result_index=9
test_case_error_info_index=10




if __name__=="__main__":
    print (baseDir)
    print (configPath)