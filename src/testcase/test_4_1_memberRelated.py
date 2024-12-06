import sys
import time

sys.path.append(r"C:\Users\Administrator\PycharmProjects\PythonProject")

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.startend import StartEnd
import logging
import re

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

        # 获取会员搜索框，并发送值“5”
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.XPATH, "//*[@text='输入卡号/手机/姓名搜索会员']"))
        #  .send_keys("1"))
        SelectMemberOpn(self.driver).input_search_input_one()

        # 点击“确定”键，进入“会员详情”页面
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")))
        #  .click())
        SelectMemberOpn(self.driver).click_confirm_btn()

        # 获取充值之前的余额
        # balance_before_recharge = (WebDriverWait(self.driver, 10, 0.5, None)
        #                             .until(lambda x: x.find_element(By.XPATH, "//*[@text='余额']/following-sibling::*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/balance_tv']"))
        #                             .text)
        balance_before_recharge = MembershipDetailOpn(self.driver).get_balance()

        # 点击“充值”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/recharge_btn"))
        #  .click())
        MembershipDetailOpn(self.driver).click_recharge_btn()

        # 获取充值列表项，并选取第4个充值项（即充￥500赠优惠券[小吃券] X 1张）
        # eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #          .until(EC.presence_of_all_elements_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/root_rl")))
        # )
        # eles[3].click() # 选取第4个充值项
        MemberRechargeOpn(self.driver).select_recharge_item(3)

        # 选择“现金”充值
        MemberRechargeOpn(self.driver).click_cash_btn()

        # 点击“确定充值”键，进入“会员详情”页面
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")))
        #  .click())
        MemberRechargeOpn(self.driver).click_confirm_btn()

        # 获取充值之后的余额
        # balance_after_recharge = (WebDriverWait(self.driver, 10, 0.5, None)
        #                            .until(lambda x: x.find_element(By.XPATH,
        #                                                            "//*[@text='余额']/following-sibling::*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/balance_tv']"))
        #                            .text)
        balance_after_recharge = MembershipDetailOpn(self.driver).get_balance()

        # 断言充值之后的金额是否是在充值之前的金额上增加了500元
        self.assertEqual(float(balance_after_recharge), float(balance_before_recharge) + 500)

        # 在“会员详情页”点击“优惠券”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_check_btn"))
        #  .click())
        MembershipDetailOpn(self.driver).click_coupon_btn()

        # 在“优惠券”页面点击“不可用券”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/action_1_tv"))
        #  .click())
        CouponOpn(self.driver).click_unavailable_coupon_btn()

        """
            前提：
                1、只支持单线程
                2、通过充值得到的优惠券状态为“未生效”
                
            判断逻辑：
                1、先获取“未生效”视图框列表的大小，得到视图框左上角和右下角的坐标值
                2、创建字典1，用于统计优惠券号码
                3、获取显示在当前视图中的优惠券元素列表，并得到其优惠券号码。检查该号码是否已经记录在字典中，如果不存在则将该号码记录在字典中
                4、使用一个标志位用于判断是否已经滑动到列表底部，具体为判断当前视图中的优惠券元素列表中最后一个元素的优惠券号码是否等于标志位记录的号码，如果相等则说明已经滑动到列表底部，跳出循环。若不相等，则进行下一步
                5、利用w3c Actions和第一步获得的视图大小值对视图列表进行滑动
                6、循环执行步骤3-5，直到滑动到列表底部
                7、统计完优惠券号码后，跳转到充值页点击赠送优惠券的充值项
                8、回到“优惠券不可用”页面，重新获取“未生效”视图框列表的大小，得到视图框左上角和右下角的坐标值（因为“未生效”视图框列表的大小是会随着优惠券数量的变化而变化）
                9、再创建一个字典2，用于统计新增的优惠券号码
                10、获取显示在当前视图中的优惠券元素列表，并得到其优惠券号码。检查该号码是否已经记录在字典1中，如果不存在则将该优惠券号码记录在字典2中
                12、使用一个标志位用于判断是否已经滑动到列表底部，具体为判断当前视图中的优惠券元素列表中最后一个元素的优惠券号码是否等于标志位记录的号码，如果相等则说明已经滑动到列表底部，跳出循环。若不相等，则进行下一步
                13、利用w3c Actions和第一步获得的视图大小值对视图列表进行滑动
                14、循环执行步骤3-5，直到滑动到列表底部
                15、通过断言判断字典2的长度是否为1，如果长度等于1，则说明成功添加了一张优惠券
        """
        # 创建字典，用于统计优惠券号码
        coupon_number_dic = {}

        # 统计“不可用优惠券”页面下，未生效优惠券的数量，用字典记录每一条优惠券号码，并返回该字典
        coupon_number_dic, _ = NotAvailableCouponScenario(self.driver).get_unavailable_coupon_num(coupon_number_dic=coupon_number_dic)

        # # # 获取“未生效”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        # # coupon_view = (WebDriverWait(self.driver, 10, 0.5, None)
        # #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv")))  # 获得小吃券视图
        # # coupon_view_bounds = coupon_view.get_attribute('bounds')
        # # # 使用正则表达式提取两个坐标对
        # # matches = re.findall(r'\[(\d+),(\d+)\]', coupon_view_bounds)
        # # top_left_x , top_left_y = int(matches[0][0]), int(matches[0][1])    # 第一个坐标对
        # # lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])   # 第二个坐标对
        # top_left_x, top_left_y, lower_right_x, lower_right_y = NotAvailableCouponOpn(self.driver).get_not_available_coupon_view_size()
        #
        # # 判断是否已经滑动到列表底部的标志位
        # last_coupon_number_index = "0"
        #
        # # 获取屏幕的大小
        # size_dict = self.driver.get_window_size()
        #
        # # 统计优惠券号码
        # while True:
        #     # 获取当前显示在“未生效”视图中，优惠券号码元素列表
        #     # coupon_no_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #     #                .until(lambda x: x.find_elements(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_code_tv']")))
        #     coupon_no_eles = NotAvailableCouponOpn(self.driver).get_not_available_coupon_number_list()
        #     for i in range(len(coupon_no_eles)):
        #         coupon_no = coupon_no_eles[i].text
        #         if coupon_no not in coupon_number_dic:
        #             coupon_number_dic[coupon_no] = 1    # 记录每一个优惠券编号
        #     if last_coupon_number_index == coupon_no_eles[-1].text: # 用于判断是否滑动到列表底部
        #         break
        #     last_coupon_number_index = coupon_no_eles[-1].text
        #
        #     # 滑动“小吃券”列表
        #     BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        start_y=(lower_right_y * 0.9) / size_dict['height'],
        #                                        end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        end_y=(lower_right_y * 0.5) / size_dict['height'], duration=10)
        #     coupon_no_eles.clear()
        # logging.info("top_left_x:{} , top_left_y:{}".format(top_left_x, top_left_y))
        # logging.info("lower_right_x:{} , lower_right_y:{}".format(lower_right_x, lower_right_y))
        # logging.info(
        #     "start_x:{}, start_y:{}, end_x:{}, end_y:{}".format(((lower_right_x + top_left_x) / 2), (lower_right_y * 0.8),
        #                                                     ((lower_right_x + top_left_x) / 2), (top_left_y * 1.2)))

        logging.info("coupon_number_dic:{}".format(coupon_number_dic))
        # 连续点击两次“返回键”，回到“会员详情”页面
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)

        # 点击“充值”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/recharge_btn"))
        #  .click())
        MembershipDetailOpn(self.driver).click_recharge_btn()

        # 获取充值列表项，并选取第4个充值项（即充￥500赠优惠券[小吃券] X 1张）
        # eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #         .until(
        #     EC.presence_of_all_elements_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/root_rl")))
        #         )
        # eles[3].click()  # 选取第4个充值项
        MemberRechargeOpn(self.driver).select_recharge_item(3)

        # 选择“现金”充值
        MemberRechargeOpn(self.driver).click_cash_btn()

        # 点击“确定充值”键，进入“会员详情”页面
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: (x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")))
        #  .click())
        MemberRechargeOpn(self.driver).click_confirm_btn()

        # 在“会员详情页”点击“优惠券”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_check_btn"))
        #  .click())
        MembershipDetailOpn(self.driver).click_coupon_btn()

        # 在“优惠券”页面点击“不可用券”按钮
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/action_1_tv"))
        #  .click())
        CouponOpn(self.driver).click_unavailable_coupon_btn()

        # 创建字典，用于统计新增的优惠券号码
        coupon_number_extend_dic = {}

        # 统计“不可用优惠券”页面下，未生效优惠券的数量，用字典记录每一条优惠券号码，并返回该字典
        _, coupon_number_extend_dic = NotAvailableCouponScenario(self.driver).get_unavailable_coupon_num(coupon_number_dic=coupon_number_dic, coupon_number_extend_dic=coupon_number_extend_dic, is_first=False)

        # # # 获取“未生效”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        # # coupon_view = (WebDriverWait(self.driver, 10, 0.5, None)
        # #                .until(lambda x: x.find_element(By.ID,
        # #                                                "cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv")))  # 获得小吃券视图
        # # coupon_view_bounds = coupon_view.get_attribute('bounds')  # "[480,92][1440,1080]"
        # # # 使用正则表达式提取两个坐标对
        # # matches = re.findall(r'\[(\d+),(\d+)\]', coupon_view_bounds)
        # # top_left_x, top_left_y = int(matches[0][0]), int(matches[0][1])  # 第一个坐标对
        # # lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])  # 第二个坐标对
        # top_left_x, top_left_y, lower_right_x, lower_right_y = NotAvailableCouponOpn(
        #     self.driver).get_not_available_coupon_view_size()
        #
        # # 判断是否已经滑动到列表底部的标志位
        # last_coupon_number_index = "0"
        #
        # # 获取屏幕的大小
        # size_dict = self.driver.get_window_size()
        #
        # # 统计优惠券号码
        # while True:
        #     # 获取当前显示在“未生效”视图中，优惠券号码元素列表
        #     # coupon_no_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #     #                   .until(lambda x: x.find_elements(By.XPATH,
        #     #                                                    "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_code_tv']")))
        #     coupon_no_eles = NotAvailableCouponOpn(self.driver).get_not_available_coupon_number_list()
        #     for i in range(len(coupon_no_eles)):
        #         coupon_no = coupon_no_eles[i].text
        #         if coupon_no not in coupon_number_dic:
        #             coupon_number_extend_dic[coupon_no] = 1  # 记录新增的优惠券号码到字典中
        #
        #     if last_coupon_number_index == coupon_no_eles[-1].text: # 用于判断是否滑动到列表底部
        #         break
        #     last_coupon_number_index = coupon_no_eles[-1].text
        #
        #     # 滑动“小吃券”列表
        #     BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        start_y=(lower_right_y * 0.9) / size_dict['height'],
        #                                        end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
        #                                        end_y=(lower_right_y * 0.5) / size_dict['height'], duration=2)
        #
        #     coupon_no_eles.clear()

        logging.info("coupon_number_extend_dic:{}".format(coupon_number_extend_dic))

        # 判断优惠券是否被成功添加，如果“coupon_number_extend_dic”的长度等于1，则优惠券被成功添加
        self.assertEqual(len(coupon_number_extend_dic), 1)


if __name__ == '__main__':
    unittest.main()