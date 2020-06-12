# 1导包
import unittest
from parameterized import parameterized
import logging
# 2定义类
import app
from api.login_api import IhrmLoginEmpApi
from uitle import duanyan, paramterizde


class TestIhrmEmp(unittest.TestCase):
    # 3类级别方法-初始化
    def setUp(self):
        # 实例化emp类
        self.ihrmloginempapi = IhrmLoginEmpApi()

    # 4类级别方法-销毁
    def tearDown(self):
        pass

    # 5登录成功
    # 参数化
    logging.info("开始登陆")
    filename = app.base_path + "/data/login.json"

    @parameterized.expand(paramterizde(filename, 'login'))
    def test01_login_success(self, mobile, password, stuat_code, success, code, message):
        data = {"mobile": mobile, "password": password}
        headers = {"Content-Type": "application/json"}
        respone = self.ihrmloginempapi.test_login(data, headers)

        print("返回的登录结果:", respone.json())
        # 获取令牌并保存
        token = "Bearer " + respone.json().get("data")
        print("令牌为:", token)
        # 把请求头和令牌赋值给base_token
        app.base_token = {"Content-Type": "application/json", "Authorization": token}

        # 断言
        duanyan(self, stuat_code, success, code, message, respone)
        logging.info("登陆成功")

    # 6增加新的部门
    logging.info("开始新增部门")

    @parameterized.expand(paramterizde(filename, 'zj_emp'))
    def test02_zj_emp(self, name, code, manager, introduce, pid, stuat_code, success, code_1, message):
        data = {"name": name,
                "code": code,
                "manager": manager,
                "introduce": introduce,
                "pid": pid}
        respone = self.ihrmloginempapi.test_zj_emp(app.base_token, data)
        print("新增部门返回的结果:", respone.json())
        # 获取新建部门的id
        app.emp_id = respone.json().get("data").get("id")
        # 断言
        duanyan(self, stuat_code, success, code_1, message, respone)

    # 查看部门信息
    logging.info("查看新增的部门")

    @parameterized.expand(paramterizde(filename, 'duanyan'))
    def test03_chack_emp(self, stuat_code, success, code, message):
        respone = self.ihrmloginempapi.test_chakan_emp(app.emp_id, app.base_token)
        print("查看部门信息:", respone.json())
        # 断言
        duanyan(self, stuat_code, success, code, message, respone)

    # 7修改部门
    logging.info("修改部门信息")

    @parameterized.expand(paramterizde(filename, 'upate_emp'))
    def test04_update_emp(self, name, code, manager, introduces, pid, stuat_code, success, code_1, message):
        data = {"name": name,
                "code": code,
                "manager": manager,
                "introduces": introduces,
                "pid": pid
                }
        repone = self.ihrmloginempapi.test_upate_emp(app.emp_id, app.base_token, data)
        # 断言
        duanyan(self, stuat_code, success, code_1, message, repone)

    # 查看部门信息
    logging.info("查看修改部门后的信息")

    @parameterized.expand(paramterizde(filename, 'duanyan'))
    def test05_chack_emp(self, stuat_code, success, code, message):
        respone = self.ihrmloginempapi.test_chakan_emp(app.emp_id, app.base_token)
        print("查看部门信息:", respone.json())
        duanyan(self, stuat_code, success, code, message, respone)

    # 8删除部门
    logging.info("开始删除部门")

    @parameterized.expand(paramterizde(filename, 'duanyan'))
    def test06_delete_emp(self, stuat_code, success, code, message):
        respon = self.ihrmloginempapi.test_delete_emp(app.emp_id, app.base_token)
        # 断言
        print("删除部门接口返回的数据:", respon.json())
        duanyan(self, stuat_code, success, code, message, respon)

    # 查看部门信息
    logging.info("查看删除后的部门信息")

    def test07_chack_emp(self):
        respone = self.ihrmloginempapi.test_chakan_emp(app.emp_id, app.base_token)
        print("查看部门信息:", respone.json())
        duanyan(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试", respone)
