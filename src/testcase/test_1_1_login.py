import sys
sys.path.append(r"/")

import unittest

import ddt
import time
from src.common.startend import StartEnd
from src.base.parse_csv import parse_csv
from src.page.operations import LoginInPageOpn
from src.page.scenarios import LoginScenario
import os
import logging
import re

logging = logging.getLogger()

@ddt.ddt
class TestLogin(StartEnd):
    """
        1、os.getcwd() 返回当前工作目录（即 Python 进程的当前目录）
        2、os.path.dirname(path) 返回指定路径的父目录
        3、这是字符串 "data"，它表示一个文件夹名称。接下来会把它拼接到路径中
        4、os.path.basename(__file__) 会从这个路径中提取出文件名部分。例如，如果脚本的路径是 /home/user/myproject/test.py，那么 os.path.basename(__file__) 返回的就是 "test.py"
        5、split(".") 将文件名根据 "." 分割成一个列表，[0] 获取文件名的第一部分（去掉扩展名）。比如，"test.py".split(".") 会得到 ["test", "py"]，取 [0] 后，得到 "test"
    """
    file_dir = os.path.join(os.path.dirname(os.getcwd()), "data", os.path.basename(__file__).split(".")[0]) + ".csv"    # 拼接测试数据的路径

    """
        1、@ddt.data()，圆括号中可以传递列表或元组
        2、这里传递的是两个列表，代表两个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    # @ddt.data(["admin_001", "password_001"], ["admin_002", "password_002"])
    @ddt.data(*parse_csv(file_dir))  # "../data/test_1_1_login.csv"
    @ddt.unpack
    def test_login(self, username, password):
        logging.info("==========test_login==========")

        # 获取系统权限请求页中的文本信息，从而得到需要点击多少次“允许”按钮
        permission_page_text = LoginInPageOpn(self.driver).permission_page_text()   # 文本信息类似于“第 1 项权限（共 3 项）”
        match = re.search(r"（共 (\d+) 项）", permission_page_text)
        if match:
            num = int(match.group(1))
        else:
            raise Exception("无法匹配文本信息")

        # 连续点击上次“允许”按钮
        for i in range(num):
            LoginInPageOpn(self.driver).click_permission_allow_btn()

        # 执行输入账号名和密码，并且点击登录按钮的命令
        LoginScenario(self.driver).fillin_account_pwd_and_login(username, password)

        # 获取 Toast 的文本信息
        # text = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        text = LoginInPageOpn(self.driver).get_toast_text()

        # 判断 Toast 的文本信息时候匹配
        self.assertEqual(text, "输入的账号密码错误")

        # 截图
        self.driver.get_screenshot_as_file(r"homepage.png")
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()