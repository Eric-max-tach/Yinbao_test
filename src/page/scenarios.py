from collections import OrderedDict
from typing import Optional, Dict

from src.base.basepage import *
from src.page.operations import PointExchangeOpn, LoginInPageOpn, NotAvailableCouponOpn


class LoginScenario(BasePage):
    """
        定义了与登录相关的场景
    """
    # 输入账号名和密码，并且点击登录按钮
    def fillin_account_pwd_and_login(self, username: str, password: str):
        """
        在登录界面，输入账号和密码，并点击登录按钮

        :param str username: 账号
        :param str password: 密码

        Example
        -------
        >>> username = "admin"  # 登录账号
        >>> password = "pwd123"    # 登录密码
        >>> LoginScenario(self.driver).fillin_account_pwd_and_login(username, password)
        """
        LoginInPageOpn(self.driver).input_account(username) # 账号输入框输入账号名
        LoginInPageOpn(self.driver).input_password(password)    # 密码输入框输入密码
        LoginInPageOpn(self.driver).click_login_btn()   # 在输入账号和密码后点击登录按钮

class NotAvailableCouponScenario(BasePage):
    """
        定义了不可用优惠券页面相关的场景
    """
    # 统计“不可用优惠券”页面下，未生效优惠券的数量，用字典记录每一条优惠券号码，并返回该字典
    def get_unavailable_coupon_num(self, coupon_number_dic: Optional[Dict[dict, OrderedDict]] = None, coupon_number_extend_dic: Optional[Dict[dict, OrderedDict]] = None, is_first: bool = True) -> tuple[Optional[Dict[dict, OrderedDict]],  Optional[Dict[dict, OrderedDict]]]:
        """
        统计“不可用优惠券”页面下，“未生效”优惠券的数量，用字典记录每一条优惠券号码，并返回该字典

        python 3.6及以上可以直接传入python提供的字典数据类型（dict），也可以传入有序字典类型（OrderDict）
        python 3.6以下只能传入有序字典类型（OrderDict）

        :param dict coupon_number_dic:   统计“未生效”优惠券编号的字典，默认为空
        :param dict coupon_number_extend_dic:    统计添加新的“未生效”优惠券后，记录新增“未生效”优惠券编号的字典，默认为空
        :param bool is_first: 判断是否为第一次统计“未生效”优惠券编号，如果是第一次统计，则将记录信息添加到coupon_number_dic字典中。如果不是第一次统计，则将记录信息添加到coupon_number_extend_dic字典中
        :return: 统计“未生效”优惠券编号的字典， 新增“未生效”优惠券编号的字典

        Example
        -------
        >>>  Example 1
        >>>  coupon_number_dic = OrderedDict()  # 统计“未生效”优惠券编号的字典
        >>>  coupon_number_extend_dic = OrderedDict()   # 记录新增“未生效”优惠券编号的字典
        >>>  is_first = True # 第一次统计“未生效”优惠券数量
        >>>  coupon_number_dic, coupon_number_extend_dic = NotAvailableCouponScenario(self.driver).get_unavailable_coupon_num(coupon_number_dic, coupon_number_extend_dic, is_first)
        >>>  # 此时字典“coupon_number_dic”中记录着第一次统计的“未生效”优惠券编号，字典“coupon_number_extend_dic”仍然为空
        >>>
        >>>  Example 2
        >>>  coupon_number_dic = OrderedDict()  # 统计“未生效”优惠券编号的字典
        >>>  coupon_number_extend_dic = OrderedDict()   # 记录新增“未生效”优惠券编号的字典
        >>>  is_first = False # 第二次统计“未生效”优惠券数量
        >>>  coupon_number_dic, coupon_number_extend_dic = NotAvailableCouponScenario(self.driver).get_unavailable_coupon_num(coupon_number_dic, coupon_number_extend_dic, is_first)
        >>>  # 此时字典“coupon_number_dic”中记录着第一次统计的“未生效”优惠券编号，字典“coupon_number_extend_dic”记录着相较于第一次统计的“未生效”的优惠券，在第二次新增的“未生效”的优惠券编号
        """

        # 获取“未生效优惠券”视图框列表的大小，并返回视图框左上角和右下角的坐标值
        top_left_x, top_left_y, lower_right_x, lower_right_y = NotAvailableCouponOpn(
            self.driver).get_not_available_coupon_view_size()

        # 判断是否已经滑动到列表底部的标志位
        last_coupon_number_index = "0"

        # 获取屏幕的大小
        size_dict = self.driver.get_window_size()

        # 统计优惠券号码
        while True:
            # 获取当前显示在“未生效”视图中，优惠券号码元素列表
            # coupon_no_eles = (WebDriverWait(self.driver, 10, 0.5, None)
            #                .until(lambda x: x.find_elements(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_code_tv']")))
            coupon_no_eles = NotAvailableCouponOpn(self.driver).get_not_available_coupon_number_list()
            for i in range(len(coupon_no_eles)):
                coupon_no = coupon_no_eles[i].text
                if coupon_no not in coupon_number_dic:
                    if is_first:
                        coupon_number_dic[coupon_no] = 1  # 如果是第一次统计，则将记录添加到coupon_number_dic字典中
                    else:
                        coupon_number_extend_dic[coupon_no] = 1  # 如果不是第一次统计，则将记录添加到额外记录字典（coupon_number_extend_dic）中
            if last_coupon_number_index == coupon_no_eles[-1].text:  # 用于判断是否滑动到列表底部
                break
            last_coupon_number_index = coupon_no_eles[-1].text

            # 滑动“小吃券”列表
            BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               start_y=(lower_right_y * 0.9) / size_dict['height'],
                                               end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               end_y=(lower_right_y * 0.5) / size_dict['height'], duration=10)
            coupon_no_eles.clear()  # 清空列表

        logging.info("top_left_x:{} , top_left_y:{}".format(top_left_x, top_left_y))
        logging.info("lower_right_x:{} , lower_right_y:{}".format(lower_right_x, lower_right_y))
        logging.info(
            "start_x:{}, start_y:{}, end_x:{}, end_y:{}".format(((lower_right_x + top_left_x) / 2),
                                                                (lower_right_y * 0.8),
                                                                ((lower_right_x + top_left_x) / 2), (top_left_y * 1.2)))

        return coupon_number_dic, coupon_number_extend_dic

