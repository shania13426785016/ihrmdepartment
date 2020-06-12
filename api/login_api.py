import unittest
import requests


# 定义接口类
class IhrmLoginEmpApi:
    # 定义类属性方法
    def __init__(self):
        self.url = "http://ihrm-test.itheima.net"

    # 定义方法_登录接口
    def test_login(self, data, headers):
        login_url = self.url + "/api/sys/login"
        return requests.post(url=login_url,
                             headers=headers,
                             json=data
                             )

    # 定义方法_添加部门
    def test_zj_emp(self, headers, data):
        zj_url = self.url + "/api/company/department"
        return requests.post(url=zj_url, headers=headers, json=data)

    # 定义方法_查看部门
    def test_chakan_emp(self, emp_id, headers):
        select_xz_url = self.url + "/api/company/department/" + emp_id
        return requests.get(url=select_xz_url, headers=headers)

    # 定义方法_修改部门信息
    def test_upate_emp(self, emp_id, headers, data):
        upate_url = self.url + "/api/company/department/" + emp_id
        return requests.put(url=upate_url, headers=headers, json=data)

    # 定义方法_查看部门
    # 定义方法_删除部门
    def test_delete_emp(self, emp_id, headers):
        delet_url = self.url + "/api/company/department/" + emp_id
        return requests.delete(url=delet_url, headers=headers)

    # 定义方法_查看部门
