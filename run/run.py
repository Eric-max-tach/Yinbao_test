import unittest
import HtmlTestRunner
import time
import logging

if __name__=='__main__':
    # 测试指定目录下，以test开头的py文件
    testSuite = unittest.TestLoader().discover('../testcase/','test*.py')
    # 定义文件名，文件名由年、月、日、时、分、秒构成
    filename = "..\\report\\Storm_{}".format(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))

    # 通过HtmlTestRunner执行测试用例，并生成报告
    logging.info("start run test case...")
    HtmlTestRunner.HTMLTestRunner(output=filename).run(testSuite)