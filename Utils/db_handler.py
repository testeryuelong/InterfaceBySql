# -*-coding:utf-8 -*-
# @Author : Zhigang

import pymysql
from Utils.config_handler import *

class DB(object):

    def __init__(self,databaseInfo):
        """初始化数据库"""
        self.db_info=databaseInfo
        self.conn=pymysql.connect(
            host=self.db_info["host"],
            port=int(self.db_info["port"]),
            user=self.db_info["user"],
            password=self.db_info["password"],
            db=self.db_info["db_name"],
            charset="utf8"
        )
        self.cur=self.conn.cursor()

    def close_connect(self):
        """提交事务，并关闭数据库连接"""
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def get_api_list(self):
        """获取接口测试请求，以列表形式返回"""
        try:
            sqlStr="select * from interface_api where status = 1"
            self.cur.execute(sqlStr)
            apiList=self.cur.fetchall()
            return list(apiList)
        except Exception as e:
            raise e

    def get_api_case_list(self,api_id):
        """获取指定接口的测试用例，以列表形式返回"""
        try:
            sqlStr="select * from interface_test_case where api_id = %s and active = 1 " % api_id
            self.cur.execute(sqlStr)
            apiList=self.cur.fetchall()
            return list(apiList)
        except Exception as e:
            raise e

    def get_data_store(self,case_id):
        """获取指定测试用例的依赖数据,保留数据格式"""
        try:
            sqlStr="select data_store from interface_data_store where case_id = %s " % case_id
            self.cur.execute(sqlStr)
            relyData=eval(self.cur.fetchall()[0][0])
            return relyData
        except Exception as e:
            raise e

    def write_data_store(self,api_id,case_id,data_store):
        """将依赖数据写入interface_data_store表中，如果已存在数据则更新依赖数据，不存在则直接插入
            data_store：字典格式
        """
        try:
            sqlStr="select data_store from interface_data_store where api_id = %s and case_id = %s" % (api_id,case_id)
            self.cur.execute(sqlStr)
        except Exception as e:
            raise e
        else:
            relyData = self.cur.fetchall()
            if relyData:
                # 此处需注意标点符号，因为虽然data_store传参时为双引号，但打印sqlStr语句为单引号，所以需要在外面加双引号
                sqlStr="update interface_data_store set data_store=\"%s\" where api_id = %s and case_id = %s" % (data_store,api_id,case_id)
            else:
                sqlStr="insert interface_data_store(api_id,case_id,data_store) values(%s,%s,\"%s\")" % (api_id,case_id,data_store)
            # print (sqlStr)
            self.cur.execute(sqlStr)

    def write_test_result(self,case_id,response_code,response_data,result,error_info):
        """将测试用例运行结果写入到interface_test_case表中，对应运行的测试用例
            case_id:是唯一值，故不需要api_id,
            response_code：数字格式
            response_data：字典格式
            result：字符串格式
            error_info：字典格式
        """
        try:
            sqlStr="update interface_test_case set response_code=%s,response_data=\"%s\",result=\"%s\",error_info=\"%s\" where case_id=%s" \
                   % (response_code,response_data,result,error_info,case_id)
            # print (sqlStr)
            self.cur.execute(sqlStr)
            self.conn.commit()
        except Exception as e:
            raise e

    def empty_test_result(self):
        """
        清空数据
        """
        try:
            sqlTestCaseStr="update  interface_test_case set response_code=null,response_data=null,result=null,error_info=null"
            sqlDataStore="update interface_data_store set data_store=null"
            self.cur.execute(sqlTestCaseStr)
            self.cur.execute(sqlDataStore)
            self.conn.commit()
        except Exception as e:
            raise e

if __name__=="__main__":
    databaseInfo=ConfigParse.getDatabaseConfig(configPath, "localmysql")
    db=DB(databaseInfo)
    # print (db.get_api_list())
    # print (db.get_api_case_list(1))
    # print (db.get_api_case_list(2))
    print (db.get_data_store(1))
    # print (db.write_data_store(1,1,{"request.register.1.username":"asd1","request.register.1.password":"sdfsdf23dd"}))
    # db.write_test_result(1,200,{'code': '00', 'userid': 32889},"pass",{'code': '00'})
