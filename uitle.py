import json
import logging
from logging import handlers
# 断言函数
import time

import app
from app import base_path


def duanyan(self, status_code, success, code, message, respone):
    self.assertEqual(status_code, respone.status_code)
    self.assertEqual(success, respone.json().get("success"))
    self.assertEqual(code, respone.json().get("code"))
    self.assertIn(message, respone.json().get("message"))


# 定义日志函数
def log():
    # 1导包
    # 2创建日志器,严重级别
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 3创建处理器
    hi = logging.StreamHandler()
    # 4创建文件处理器
    file_name = base_path + "./log/ihrm-log{}.log".format(time.strftime("%H%M%S"))
    # 文件的保存方式
    sh = logging.handlers.TimedRotatingFileHandler(file_name, when='M', interval=1, backupCount=3, encoding='utf-8')
    # 5创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    format1 = logging.Formatter(fmt)
    # 6将格式化放到处理器上
    hi.setFormatter(format1)
    sh.setFormatter(format1)
    # 7将处理器放到日志器上
    logger.addHandler(hi)  # 控制台输出
    logger.addHandler(sh)


# 定义参数类
def paramterizde(filename, interface_name):
    # 定义空的列表
    dict_list = []
    # 打开json文件,读取里面的数据
    with open(filename, 'r', encoding='utf-8')as f:
        # 将json函数转换成字典
        jsondata = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        emp_data = jsondata.get(interface_name)
        # print(emp_data)
        # 将数据转换成列表包元祖的模式
        dict_list.append(tuple(emp_data.values()))
        # print(dict_list)
    return dict_list


# paramterizde(filename, 'login')
