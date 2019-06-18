# -*-coding:utf-8 -*-
# @Author : Zhigang

from configparser import ConfigParser
from Public.project_var import configPath

class ConfigParse(object):

    @classmethod
    def getDatabaseConfig(cls,configPath,section):
        cf=ConfigParser()
        cf.read(configPath)
        host=cf.get(section,"host")
        port=cf.get(section,"port")
        user = cf.get(section, "user")
        password = cf.get(section, "password")
        db_name = cf.get(section, "db_name")
        return {"host":host,"port":port,"user":user,"password":password,"db_name":db_name}


if __name__=="__main__":
    print (ConfigParse.getDatabaseConfig(configPath,"localmysql"))
