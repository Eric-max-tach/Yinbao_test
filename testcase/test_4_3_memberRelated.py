import random
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
from collections import OrderedDict

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

        # 点击"自用品(收银用)"分类按钮
        _ = CashInterfaceOpn(self.driver).click_category_btn(3)

        # 从当前屏幕所显示的菜品中随机选择两个商品
        product_names = []   # 用于记录所选商品的名字
        product_prices = []  # 用于记录所选商品的价格
        actual_product_num = min(19, CashInterfaceOpn(self.driver).get_goods_list_num() - 1)    # 除去"新增商品"按钮,一页最多获取到19个商品信息
        product_indexs = random.sample(range(1, actual_product_num), actual_product_num // 2) # 随机生成一组不重复的商品序号
        for i in range(len(product_indexs)):
            product_index = product_indexs[i]
            CashInterfaceOpn(self.driver).click_goods_btn(product_index)

            # 获取指定序号的商品名
            product_names.append(CashInterfaceOpn(self.driver).get_goods_name(product_index))

            # 获取指定序号的商品价格
            logging.info(product_index)
            product_prices.append(CashInterfaceOpn(self.driver).get_goods_price(product_index))

        # 将订单列表滑动到顶部
        # # 获取“订单”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        # # order_view_bounds = (WebDriverWait(self.driver, 10, 0.5, None)
        # #                .until(lambda x: x.find_element(
        # #                 By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls"))
        # #                .get_attribute("bounds"))
        # # # 使用正则表达式提取两个坐标对
        # # matches = re.findall(r'\[(\d+),(\d+)\]', order_view_bounds)
        # # top_left_x , top_left_y = int(matches[0][0]), int(matches[0][1])    # 第一个坐标对
        # # lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])   # 第二个坐标对
        # top_left_x, top_left_y, lower_right_x, lower_right_y = CashInterfaceOpn(self.driver).get_order_view_size()
        #
        # # 获取屏幕的大小
        # size_dict = self.driver.get_window_size()
        #
        # # 先将订单列表滑动到顶部
        # while True:
        #     # 获取当前屏幕中订单视图框内所有商品的序号的元素
        #     # product_ids_in_order_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #     #                              .until(lambda x: x.find_elements(By.XPATH,
        #     #                                                               "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/no_tv']")))
        #     product_ids_in_order_eles = CashInterfaceOpn(self.driver).get_goods_num_list()
        #
        #     # 判断当前屏幕中的订单位置,第一个商品的序号是否为"01.",如果为1则说明已经滑动到顶部
        #     if product_ids_in_order_eles[0].text == "01.":
        #         break
        #
        #     # 从下往上滑动"订单列表"
        #     BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        start_y=(top_left_y * 1.1) / size_dict['height'],
        #                                        end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        end_y=(lower_right_y * 0.9) / size_dict['height'], duration=2)
        CashInterfaceOpn(self.driver).scroll_order_list_to_top()

        # 将订单列表滑动到底部，并统计订单中包含的商品名和商品价格，返回两个字典，分别为订单中的商品名和商品价格
        # 统计在订单中的商品名和商品价格
        """
            1. 在 Python 3.7 及更高版本中，字典（dict）会按照元素添加的顺序记录
            2. 在 Python 3.6 或更早版本使用字典，插入顺序可能不受保障,需要使用collections.OrderedDict 来确保插入顺序
        """
        product_names_in_order = OrderedDict()  # 用于记录订单中商品的名字
        product_prices_in_order = OrderedDict()  # 用于记录订单中商品的价格

        # # 判断是否已经滑动到列表底部的标志位
        # last_id_in_order = "0"
        #
        # while True:
        #     # 获取当前屏幕中订单视图框内所有商品的序号的元素
        #     product_ids_in_order_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #                                  .until(lambda x: x.find_elements(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/no_tv']")))
        #
        #     # 获得当前屏幕中订单视图框内所有商品的名称和价格元素
        #     product_names_in_order_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #                                  .until(lambda x: x.find_elements(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/plu_name_tv']")))
        #     product_prices_in_order_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #                                  .until(lambda x: x.find_elements(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/price_tv']")))
        #
        #     """
        #         可能会出现当前屏幕中订单视图框中最后一个元素"商品序号","商品名字","商品价格"不能同时获取的情况
        #         当上述情况发生时,就先不处理最后一个元素
        #     """
        #     min_len = min(min(len(product_ids_in_order_eles), len(product_names_in_order_eles)), len(product_prices_in_order_eles))
        #
        #     for i in range(min_len): # 遍历订单视图框内所有商品的序号元素,并将其添加到列表中
        #         product_id_in_order = product_ids_in_order_eles[i].get_attribute('text')    # 商品在订单中的编号
        #         if product_id_in_order not in product_names_in_order:
        #             product_names_in_order[product_id_in_order] = product_names_in_order_eles[i].text
        #         if product_id_in_order not in product_prices_in_order:
        #             product_prices_in_order[product_id_in_order] = product_prices_in_order_eles[i].text.split('￥')[-1] # 去掉符号后提取数字
        #
        #     if product_ids_in_order_eles[min_len - 1].get_attribute('text') == last_id_in_order: # 用于判断是否滑动到列表底部
        #         break
        #
        #     last_id_in_order = product_ids_in_order_eles[min_len - 1].get_attribute('text')
        #
        #     # 滑动"订单列表"
        #     BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        start_y=(lower_right_y * 0.9) / size_dict['height'],
        #                                        end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        end_y=(lower_right_y * 0.5) / size_dict['height'], duration=2)
        #
        #     # 清空列表
        #     product_ids_in_order_eles.clear()
        #     product_names_in_order_eles.clear()
        #     product_prices_in_order_eles.clear()
        CashInterfaceOpn(self.driver).scroll_order_list_to_bottom(product_names_in_order, product_prices_in_order)

        # 判断记录订单中商品的名字和价格与从菜单中选取的商品的名字和价格是否相等
        product_names_in_order = list(product_names_in_order.values())
        product_prices_in_order = list(product_prices_in_order.values())
        self.assertEqual(len(product_names_in_order), len(product_names)) # 先判断商品数量是否相等
        self.assertEqual(len(product_prices_in_order), len(product_prices))  # 先判断商品数量是否相等
        for i in range(len(product_names_in_order)):    # 再判断商品名和价格是否相等
            self.assertEqual(product_names_in_order[i], product_names[i])
            self.assertEqual(product_prices_in_order[i], product_prices[i])

        # 点击"收银"按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x : x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/checkout_action_ll"))
        #  .click())
        CashInterfaceOpn(self.driver).click_cash_btn()

        # 在收银详情页,点击"储蓄卡"按钮
        RechargeDetailOpn(self.driver).click_value_card_btn()

        # 在选择会员页面,输入键盘数字"5",并点击"确定"按钮
        RechargeDetailOpn(self.driver).input_search_input_five()
        RechargeDetailOpn(self.driver).click_confirm_btn()

        # 在会员详情页,获取扣款前的会员余额
        before_deduction_balance = MembershipDetailOpn(self.driver).get_balance()

        # 点击"选择会员"按钮
        MembershipDetailOpn(self.driver).click_select_member_btn()

        # 获取实际的实收金额
        actual_total_amount = RechargeDetailOpn(self.driver).get_actual_amount_text()

        # 在收银详情页,点击"确定"按钮,确认付款
        RechargeDetailOpn(self.driver).click_confirm_btn()

        # 在收银页面,判断左侧的订单栏是否为空
        """
            判断逻辑：获取订单列表中第一个商品的序号的元素，如果在指定时间内没有找到该元素，会抛出超时异常，则说明订单被成功清空
        """
        try:
            # 获取当前屏幕中订单视图框内所有商品的序号的元素
            # (WebDriverWait(self.driver, 2, 0.5, None)
            #                              .until(lambda x: x.find_element(By.XPATH,
            #                                                               "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/no_tv']")))
            BasePage(self.driver).get_presence_element_need_exception(locator=CashInterface.OrderViewGoodsNums, need_screenshot=0)
        except Exception as e:
            # 判断捕获的异常是否是超时异常（即订单被成功清空）
            self.assertTrue(isinstance(e, TimeoutException))

        # 在收银页面,点击"点击选择会员"按钮
        CashInterfaceOpn(self.driver).click_select_member_btn()

        # 在选择会员页面,点击键盘数字"5",并点击确定按钮
        SelectMemberOpn(self.driver).input_search_input_five()
        RechargeDetailOpn(self.driver).click_confirm_btn()

        # 在会员详情页,获取扣款后的会员余额
        after_deduction_balance = MembershipDetailOpn(self.driver).get_balance()

        # 判断扣款是否正确
        self.assertEqual(int(float(after_deduction_balance) + float(actual_total_amount)), int(float(before_deduction_balance)))

if __name__ == '__main__':
    unittest.main()