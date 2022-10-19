import sys
path = 'D:\PythonProject'
sys.path.append(path)  # 声明包查找的路径
from UIautomation.atstudy.test_run.BSTestRunner import BSTestRunner

import unittest
import time


test_dir = r'D:\PythonProject\UIautomation\atstudy\test_case'
report_dir = r'D:\PythonProject\UIautomation\atstudy\reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
now = time.strftime("%Y-%m-%d-%H_%M_%S")
report_name = report_dir + '/' + now + 'test_report.html'
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='选课功能测试报告', description='我的选课功能测试报告')
    runner.run(discover)

print(3331)
