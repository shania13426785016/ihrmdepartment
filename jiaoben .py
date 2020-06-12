# 1 导包
import requests
import unittest
import pymysql
# 连接数据库
# pymysql.Connect("localhost","root","root","")
# 创建游标


# 2请求登录接口_测试用例-登录成功
login_url = "http://ihrm-test.itheima.net/api/sys/login"
respone = requests.post(url=login_url,
              headers={"Content-Type": "application/json"},
              json={"mobile": "13800000002", "password": "123456"}
              )
# 3查看返回的数据
print("查看登录接口返回的数据",respone.json())
token = "Bearer "+respone.json().get("data")
print("令牌:",token)

# 查询组织架构列表
select_url = "http://ihrm-test.itheima.net/api/company/department"
headers = {"Authorization":token}
respone1 = requests.get(url=select_url, headers=headers)
# print("获取组织架构列表返回的数据:", respone1.json())


# 添加部门
url = "http://ihrm-test.itheima.net"

emp_url = url + "/api/company/department"
headers = {"Content-Type": "application/json", "Authorization": token}
data = {"name": "猪猪侠部门", "code": "009"}
respone = requests.post(url=emp_url, headers=headers, json=data)
print("添加部门返回的结果:",respone.json())
# 保存新增部门的id
id = respone.json().get("data").get("id")
print("员工id:",id)

# 查询部门
select_xz_url = url + "/api/company/department/" + id
headers={"Authorization": token}
repone = requests.get(url=select_xz_url, headers=headers)
print("查询员工接口返回的信息:",repone.json())
#

# 修改部门信息
upate_url = url + "/api/company/department/" + id
headers = {"Content-Type": "application/json", "Authorization": token}
data = {"name": "吧啦啦小魔仙部门",
        "code": "011",
        "manager": "小黄",
        "introduces": "吃货"}
report = requests.put(url=upate_url,headers=headers,json=data)
print("查看修改接口返回的结果:",respone.json())
#
# 查询部门
select_xz_url = url + "/api/company/department/" + id
headers={"Authorization": token}
repone2 = requests.get(url=select_xz_url, headers=headers)
print("查询员工接口返回的信息:",repone2.json())
#
# # 删除部门
delet_url=url + "/api/company/department/" +id
headers={"Authorization": token}
respone = requests.delete(url=delet_url,headers=headers)
print("删除部门接口返回的结果:",respone.json())

# 查询部门
select_xz_url = url + "/api/company/department/" + id
headers={"Authorization": token}
repone2 = requests.get(url=select_xz_url, headers=headers)
print("查询员工接口返回的信息:",repone2.json())