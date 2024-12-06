import sys
import time

from src.base.basepage import BasePage
from src.page.operations import LoginInPageOpn, IndustrySelectionPageOpn, MessageCenterOpn

sys.path.append(r"C:\Users\Administrator\PycharmProjects\PythonProject\src")

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.startend import StartEnd
import logging
import re

logging = logging.getLogger()

class TestCaseInterface(StartEnd):
    def testMeassageClear(self):
        """
            收银页面清除“库存预警”模块的消息记录
        """
        logging.info("==========test_MessageClear==========")
        # 获取系统权限请求页的文本信息，从而得到需要点击多少次“允许”按钮
        permission_page_text = LoginInPageOpn(self.driver).permission_page_text()  # 文本信息类似于“第 1 项权限（共 3 项）”
        match = re.search(r"（共 (\d+) 项）", permission_page_text)
        if match:
            num = int(match.group(1))
        else:
            raise Exception("无法匹配文本信息")

        # 连续点击三次“允许”按钮""
        for i in range(num):
            LoginInPageOpn(self.driver).click_permission_allow_btn()

        # 点击“体验账号”按钮
        LoginInPageOpn(self.driver).try_login_btn()
        time.sleep(2)

        # 点击“我已了解，立即体验”按钮
        (WebDriverWait(self.driver, 10, 0.5, None)
         .until(lambda x: x.find_element(
            By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/try_btn"))
         .click())

        # 点击“餐饮行业”按钮
        IndustrySelectionPageOpn(self.driver).food_industry_btn()

        # 选择“text=pspldemo0082”的账号
        (WebDriverWait(self.driver, 10, 0.5, None)
         .until(lambda x: x.find_element(
            By.XPATH, "//*[@class='android.widget.LinearLayout']/*[@text='pspldemo0082']"))
         .click())

        # 获取“文件下载完成”Toast，当该元素出现后，才能进行下一步
        e = (WebDriverWait(self.driver, 10, 0.5, None)
             .until_not(lambda x: x.find_element(
            By.XPATH, "//*[@class='android.widget.Toast']")))

        # 点击“未读消息”按钮
        time.sleep(15)   # 才进入收银页面时，应用不是全屏，所以需要等待一段时间，才能定位到元素。否则，定位到的元素位置是偏移的，进行不了任何操作
        unread_message_btn = (WebDriverWait(self.driver, 10, 0.5, None)
         .until(lambda x: x.find_element(
            By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/notice_ib"
        )))
        unread_message_btn.click()
        # CashInterfaceOpn(self.driver).click_unread_message_btn()

        # 点击“库存预警”按钮
        # # 获取屏幕窗口的大小
        # size_dict = self.driver.get_window_size()
        # actions = ActionChains(self.driver)
        # # 输入源设备列表为空
        # actions.w3c_actions.devices = []
        # # =============点击屏幕指定位置，“库存预警”按钮位于屏幕的（0.1875, 0.4741）的位置===========
        # # 添加新的输入源到设备中
        # new_input = actions.w3c_actions.add_pointer_input("touch", "finger1")
        # # 指针移动到x轴的0.1875的位置，y轴的0.4741的位置
        # new_input.create_pointer_move(x=size_dict['width']*0.1875, y=size_dict['height']*0.4741)
        # # 按住鼠标左键
        # new_input.create_pointer_down()
        # # 等待1秒
        # new_input.create_pause(1)
        # # 释放鼠标左键
        # new_input.create_pointer_up(MouseButton.LEFT)
        # # 执行动作
        # actions.perform()
        BasePage(self.driver).click_screen(start_x=0.1875, start_y=0.4741, duration=1)  # 点击屏幕的（0.1875, 0.4741）的位置
        time.sleep(2)

        # 进入消息中心后，点击“库存预警”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.XPATH, "//*[@text='库存预警']"))
        #  .click())
        MessageCenterOpn(self.driver).click_stock_btn()

        # 通过兄弟元素定位法，找到“库存预警”的数量
        # inventory_warning_num = (WebDriverWait(self.driver, 10, 0.5, None)
        #         .until(lambda x: x.find_element(
        #     By.XPATH, "//*[@text='库存预警']/following-sibling::*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/count_tv']")).text)
        inventory_warning_num = MessageCenterOpn(self.driver).get_stock_warning_num()
        logging.info("库存预警数量为：%s" % inventory_warning_num)
        # 如果库存预警数量大于0，则执行下一步操作
        if inventory_warning_num > 0:
            # 点击“全选”按钮
            # (WebDriverWait(self.driver, 10, 0.5, None)
            #  .until(lambda x: x.find_element(
            #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/select_all_iv"))
            #  .click())
            MessageCenterOpn(self.driver).click_select_all_btn()

            # 点击“忽略此商品”按钮
            # (WebDriverWait(self.driver, 10, 0.5, None)
            #  .until(lambda x: x.find_element(
            #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/left_btn"))
            #  .click())
            MessageCenterOpn(self.driver).click_ignore_this_goods_btn()

            # 通过兄弟元素定位法，再次获得“库存预警”的数量
            # new_inventory_warning_num = (WebDriverWait(self.driver, 10, 0.5, None)
            #                          .until(lambda x: x.find_element(
            #     By.XPATH,
            #     "//*[@text='库存预警']/following-sibling::*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/count_tv']")).text)
            new_inventory_warning_num = MessageCenterOpn(self.driver).get_stock_warning_num()

            # 判断“库存预警”数量是否为0
            self.assertEqual(new_inventory_warning_num, 0)

        # 点击“页面返回”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/back_tv"))
        #  .click())
        MessageCenterOpn(self.driver).click_back_btn()

if __name__ == '__main__':
    unittest.main()