class PointExchangeScenarios(BasePage):
    """
    定义了积分兑换页面相关的场景
    """
    # 获得"积分兑换商品"列表的最后一个元素的名称
    def get_last_point_exchange_goods_name(self) -> str:
        """
        在“积分兑换”页面下，获取“积分兑换商品”视图框列表中，最后一项可兑换商品的名称

        :return: 最后一项可兑换商品的名称

        Example
        -------
        >>>  product_name = PointExchangeScenarios(self.driver).get_last_point_exchange_goods_name()
        >>>  print("最后一项可兑换商品的名称为：{}".format(product_name))
        >>>  # 最后一项可兑换商品的名称为：商品1
        """
        # 获取“兑换商品”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        top_left_x, top_left_y, lower_right_x, lower_right_y = PointExchangeOpn(
            self.driver).get_points_exchange_view_size()

        # 判断是否已经滑动到列表底部的标志位
        last_product = ""

        # 获取屏幕的大小
        size_dict = self.driver.get_window_size()

        # 滑动到列表底部
        while True:
            # 获取当前显示在“兑换商品”视图中，品名元素列表
            if last_product == PointExchangeOpn(self.driver).get_points_exchange_item_name(-1):
                break
            last_product = PointExchangeOpn(self.driver).get_points_exchange_item_name(-1)

            # 滑动“兑换商品”列表
            BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               start_y=(lower_right_y * 0.9) / size_dict['height'],
                                               end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               end_y=(top_left_y * 0.9) / size_dict['height'], duration=2)

        return last_product