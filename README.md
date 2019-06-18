# InterfaceBySql
基于数据库的接口测试框架

Action

    --check_result.py          # 将接口响应与预期结果对比
    --rely_data_analysis.py    # 对依赖数据进行处理，拼接最终请求参数
    --store_rely_data.py       # 存储依赖数据，为下一个接口做数据准备

Public

    --db_config_info.ini         # 数据库配置信息
    --project_var.py             # 工程变量

Utils

    --config_handler.py        # 解析配置文件
    --db_handler.py            # 数据库相关操作
    --encrypt.py               # 加密模块
    --send_request.py          # 发送请求

main.py   主程序脚本
