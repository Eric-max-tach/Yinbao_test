import sys
import time

sys.path.append(r"C:\Users\Administrator\PycharmProjects\PythonProject")

import unittest

from appium import webdriver
from parameterized import parameterized
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.parse_csv import parse_csv

from common.startend import StartEnd
from page.operations import *
from page.scenarios import *
import logging
import re
import ddt

logging = logging.getLogger()

class TestCaseInterface(StartEnd):
    def testRechargeAndCouponIssue(self):
        """
            测试会员模块中会员充值功能和优惠券发放功能
        """
        logging.info("==========testRechargeAndCouponIssue==========")
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
        CashInterfaceOpn(self.driver).wait_toast_disappear()
        time.sleep(15)  # 才进入收银页面时，应用不是全屏，所以需要等待一段时间，才能定位到元素。否则，定位到的元素位置是偏移的，进行不了任何操作

        # 点击“点击选择会员”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/customer_rl"))
        #  .click())
        CashInterfaceOpn(self.driver).click_select_member_btn()

        # 获取会员搜索框，并发送值“1”
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.XPATH, "//*[@text='输入卡号/手机/姓名搜索会员']"))
        #  .send_keys("1"))
        SelectMemberOpn(self.driver).input_search_input_one()

        # 点击“确定”键，进入“会员详情”页面
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")))
        #  .click())
        SelectMemberOpn(self.driver).click_confirm_btn()

        # 获取未兑换商品之前的积分值
        # before_points = (WebDriverWait(self.driver, 10, 0.5, None)
        #                  .until(lambda x: (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/point_tv")))
        #                  .get_attribute("text"))
        before_points = MembershipDetailOpn(self.driver).get_points()

        # 点击积分兑换按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/exchange_btn")
        # ))
        #  .click())
        MembershipDetailOpn(self.driver).click_points_exchange_btn()

        # 获取前两项元素以及对应的积分值
        # points_exchange_list = (WebDriverWait(self.driver, 10, 0.5, None)
        #         .until(lambda x: (
        #     x.find_elements(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/root_ll")
        # )))
        points_exchange_list = PointExchangeOpn(self.driver).get_points_exchange_list()

        points = [] # 记录所消耗的积分值

        for i in range(2):  # 获取前两项元素以及对应的积分值
            # 获取“积分兑换商品”列表中，指定序号元素的积分值
            # needed_point = (
            #     WebDriverWait(points_exchange_list[i], 10, 0.5, None)
            #     .until(lambda x: (
            #         x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/need_point_tv")
            #     ))
            #     .get_attribute("text")
            # )
            needed_point = PointExchangeOpn(self.driver).get_points_exchange_item_points(i)

            # 记录当前兑换商品所需要的积分值
            points.append(float(needed_point))

            # 点击“积分兑换商品”列表中，指定序号的元素
            # points_exchange_list[i].click()
            PointExchangeOpn(self.driver).click_points_exchange_item(i)

        # 点击“兑换”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")
        # ))
        #  .click())
        PointExchangeOpn(self.driver).click_points_exchange_btn()

        # 获取兑换商品之后的积分值
        after_points_1 = MembershipDetailOpn(self.driver).get_points()

        # 判断积分值是否正确减少
        self.assertEqual(float(before_points) - float(sum(points)), float(after_points_1))

        # 点击积分兑换按钮
        MembershipDetailOpn(self.driver).click_points_exchange_btn()

        # # 滑动列表，直到滑动到屏幕底部
        # # # 获取“兑换商品”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        # # product_view = (WebDriverWait(self.driver, 10, 0.5, None)
        # #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/product_list")))
        # # product_view_bounds = product_view.get_attribute('bounds')
        # # # 使用正则表达式提取两个坐标对
        # # matches = re.findall(r'\[(\d+),(\d+)\]', product_view_bounds)
        # # top_left_x , top_left_y = int(matches[0][0]), int(matches[0][1])    # 第一个坐标对
        # # lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])   # 第二个坐标对
        # top_left_x, top_left_y, lower_right_x, lower_right_y = PointExchangeOpn(self.driver).get_points_exchange_view_size()
        #
        # # 判断是否已经滑动到列表底部的标志位
        # last_product = ""
        #
        # # 获取屏幕的大小
        # size_dict = self.driver.get_window_size()
        #
        # # 滑动到列表底部
        # while True:
        #     # 获取当前显示在“兑换商品”视图中，品名元素列表
        #     # product_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #     #                 .until(lambda x: x.find_elements(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/product_name_tv")))
        #     # if last_product == product_eles[-1].get_attribute("text"):
        #     #     break
        #     # last_product = product_eles[-1].get_attribute("text")
        #     if last_product == PointExchangeOpn(self.driver).get_points_exchange_item_name(-1):
        #         break
        #     last_product = PointExchangeOpn(self.driver).get_points_exchange_item_name(-1)
        #
        #     # 滑动“兑换商品”列表
        #     BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        start_y=(lower_right_y * 0.9) / size_dict['height'],
        #                                        end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        end_y=(top_left_y * 0.9) / size_dict['height'], duration=2)
        #
        #     # product_eles.clear()
        last_product = PointExchangeScenarios(self.driver).get_last_point_exchange_goods_name() #   获得"积分兑换商品"列表的最后一个元素的名称

        # 在搜索框输入获取到的最后一个元素
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/input_et")
        # ))
        #  .send_keys(last_product))
        PointExchangeOpn(self.driver).send_keys_search_input(last_product)

        # 获取第一项元素以及对应的积分值
        points_exchange_list = PointExchangeOpn(self.driver).get_points_exchange_list()

        points.clear()  # 记录所消耗的积分值

        for i in range(1):  # 获取前两项元素以及对应的积分值
            # 获取“积分兑换商品”列表中，指定序号元素的积分值
            needed_point = PointExchangeOpn(self.driver).get_points_exchange_item_points(i)

            # 记录当前兑换商品所需要的积分值
            points.append(float(needed_point))

            # 点击“积分兑换商品”列表中，指定序号的元素
            PointExchangeOpn(self.driver).click_points_exchange_item(i)

        # 点击“兑换”按钮
        PointExchangeOpn(self.driver).click_points_exchange_btn()

        # 获取兑换商品之后的积分值
        after_points_2 = MembershipDetailOpn(self.driver).get_points()

        # 判断积分值是否正确减少
        self.assertEqual(float(after_points_1) - float(sum(points)), float(after_points_2))


if __name__ == '__main__':
    unittest.main()