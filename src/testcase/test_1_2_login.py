import sys
sys.path.append(r"C:\Users\Administrator\PycharmProjects\PythonProject")

import time
import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By

from src.common.startend import StartEnd
import logging
import re

logging = logging.getLogger()


class TestLogin(StartEnd):
    def test_trylogin(self):
        logging.info("==========test_trylogin==========")
        # 获取系统权限请求页中的文本信息，从而得到需要点击多少次“允许”按钮
        permission_page_text = LoginInPageOpn(self.driver).permission_page_text()  # 文本信息类似于“第 1 项权限（共 3 项）”
        match = re.search(r"（共 (\d+) 项）", permission_page_text)
        if match:
            num = int(match.group(1))
        else:
            raise Exception("无法匹配文本信息")

        # 连续点击三次“允许”按钮
        for i in range(num):
            LoginInPageOpn(self.driver).click_permission_allow_btn()

        # 自定义显式等待条件，查找并点击“体验账号”的按钮
        # try:
        #     ele = WebDriverWait(self.driver, 10, 0.5, None).until(
        #         lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/try_tv"))
        #     ele.click()
        # except Exception as e:
        #     raise e
        LoginInPageOpn(self.driver).try_login_btn()
        time.sleep(2)

        # 点击“我已了解，立即体验”按钮
        self.driver.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/try_btn").click()
        time.sleep(2)

        # 点击“餐饮行业”按钮
        # self.driver.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/food_version_ll").click()
        IndustrySelectionPageOpn(self.driver).food_industry_btn()
        time.sleep(2)

        # 滑动账号列表
        # 获取屏幕窗口的大小
        size_dict = self.driver.get_window_size()
        actions = ActionChains(self.driver)
        # 输入源设备列表为空
        actions.w3c_actions.devices = []
        # ==============手指：从屏幕下面7/10的位置向上滑动到屏幕4/10的位置===============
        # 添加新的输入源到设备中
        new_input = actions.w3c_actions.add_pointer_input("touch", "finger1")
        # 指针移动到x轴的居中位置，y轴0.7位置
        new_input.create_pointer_move(x=size_dict["width"] / 2, y=size_dict["height"] * 0.7)
        # 按住鼠标左键
        new_input.create_pointer_down()
        # 等待1秒
        new_input.create_pause(1)
        # 向上滑动
        new_input.create_pointer_move(x=size_dict["width"] / 2, y=size_dict["height"] * 0.4)
        # 松开鼠标左键
        new_input.create_pointer_up(MouseButton.LEFT)
        # 执行动作
        actions.perform()
        time.sleep(2)

        # 选择“text=chenxunyou12”的账号
        self.driver.find_element(By.XPATH, "//*[@class='android.widget.LinearLayout']/*[@text='chenxunyou12']").click()
        time.sleep(2)

        # 在体验账号登录界面，点击“员工登录”按钮
        # self.driver.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn").click()
        TryLogInPageOpn(self.driver).click_employee_login_btn()
        time.sleep(2)

        # 获取 Toast 的文本信息
        print(TryLogInPageOpn(self.driver).get_toast_text())
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()