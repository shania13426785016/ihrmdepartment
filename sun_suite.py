# 1导包
import unittest
import HTMLTestRunner_PY3
# 2生成测试套件
import app
from script.test_emp import TestIhrmEmp

suit = unittest.TestSuite()
# 3添加测试用例
suit.addTest(unittest.makeSuite(TestIhrmEmp))
# 4测试用例的命名
filename = app.base_path + "/report/Ihrm_report.html"
# 5
# 将测试报告写入命名好的测试文件里面
with open(filename, "wb")as f:
    sunner = HTMLTestRunner_PY3.HTMLTestRunner(f, description="ihrm部门的删改查测试用例",
                                               title='ihrm测试报告', )

    # 运行测试报告
    sunner.run(suit)
