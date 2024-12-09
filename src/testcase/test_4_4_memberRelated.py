import random
import sys
import time

from src.base.basepage import BasePage
from src.page.locators import CashInterface
from src.page.operations import *

sys.path.append(r"C:\Users\Administrator\PycharmProjects\PythonProject\src")

import unittest

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.startend import StartEnd
import logging
import re
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

        # 在收银页面,点击"点击选择会员"按钮
        CashInterfaceOpn(self.driver).click_select_member_btn()

        # 在选择会员页面,点击键盘数字"5",并点击确定按钮
        SelectMemberOpn(self.driver).input_search_input_five()
        RechargeDetailOpn(self.driver).click_confirm_btn()

        # 在会员详情页,获取扣款前的会员余额
        before_deduction_balance = MembershipDetailOpn(self.driver).get_balance()

        # 在会员详情页，点击“选择会员”按钮
        MembershipDetailOpn(self.driver).click_select_member_btn()

        # 在收银页面，点击“优惠券”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_ll")
        # ))
        #  .click())
        CashInterfaceOpn(self.driver).click_coupon_btn()

        # 在选择优惠券页面，点击“通用券码”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/comment_coupon_rb")
        # ))
        #  .click())
        SelectCouponOpn(self.driver).click_common_coupon_btn()

        # # 获得“优惠券列表”视图的大小，并返回其左上角和右下角的坐标值
        # # coupons_recycle_view = (WebDriverWait(self.driver, 10, 0.5, None)
        # #                      .until(lambda x: (
        # #                         x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupons_recycle_view")
        # #                     )))
        # # coupons_recycle_view_bounds = coupons_recycle_view.get_attribute("bounds")
        # # # 使用正则表达式提取两个坐标对
        # # matches = re.findall(r'\[(\d+),(\d+)\]', coupons_recycle_view_bounds)
        # # top_left_x , top_left_y = int(matches[0][0]), int(matches[0][1])    # 第一个坐标对
        # # lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])   # 第二个坐标对
        # top_left_x, top_left_y, lower_right_x, lower_right_y = SelectCouponOpn(self.driver).get_coupon_list_view_size()
        #
        # # 判断是否已经滑动到列表底部的标志位
        # last_coupon_name = "."
        #
        # # 获取屏幕的大小
        # size_dict = self.driver.get_window_size()
        #
        # while True:
        #     # 获取当前屏幕中优惠券列表视图框内所有优惠券的名称的元素集合
        #     # coupon_name_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #     #                  .until(lambda x: (
        #     #                     x.find_elements(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_name_tv")
        #     #                 )))
        #     coupon_name_eles = BasePage(self.driver).get_elements(SelectCouponInterface.CouponNameText)
        #
        #     # 获取当前屏幕中优惠券列表视图框内所有优惠券的添加按钮的元素集合
        #     # coupon_addbtn_ele = (WebDriverWait(self.driver, 10, 0.5, None)
        #     #                  .until(lambda x: (
        #     #                     x.find_elements(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/add_iv")
        #     #                 )))
        #     coupon_addbtn_ele = BasePage(self.driver).get_elements(SelectCouponInterface.CouponAddBtn)
        #
        #     # 判断当前优惠券列表视图中，是否有名称为“20减5”的优惠券
        #     lens = min(len(coupon_name_eles), len(coupon_addbtn_ele))   # 有可能存在列表最后一个元素没有加载出来的情况
        #     for i in range(lens):
        #         coupon_name = coupon_name_eles[i].text
        #         if str.startswith(coupon_name, "20减5"):
        #             logging.info("coupon_name:{}".format(coupon_name))
        #             coupon_addbtn_ele[i].click()
        #
        #     if last_coupon_name == coupon_name_eles[lens - 1].text: # 用于判断是否已经滑动到列表底部
        #         break
        #     last_coupon_name = coupon_name_eles[lens - 1].text
        #
        #     # 滑动“优惠券”列表视图
        #     BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                         start_y=(lower_right_y * 0.9) / size_dict['height'],
        #                                         end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                         end_y=(lower_right_y * 0.5) / size_dict['height'], duration=2)
        #
        #     # 清空列表
        #     coupon_name_eles.clear()
        #     coupon_addbtn_ele.clear()
        # 查找并点击指定次数和名称的优惠券
        SelectCouponOpn(self.driver).find_and_click_coupon(coupon_prefix_name="20减5", coupon_num=1, is_add=True)

        # 在选择优惠券页面，点击“确定”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x : (
        #     x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")
        # ))
        #  .click())
        SelectCouponOpn(self.driver).click_confirm_btn()

        # 在收银页面，将订单列表滑动到顶部
        CashInterfaceOpn(self.driver).scroll_order_list_to_top()

        """
            在收银页面，遍历左侧订单栏中每一个商品的”折扣值”元素，并将这个值保存在有序字典中
        """
        # # 获取“订单”视图框列表的大小，得到                                                            视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        # order_view_bounds = (WebDriverWait(self.driver, 10, 0.5, None)
        #                .until(lambda x: x.find_element(
        #                 By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls"))
        #                .get_attribute("bounds"))
        # # 使用正则表达式提取两个坐标对
        # matches = re.findall(r'\[(\d+),(\d+)\]', order_view_bounds)
        # top_left_x , top_left_y = int(matches[0][0]), int(matches[0][1])    # 第一个坐标对
        # lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])   # 第二个坐标对
        #
        # # 获取屏幕的大小
        # size_dict = self.driver.get_window_size()
        #
        # # 统计在订单中的商品的折扣值
        # """
        #     1. 在 Python 3.7 及更高版本中，字典（dict）会按照元素添加的顺序记录
        #     2. 在 Python 3.6 或更早版本使用字典，插入顺序可能不受保障,需要使用collections.OrderedDict 来确保插入顺序
        # """
        # product_discounts_in_order = OrderedDict()  # 用于记录订单中商品的折扣值
        #
        # # 判断是否已经滑动到列表底部的标志位
        # last_id_in_order = "0"
        #
        # while True:
        #     # 获取当前屏幕中订单视图框内所有商品的序号的元素集合
        #     product_ids_in_order_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #                                  .until(lambda x: x.find_elements(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/no_tv']")))
        #
        #     # 获取当前屏幕中订单视图框内所有商品的折扣的元素集合
        #     product_discounts_in_order_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #                                  .until(lambda x: x.find_elements(By.XPATH,
        #                                                                   "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/discount_tv']")))
        #
        #     """
        #         可能会出现当前屏幕中订单视图框中最后一个元素"商品序号","商品折扣值"不能同时获取的情况
        #         当上述情况发生时,就先不处理最后一个元素
        #     """
        #     min_len = min(len(product_ids_in_order_eles), len(product_discounts_in_order_eles))
        #
        #     for i in range(min_len):    # 遍历订单视图框内所有商品的序号元素,并将其添加到列表中
        #         product_id_in_order = product_ids_in_order_eles[i].get_attribute('text')  # 商品在订单中的编号
        #         if product_id_in_order not in product_discounts_in_order:
        #                 product_discounts_in_order[product_id_in_order] = product_discounts_in_order_eles[i].text   # 折扣值的存储形式为“折扣: -0.08”
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
        #                                        end_y=(lower_right_y * 0.5) / size_dict['height'], duration=10)
        #
        #     # 清空列表
        #     product_ids_in_order_eles.clear()
        #     product_discounts_in_order_eles.clear()
        # 统计在订单中的商品的折扣值列表
        # 统计在订单中的商品的折扣值
        """
            1. 在 Python 3.7 及更高版本中，字典（dict）会按照元素添加的顺序记录
            2. 在 Python 3.6 或更早版本使用字典，插入顺序可能不受保障,需要使用collections.OrderedDict 来确保插入顺序
        """
        product_discounts_in_order = OrderedDict()  # 用于记录订单中商品的折扣值
        product_discounts_in_order = CashInterfaceOpn(self.driver).get_discount_value(product_discounts_in_order)


        # 将统计的折扣值进行求和，判断折扣金额是否为5元
        product_discounts_in_order = list(product_discounts_in_order.values())
        product_discounts_in_order = [s.removeprefix("折扣: -") for s in product_discounts_in_order]  # # 折扣值的存储形式为“折扣: -0.08”，只需要获取值的部分
        self.assertEqual(sum(map(float, product_discounts_in_order)), float(5))

        # 在收银页面，获取实收金额值
        actual_receipt_price = CashInterfaceOpn(self.driver).get_receipt_price_text()

        # 在收银页面，获取总额金额值
        total_price = CashInterfaceOpn(self.driver).get_total_price_text()

        # 在收银页面，获取折扣金额值
        discount_price = CashInterfaceOpn(self.driver).get_discount_price_text()

        # 判断折扣后的金额是否正确
        self.assertEqual(float(actual_receipt_price), float(total_price) - float(discount_price))

        # 在收银页面，点击收银按钮
        CashInterfaceOpn(self.driver).click_cash_btn()

        # 在收银详情页，获取实收金额值，并判断在收银页面获取的实收金额值和在收银详情页获取的实收金额值是否相等
        self.assertEqual(float(RechargeDetailOpn(self.driver).get_actual_amount_text()), float(actual_receipt_price))

        # 在收银详情页，点击“确定”按钮
        RechargeDetailOpn(self.driver).click_confirm_btn()

        # 在收银页面，点击“点击选择会员”按钮
        CashInterfaceOpn(self.driver).click_select_member_btn()

        # 在“选择会员”页面，输入数字“5”，并点击“确定”按钮
        SelectMemberOpn(self.driver).input_search_input_five()
        SelectMemberOpn(self.driver).click_confirm_btn()

        # 在会员详情页,获取扣款后的会员余额
        after_deduction_balance = MembershipDetailOpn(self.driver).get_balance()

        # 判断扣款后的会员余额是否正确
        self.assertEqual(round(float(after_deduction_balance),1), round(float(before_deduction_balance) - float(actual_receipt_price), 1))   # 四舍五入保留一位小数

if __name__ == '__main__':
    unittest.main()