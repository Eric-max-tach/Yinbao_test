from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException

from src.base.basepage import *
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
import re

from src.page.locators import *

logging = logging.getLogger()

class LoginInPageOpn(BasePage):
    """
        登录页元素操作
    """
    def permission_page_text(self):
        """
        在系统权限请求页面中，获取current_page_text中的文本信息，即“第 1 项权限（共 3 项）”

        :return: 当前正在处理第几项权限请求，即“第 1 项权限（共 3 项）”

        Example
        -------
        >>> permission_page_text = LoginInPageOpn(self.driver).permission_page_text()
        """
        logging.info('==========permission_page_text==========')
        # 获取文本信息元素的文本内容，即获取内容“第 1 项权限（共 3 项）”
        ele = self.get_presence_element(LoginInPageLocators.PermissionPageText)
        return ele.get_attribute("text")

    # 在系统权限请求页面中，点击“同意”按钮
    def click_permission_allow_btn(self):
        """
        在系统权限请求页面中，点击“同意”按钮

        Example
        -------
        >>> LoginInPageOpn(self.driver).click_permission_allow_btn()
        """
        logging.info('==========click_permission_allow_btn==========')
        # 查找点击元素
        # ele = self.driver.find_element(*LoginInPageLocators.PermissionAllowBtn)
        ele = self.get_clickable_element(LoginInPageLocators.PermissionAllowBtn)    # 替换为添加了显示等待的元素定位方法
        ele.click()


    # 账号输入框输入账号名
    def input_account(self, username: str):
        """
        账号输入框输入账号名

        :param str username: 账号名

        Example
        -------
        >>> username = "Eric"
        >>> LoginInPageOpn(self.driver).input_account(username)
        """
        logging.info('==========input_account==========')
        # ele = self.driver.find_element(*LoginInPageLocators.AccountInput)
        ele = self.get_visible_element(LoginInPageLocators.AccountInput)    # 替换为添加了显示等待的元素定位方法
        ele.send_keys(username)

    # 密码输入框输入密码
    def input_password(self, password: str):
        """
        密码输入框输入密码

        :param str password: 密码

        Example
        -------
        >>> password = "123"
        >>> LoginInPageOpn(self.driver).input_password(password)
        """
        logging.info('==========input_password==========')
        # ele = self.driver.find_element(*LoginInPageLocators.PasswordInput)
        ele = self.get_visible_element(LoginInPageLocators.PasswordInput)   # 替换为添加了显示等待的元素定位方法
        ele.send_keys(password)

    # 在输入账号和密码后点击登录按钮
    def click_login_btn(self):
        """
        在输入账号和密码后点击登录按钮

        Example
        -------
        >>>  LoginInPageOpn(self.driver).click_login_btn()
        """
        logging.info('==========click_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.LoginBtn)
        ele = self.get_clickable_element(LoginInPageLocators.LoginBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 获取Toast文本信息
    def get_toast_text(self) -> str:
        """
        获取Toast文本信息

        :return str: Toast文本信息

        Example
        -------
        >>>  LoginInPageOpn(self.driver).get_toast_text()
        """
        logging.info('==========get_toast_text==========')
        # ele = self.driver.find_element(*LoginInPageLocators.Toast)
        ele = self.get_presence_element(LoginInPageLocators.Toast)  # 替换为添加了显示等待的元素定位方法
        return ele.text

    # 体验账号按钮点击
    def try_login_btn(self):
        """
        体验账号按钮点击

        Example
        -------
        >>>  LoginInPageOpn(self.driver).try_login_btn()
        """
        logging.info('==========try_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.TryAccountBtn)
        ele = self.get_clickable_element(LoginInPageLocators.TryAccountBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 免费注册按钮点击
    def free_login_btn(self):
        """
        免费注册按钮点击

        Example
        -------
        >>>  LoginInPageOpn(self.driver).free_login_btn()
        """
        logging.info('==========free_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.FreeRegistBtn)
        ele = self.get_clickable_element(LoginInPageLocators.FreeRegistBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 联系客服按钮点击
    def contact_service_btn(self):
        """
        联系客服按钮点击

        Example
        -------
        >>>  LoginInPageOpn(self.driver).contact_service_btn()
        """
        logging.info('==========contact_service_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.ContactServiceBtn)
        ele = self.get_clickable_element(LoginInPageLocators.ContactServiceBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 账号+工号登录按钮点击
    def account_cashier_login_btn(self):
        """
        账号+工号登录按钮点击

        Example
        -------
        >>>  LoginInPageOpn(self.driver). account_cashier_login_btn()
        """
        logging.info('==========account_cashier_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.AccountCashierLoginBtn)
        ele = self.get_clickable_element(LoginInPageLocators.AccountCashierLoginBtn)    # 替换为添加了显示等待的元素定位方法
        ele.click()

class IndustrySelectionPageOpn(BasePage):
    """
        在登录页选择体验账号后，进入的行业选择页面的相关操作
    """
    # 零售行业按钮点击
    def retail_industry_btn(self):
        """
        零售行业按钮点击

        Example
        -------
        >>>  IndustrySelectionPageOpn(self.driver).retail_industry_btn()
        """
        logging.info('==========retail_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.RetailBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.RetailBtn)   # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 餐饮行业按钮点击
    def food_industry_btn(self):
        """
        餐饮行业按钮点击

        Example
        -------
        >>>  IndustrySelectionPageOpn(self.driver).food_industry_btn()
        """
        logging.info('==========food_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.FoodBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FoodBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 服装鞋帽按钮点击
    def clothes_shoes_industry_btn(self):
        """
        服装鞋帽按钮点击

        Example
        -------
        >>>  IndustrySelectionPageOpn(self.driver).clothes_shoes_industry_btn()
        """
        logging.info('==========clothes_shoes_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.ClothesShoesBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.ClothesShoesBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 生活服务按钮点击
    def service_industry_btn(self):
        """
        生活服务按钮点击

        Example
        -------
        >>>  IndustrySelectionPageOpn(self.driver).service_industry_btn()
        """
        logging.info('==========service_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.ServiceBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.ServiceBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 母婴行业按钮点击
    def maternal_supply_industry_btn(self):
        logging.info('==========maternal_supply_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.MaternalSupplyBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.MaternalSupplyBtn)   # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 宠物行业按钮点击
    def pet_industry_btn(self):
        logging.info('==========pet_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.PetBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.PetBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 烘焙行业按钮点击
    def bake_industry_btn(self):
        logging.info('==========bake_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.BakeBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.BakeBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 生鲜称重按钮点击
    def fresh_industry_btn(self):
        logging.info('==========fresh_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.FreshBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FreshBtn)    # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 美妆休闲按钮点击
    def leisure_industry_btn(self):
        logging.info('==========leisure_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.LeisureBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.LeisureBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 尽请期待按钮点击
    def future_industry_btn(self):
        logging.info('==========future_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.FutureBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FutureBtn)   # 替换为添加了显示等待的元素定位方法
        ele.click()

class TryLogInPageOpn(BasePage):
    """
        体验账号登录页元素操作
    """
    # 账号输入框文本获取
    def get_account_input_text(self) -> str:
        logging.info('==========get_account_input_text==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.AccountInput)
        ele = self.get_visible_element(TryLoginInPageLocators.AccountInput) # 替换为添加了显示等待的元素定位方法
        return ele.text

    # 工号输入框获取工号
    def get_job_number_input_text(self) -> str:
        logging.info('==========get_job_number_input_text==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.JobNumberInput)
        ele = self.get_visible_element(TryLoginInPageLocators.JobNumberInput)   # 替换为添加了显示等待的元素定位方法
        return ele.text

    # 工号输入框输入工号
    def input_job_number(self, job_number):
        logging.info('==========input_job_number==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.JobNumberInput)
        ele = self.get_visible_element(TryLoginInPageLocators.JobNumberInput)   # 替换为添加了显示等待的元素定位方法
        if len(self.get_job_number_input_text()) != 0:
            ele.clear() #   如果工号输入框中有内容，则先清空内容
        ele.send_keys(job_number)

    # 密码输入框输入密码
    def input_password(self, password):
        logging.info('==========input_password==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.PasswordInput)
        ele = self.get_visible_element(TryLoginInPageLocators.PasswordInput)    # 替换为添加了显示等待的元素定位方法
        ele.clear()
        ele.send_keys(password)

    # 员工登录按钮点击
    def click_employee_login_btn(self):
        logging.info('==========click_employee_login_btn==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.EmployeeLoginBtn)
        ele = self.get_clickable_element(TryLoginInPageLocators.EmployeeLoginBtn)   # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 管理后台按钮点击
    def click_manager_btn(self):
        logging.info('==========click_manager_btn==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.ManagerBtn)
        ele = self.get_clickable_element(TryLoginInPageLocators.ManagerBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 联系客服按钮点击
    def click_contact_service_btn(self):
        logging.info('==========click_contact_service_btn==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.ContactServiceBtn)
        ele = self.get_clickable_element(TryLoginInPageLocators.ContactServiceBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 交接班记录按钮
    def click_history_handover_btn(self):
        logging.info('==========click_history_handover_btn==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.HistoryHandoverBtn)
        ele = self.get_clickable_element(TryLoginInPageLocators.HistoryHandoverBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 获取Toast文本信息
    def get_toast_text(self) -> str:
        logging.info('==========get_toast_text==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.Toast)
        ele = self.get_presence_element(TryLoginInPageLocators.Toast)    # 替换为添加了显示等待的元素定位方法
        return ele.text

class CashInterfaceOpn(BasePage):
    """
        收银页面元素相关操作
    """
    # 点击未读消息按钮
    def click_unread_message_btn(self):
        logging.info('==========click_unread_message_btn==========')
        ele = self.get_presence_element(CashInterface.UreadMessageBtn)
        ele.click()

    # 等待Toast消息消失
    def wait_toast_disappear(self):
        logging.info('==========wait_toast_disappear==========')
        ele = self.get_presence_until_not_element(CashInterface.Toast)


    # 点击指定序号的“分类”按钮，并获得其分类名：
    def click_category_btn(self, category_num) -> str:
        logging.info('==========click_category_btn==========')
        eles = self.get_elements(CashInterface.CategoryList)
        eles[category_num].click()
        ele = self.get_presence_element(locator=CashInterface.CategoryText, element=eles[category_num])
        return ele.text

    # 点击某一分类下的“新增商品”按钮
    def click_add_product_btn(self):
        logging.info('==========click_add_product_btn==========')
        while True:
            eles = self.get_elements(CashInterface.GoodsList)
            # 获取列表中最后一个元素的文本值是不是"新增商品",如果不是则一直向下滑动列表,直到找到该元素
            try:
                self.get_presence_element_need_exception(locator=CashInterface.CategoryText, element=eles[-1], need_screenshot=0, timeout=1)   # 封装好的方法已经把异常给处理了，因此无法再获得异常信息，因此只能使用可以抛出异常的方法
            except TimeoutException:
                """
                    如果列表的最后一个元素不是“新增商品”，那么通过try模块中获取元素的方法在滑动屏幕到底部后就无法成功获取元素，这个是否就会报超时错误
                """
                ee = eles[-1].find_element(AppiumBy.XPATH, "//*[@text='新增商品']")
                print(ee.get_attribute("text"))
                eles[-1].click()
                break

            # 滑动屏幕，从屏幕的（0.5， 0.95）的位置滑动到屏幕的（0.5， 0.4）的位置，持续时间1s
            self.swipe_screen(start_x=0.5, start_y=0.95, end_x=0.5, end_y=0.4, duration=1)

            # 清空元素列表
            eles.clear()

    # 获取指定分类序号下,最新添加的商品名和商品售价
    def get_new_product_name_price(self) -> tuple:
        logging.info('==========get_new_product_name_price==========')
        while True:
            eles = self.get_elements(CashInterface.GoodsList)
            # 获取列表中最后一个元素的文本值是不是"新增商品",如果不是则一直向下滑动列表,直到找到该元素
            try:
                self.get_presence_element_need_exception(locator=CashInterface.CategoryText, element=eles[-1], need_screenshot=0, timeout=1)   # 封装好的方法已经把异常给处理了，因此无法再获得异常信息，因此只能使用可以抛出异常的方法
            except TimeoutException:
                """
                    如果列表的最后一个元素不是“新增商品”，那么通过try模块中获取元素的方法在滑动屏幕到底部后就无法成功获取元素，这个是否就会报超时错误
                """
                new_trade_name_ele = self.get_presence_element(locator=CashInterface.GoodsNameText,
                                                               element=eles[-2])
                new_selling_price_ele = self.get_presence_element(locator=CashInterface.GoodsPriceText,
                                                                  element=eles[-2])
                return new_trade_name_ele.get_attribute("text"), new_selling_price_ele.get_attribute("text")
            # 获取屏幕窗口的大小
            size_dict = self.driver.get_window_size()
            actions = ActionChains(self.driver)
            # 输入源设备列表为空
            actions.w3c_actions.devices = []
            # =============从屏幕指定位置滑动到另一个指定位置===========
            # 添加新的输入源到设备中
            new_input = actions.w3c_actions.add_pointer_input("touch", "finger1")
            # 指针移动到x轴的0.1875的位置，y轴的0.4741的位置
            new_input.create_pointer_move(x=size_dict['width'] * 0.5, y=size_dict['height'] * 0.95)
            # 按住鼠标左键
            new_input.create_pointer_down()
            # 等待1秒
            new_input.create_pause(1)
            # 向上滑动
            new_input.create_pointer_move(x=size_dict["width"] / 2, y=size_dict["height"] * 0.4)
            # 释放鼠标左键
            new_input.create_pointer_up(MouseButton.LEFT)
            # 执行动作
            actions.perform()
            time.sleep(2)

            # 清空元素列表
            eles.clear()

    # 点击“点击选择会员”按钮
    def click_select_member_btn(self):
        logging.info('==========click_select_member_btn==========')
        ele = self.get_presence_element(CashInterface.SelectMemberBtn)
        ele.click()

    # 获取当前分类下的商品列表的元素个数
    def get_goods_list_num(self) -> int:
        logging.info('==========get_goods_list_num==========')
        eles = self.get_elements(CashInterface.GoodsList)
        return len(eles)

    # 点击指定序号的商品
    def click_goods_btn(self, goods_num):
        logging.info('==========click_goods_btn==========')
        eles = self.get_elements(CashInterface.GoodsList)
        eles[goods_num - 1].click()

    # 获取指定序号的商品名
    def get_goods_name(self, goods_num) -> str:
        logging.info('==========get_goods_name==========')
        eles = self.get_elements(CashInterface.GoodsList)
        return self.get_presence_element(locator=CashInterface.GoodsNameText, element=eles[goods_num - 1]).get_attribute("text")

    # 获取指定序号的商品价格
    def get_goods_price(self, goods_num) -> str:
        logging.info('==========get_goods_price==========')
        eles = self.get_elements(CashInterface.GoodsList)
        return self.get_presence_element(locator=CashInterface.GoodsPriceText, element=eles[goods_num - 1]).get_attribute("text").split('￥')[-1] # 去掉符号后提取数字

    # 获取“订单”视图框的大小，并返回该视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
    def get_order_view_size(self) -> tuple:
        logging.info('==========get_order_view_size==========')
        ele = self.get_presence_element(CashInterface.OrderView)
        ele_bounds = ele.get_attribute('bounds')
        # 使用正则表达式提取两个坐标对
        matches = re.findall(r'\[(\d+),(\d+)\]', ele_bounds)
        top_left_x, top_left_y = int(matches[0][0]), int(matches[0][1])  # 第一个坐标对
        lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])  # 第二个坐标对
        return top_left_x, top_left_y, lower_right_x, lower_right_y

    # 获取当前屏幕中订单视图框内所有商品的序号的元素集合
    def get_goods_num_list(self) -> list:
        logging.info('==========get_goods_num_list==========')
        return self.get_elements(CashInterface.OrderViewGoodsNums)
    
    # 将订单列表滑动到顶部
    def scroll_order_list_to_top(self):
        logging.info('==========scroll_order_list_to_top==========')
        # 获取“订单”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        top_left_x, top_left_y, lower_right_x, lower_right_y = self.get_order_view_size()

        # 获取屏幕的大小
        size_dict = self.driver.get_window_size()

        # 先将订单列表滑动到顶部
        while True:
            # 获取当前屏幕中订单视图框内所有商品的序号的元素
            product_ids_in_order_eles = self.get_goods_num_list()

            # 判断当前屏幕中的订单位置,第一个商品的序号是否为"01.",如果为1则说明已经滑动到顶部
            if product_ids_in_order_eles[0].text == "01.":
                break

            # 从下往上滑动"订单列表"
            BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               start_y=(top_left_y * 1.1) / size_dict['height'],
                                               end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               end_y=(lower_right_y * 0.9) / size_dict['height'], duration=2)

    # 将订单列表滑动到底部，并统计订单中包含的商品名和商品价格，返回两个字典，分别为订单中的商品名和商品价格
    def scroll_order_list_to_bottom(self, product_names_in_order, product_prices_in_order) -> tuple:
        """
        :param product_names_in_order: product_names_in_order = OrderedDict()  # 用于记录订单中商品的名字
        :param product_prices_in_order: product_prices_in_order = OrderedDict()  # 用于记录订单中商品的价格
        :return: product_names_in_order, product_prices_in_order
        """
        logging.info('==========scroll_order_list_to_bottom==========')
        # 获取“订单”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        top_left_x, top_left_y, lower_right_x, lower_right_y = self.get_order_view_size()

        # 获取屏幕的大小
        size_dict = self.driver.get_window_size()

        # 判断是否已经滑动到列表底部的标志位
        last_id_in_order = "0"
        
        while True:
            # 获取当前屏幕中订单视图框内所有商品的序号的元素集合
            product_ids_in_order_eles = self.get_elements(CashInterface.OrderViewGoodsNums)

            # 获得当前屏幕中订单视图框内所有商品的名称和价格元素集合
            product_names_in_order_eles = self.get_elements(CashInterface.OrderViewGoodsNames)
            product_prices_in_order_eles = self.get_elements(CashInterface.OrderViewGoodsPrices)

            """
                可能会出现当前屏幕中订单视图框中最后一个元素"商品序号","商品名字","商品价格"不能同时获取的情况
                当上述情况发生时,就先不处理最后一个元素
            """
            min_len = min(min(len(product_ids_in_order_eles), len(product_names_in_order_eles)), len(product_prices_in_order_eles))

            for i in range(min_len): # 遍历订单视图框内所有商品的序号元素,并将其添加到列表中
                product_id_in_order = product_ids_in_order_eles[i].get_attribute('text')    # 商品在订单中的编号
                if product_id_in_order not in product_names_in_order:
                    product_names_in_order[product_id_in_order] = product_names_in_order_eles[i].text
                if product_id_in_order not in product_prices_in_order:
                    product_prices_in_order[product_id_in_order] = product_prices_in_order_eles[i].text.split('￥')[-1] # 去掉符号后提取数字

            if product_ids_in_order_eles[min_len - 1].get_attribute('text') == last_id_in_order: # 用于判断是否滑动到列表底部
                break

            last_id_in_order = product_ids_in_order_eles[min_len - 1].get_attribute('text')

            # 滑动"订单列表"
            BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               start_y=(lower_right_y * 0.9) / size_dict['height'],
                                               end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               end_y=(lower_right_y * 0.5) / size_dict['height'], duration=2)

            # 清空列表
            product_ids_in_order_eles.clear()
            product_names_in_order_eles.clear()
            product_prices_in_order_eles.clear()
        
        return product_names_in_order, product_prices_in_order

    # 点击“收银”按钮
    def click_cash_btn(self):
        logging.info('==========click_cash_btn==========')
        self.get_clickable_element(CashInterface.CashBtn).click()

    # 获取“实收金额”文本值
    def get_receipt_price_text(self) -> str:
        logging.info('==========get_receipt_price_text==========')
        return self.get_presence_element(CashInterface.ReceiptPriceText).text.removeprefix("￥")  # “实收金额”的文本形式为“￥1255”，所以需要移除前缀

    # 获取“总额”文本值
    def get_total_price_text(self) -> str:
        logging.info('==========get_total_price_text==========')
        return self.get_presence_element(CashInterface.TotalPriceText).text.removeprefix("总额")  # “总额”的文本形式为“总额1255”，所以需要移除前缀

    # 获取“折扣”文本值
    def get_discount_price_text(self) -> str:
        logging.info('==========get_discount_text==========')
        return self.get_presence_element(CashInterface.DiscountText).text.removeprefix("折扣")  # “折扣”的文本形式为“折扣1255”，所以需要移除前缀

    # 在订单栏下方点击“优惠券”图标按钮
    def click_coupon_btn(self):
        logging.info('==========click_coupon_btn==========')
        self.get_clickable_element(CashInterface.CouponBtn).click()

    # 统计在订单中的商品的折扣值列表
    def get_discount_value(self, product_discounts_in_order: dict):
        logging.info('==========get_discount_value==========')
        # 获取“订单”视图框列表的大小，得到视图框左上角和右下角的坐标值，即"[480,92][1440,1080]"
        top_left_x, top_left_y, lower_right_x, lower_right_y = self.get_order_view_size()

        # 获取屏幕的大小
        size_dict = self.driver.get_window_size()

        # 判断是否已经滑动到列表底部的标志位
        last_id_in_order = "0"

        while True:
            # 获取当前屏幕中订单视图框内所有商品的序号的元素集合
            product_ids_in_order_eles = self.get_elements(CashInterface.OrderViewGoodsNums)

            # 获取当前屏幕中订单视图框内所有商品的折扣的元素集合
            product_discounts_in_order_eles = self.get_elements(CashInterface.OrderViewGoodsDiscounts)

            """
                可能会出现当前屏幕中订单视图框中最后一个元素"商品序号","商品折扣值"不能同时获取的情况
                当上述情况发生时,就先不处理最后一个元素
            """
            min_len = min(len(product_ids_in_order_eles), len(product_discounts_in_order_eles))

            for i in range(min_len):  # 遍历订单视图框内所有商品的序号元素,并将其添加到列表中
                product_id_in_order = product_ids_in_order_eles[i].get_attribute('text')  # 商品在订单中的编号
                if product_id_in_order not in product_discounts_in_order:
                    product_discounts_in_order[product_id_in_order] = product_discounts_in_order_eles[
                        i].text  # 折扣值的存储形式为“折扣: -0.08”

            if product_ids_in_order_eles[min_len - 1].get_attribute('text') == last_id_in_order:  # 用于判断是否滑动到列表底部
                break

            last_id_in_order = product_ids_in_order_eles[min_len - 1].get_attribute('text')

            # 滑动"订单列表"
            BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               start_y=(lower_right_y * 0.9) / size_dict['height'],
                                               end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                               end_y=(lower_right_y * 0.5) / size_dict['height'], duration=10)

            # 清空列表
            product_ids_in_order_eles.clear()
            product_discounts_in_order_eles.clear()

        return product_discounts_in_order



class SelectCouponOpn(BasePage):
    """
        在收银页面的订单栏下方点击“优惠券”图标按钮后进入的选择优惠券页面元素的操作
    """
    # 点击“普通优惠券”按钮
    def click_normal_coupon_btn(self):
        logging.info('==========click_normal_coupon_btn==========')
        self.get_clickable_element(SelectCouponInterface.GeneralCouponBtn).click()

    # 点击“通用券码”按钮
    def click_common_coupon_btn(self):
        logging.info('==========click_common_coupon_btn==========')
        self.get_clickable_element(SelectCouponInterface.CommentCouponBtn).click()

    # 点击“券扫码下单”按钮
    def click_coupon_scan_btn(self):
        logging.info('==========click_coupon_scan_btn==========')
        self.get_clickable_element(SelectCouponInterface.CouponScanBtn).click()

    # 获得“优惠券列表”视图框大小，并返回其左上角和右下角的坐标值
    def get_coupon_list_view_size(self) -> tuple:
        logging.info('==========get_coupon_list_view_size==========')
        ele = self.get_presence_element(SelectCouponInterface.CouponListView)
        ele_bounds = ele.get_attribute('bounds')
        # 使用正则表达式提取两个坐标对
        matches = re.findall(r'\[(\d+),(\d+)\]', ele_bounds)
        top_left_x, top_left_y = int(matches[0][0]), int(matches[0][1])  # 第一个坐标对
        lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])  # 第二个坐标对

        return top_left_x, top_left_y, lower_right_x, lower_right_y

    # 点击指定序号的“优惠券列表”中优惠券的“添加”按钮
    def click_coupon_add_btn(self, coupon_id: int):
        logging.info('==========click_coupon_add_btn==========')
        eles = self.get_elements(SelectCouponInterface.CouponListView)
        eles[coupon_id].click()

    # 点击指定序号的“优惠券列表”中优惠券的“删除”按钮
    def click_coupon_delete_btn(self, coupon_id: int):
        logging.info('==========click_coupon_delete_btn==========')
        eles = self.get_elements(SelectCouponInterface.CouponListView)
        eles[coupon_id].click()

    # 查找并点击指定次数和名称的优惠券
    def find_and_click_coupon(self, coupon_prefix_name: str, coupon_num: int, is_add: bool):
        """
            查找并点击指定次数和名称的优惠券

            :param coupon_prefix_name: 所要查找的优惠券的名称的前缀
            :param coupon_num:  优惠券添加/删除个数
            :param is_add:  判断是添加还是删除优惠券，True为添加优惠券，False为删除优惠券
        """

        logging.info('==========find_and_click_coupon==========')
        top_left_x, top_left_y, lower_right_x, lower_right_y = self.get_coupon_list_view_size()

        # 判断是否已经滑动到列表底部的标志位
        last_coupon_name = "."

        # 获取屏幕的大小
        size_dict = self.driver.get_window_size()

        while True:
            # 获取当前屏幕中优惠券列表视图框内所有优惠券的名称的元素集合
            coupon_name_eles = self.get_elements(SelectCouponInterface.CouponNameText)

            # 获取当前屏幕中优惠券列表视图框内所有优惠券的添加按钮的元素集合
            coupon_addbtn_ele = self.get_elements(SelectCouponInterface.CouponAddBtn)

            # 获取当前屏幕中优惠券列表视图框内所有优惠券的删除按钮的元素集合
            coupon_deletebtn_ele = self.get_elements(SelectCouponInterface.CouponDeleteBtn)

            # 判断当前优惠券列表视图中，是否有名称为“20减5”的优惠券
            lens = min(len(coupon_name_eles), len(coupon_addbtn_ele))   # 有可能存在列表最后一个元素没有加载出来的情况
            for i in range(lens):
                coupon_name = coupon_name_eles[i].text
                if str.startswith(coupon_name, coupon_prefix_name):
                    if is_add:  # 添加优惠券
                        for j in range(coupon_num):
                            coupon_addbtn_ele[i].click()
                    else:   # 删除优惠券
                        for j in range(coupon_num):
                            coupon_deletebtn_ele[i].click()


            if last_coupon_name == coupon_name_eles[lens - 1].text: # 用于判断是否已经滑动到列表底部
                break
            last_coupon_name = coupon_name_eles[lens - 1].text

            # 滑动“优惠券”列表视图
            BasePage(self.driver).swipe_screen(start_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                                start_y=(lower_right_y * 0.9) / size_dict['height'],
                                                end_x=((lower_right_x + top_left_x) / 2) / size_dict['width'],
                                                end_y=(lower_right_y * 0.5) / size_dict['height'], duration=2)

            # 清空列表
            coupon_name_eles.clear()
            coupon_addbtn_ele.clear()
            coupon_deletebtn_ele.clear()


    # 点击“确定”按钮
    def click_confirm_btn(self):
        logging.info('==========click_confirm_btn==========')
        self.get_clickable_element(SelectCouponInterface.ConfirmBtn).click()

class NewProductPageOpn(BasePage):
    """
        新增商品元素操作
    """
    # 在“新增商品”页面，点击“生成”按钮，生成随机条码
    def click_generate_btn(self):
        logging.info('==========click_generate_btn==========')
        ele = self.get_clickable_element(NewProductPage.GenerateBtn)
        ele.click()

    # 获取商品条码文本框
    def get_barcode_input_text(self) -> str:
        logging.info('==========get_barcode_input_text==========')
        ele = self.get_visible_element(NewProductPage.BarcodeInput)
        return ele.text

    # 在“品名”输入框，输入商品名
    def input_product_name(self, product_name):
        logging.info('==========input_product_name==========')
        ele = self.get_visible_element(NewProductPage.NameInput)
        ele.clear()
        ele.send_keys(product_name)

    # 在“库存”输入框，输入库存
    def input_stock(self, stock):
        logging.info('==========input_stock==========')
        ele = self.get_visible_element(NewProductPage.StockInput)
        ele.clear()
        ele.send_keys(stock)

    # 在“售价”输入框，输入售价
    def input_price(self, price):
        logging.info('==========input_price==========')
        ele = self.get_visible_element(NewProductPage.PriceInput)
        ele.clear()
        ele.send_keys(price)

    # 在“进价”输入框，输入进价
    def input_purchase_price(self, purchase_price):
        logging.info('==========input_purchase_price==========')
        ele = self.get_visible_element(NewProductPage.PurchasePriceInput)
        ele.clear()
        ele.send_keys(purchase_price)

    # 点击“保存”按钮,保存新增商品
    def click_save_btn(self):
        logging.info('==========click_save_btn==========')
        ele = self.get_clickable_element(NewProductPage.SaveBtn)
        ele.click()


    # 点击“分类”下拉框
    def click_category_dropdown(self):
        logging.info('==========click_category_dropdown==========')
        ele = self.get_clickable_element(NewProductPage.CategoryDropdown)
        ele.click()

    # 在“分类”下拉框中，点击搜索栏并输入搜索内容
    def input_category_search_input(self, search_content):
        logging.info('==========input_category_search_input==========')
        ele = self.get_presence_element(NewProductPage.CategorySearchInput)
        ele.send_keys(search_content)

    # 在“分类”下拉框中，点击搜索结果集合中第一条搜索结果
    def click_search_result(self):
        logging.info('==========click_search_result==========')
        ele = self.get_clickable_element(NewProductPage.CategorySearchResult)
        ele.click()

    # 在“分类”下拉框中，点击“保存”按钮
    def click_category_save_btn(self):
        logging.info('==========click_save_btn==========')
        ele = self.get_clickable_element(NewProductPage.CategorySearchConfirmBtn)
        ele.click()

class MessageCenterOpn(BasePage):
    """
        消息中心元素操作
    """
    # 点击库存按钮
    def click_stock_btn(self):
        logging.info('==========click_stock_btn==========')
        ele = self.get_presence_element(MessageCenterPageLocators.StockWarningBtn)
        ele.click()

    # 获得“库存预警”的数量
    def get_stock_warning_num(self) -> int:
        logging.info('==========get_stock_warning_num==========')
        ele = self.get_presence_element(MessageCenterPageLocators.StockWarningCount)
        return int(ele.text)

    # 点击“全选”按钮
    def click_select_all_btn(self):
        logging.info('==========click_select_all_btn==========')
        ele = self.get_presence_element(MessageCenterPageLocators.SelectAllBtn)
        ele.click()

    # 点击“忽略此商品”按钮
    def click_ignore_this_goods_btn(self):
        logging.info('==========click_ignore_this_goods_btn==========')
        ele = self.get_presence_element(MessageCenterPageLocators.IgnoreThisGoodsBtn)
        ele.click()

    # 点击“返回”按钮
    def click_back_btn(self):
        logging.info('==========click_back_btn==========')
        ele = self.get_presence_element(MessageCenterPageLocators.BackBtn)
        ele.click()

class SelectMemberOpn(BasePage):
    """
        选择会员页面元素操作
    """
    # 在搜索框输入数字“1”
    def input_search_input_one(self):
        logging.info('==========input_search_input_one==========')
        ele = self.get_presence_element(SelectMemberPage.OneBtn)
        ele.click()

    # 在搜索框输入数字“2”
    def input_search_input_two(self):
        logging.info('==========input_search_input_two==========')
        ele = self.get_presence_element(SelectMemberPage.TwoBtn)
        ele.click()

    # 在搜索框输入数字“3”
    def input_search_input_three(self):
        logging.info('==========input_search_input_three==========')
        ele = self.get_presence_element(SelectMemberPage.ThreeBtn)
        ele.click()

    # 在搜索框输入数字“4”
    def input_search_input_four(self):
        logging.info('==========input_search_input_four==========')
        ele = self.get_presence_element(SelectMemberPage.FourBtn)
        ele.click()

    # 在搜索框输入数字“5”
    def input_search_input_five(self):
        logging.info('==========input_search_input_five==========')
        ele = self.get_presence_element(SelectMemberPage.FiveBtn)
        ele.click()

    # 在搜索框输入数字“6”
    def input_search_input_six(self):
        logging.info('==========input_search_input_six==========')
        ele = self.get_presence_element(SelectMemberPage.SixBtn)
        ele.click()

    # 在搜索框输入数字“7”
    def input_search_input_seven(self):
        logging.info('==========input_search_input_seven==========')
        ele = self.get_presence_element(SelectMemberPage.SevenBtn)
        ele.click()

    # 在搜索框输入数字“8”
    def input_search_input_eight(self):
        logging.info('==========input_search_input_eight==========')
        ele = self.get_presence_element(SelectMemberPage.EightBtn)
        ele.click()

    # 在搜索框输入数字“9”
    def input_search_input_nine(self):
        logging.info('==========input_search_input_nine==========')
        ele = self.get_presence_element(SelectMemberPage.NineBtn)
        ele.click()

    # 在搜索框输入数字“0”
    def input_search_input_zero(self):
        logging.info('==========input_search_input_zero==========')
        ele = self.get_presence_element(SelectMemberPage.ZeroBtn)
        ele.click()

    # 在搜索框输入数字“00”
    def input_search_input_double_zero(self):
        logging.info('==========input_search_input_double_zero==========')
        ele = self.get_presence_element(SelectMemberPage.ZeroZeroBtn)
        ele.click()

    # 在搜索框输入数字"."
    def input_search_input_dot(self):
        logging.info('==========input_search_input_dot==========')
        ele = self.get_presence_element(SelectMemberPage.DotBtn)
        ele.click()

    # 点击“删除”按钮
    def click_delete_btn(self):
        logging.info('==========click_delete_btn==========')
        ele = self.get_presence_element(SelectMemberPage.DeleteBtn)
        ele.click()

    # 点击“确定”按钮
    def click_confirm_btn(self):
        logging.info('==========click_confirm_btn==========')
        ele = self.get_presence_element(SelectMemberPage.ConfirmBtn)
        ele.click()

    # 点击“添加会员”按钮
    def click_add_member_btn(self):
        logging.info('==========click_add_member_btn==========')
        ele = self.get_presence_element(SelectMemberPage.AddMemberBtn)
        ele.click()

    # 点击“扫描”按钮
    def click_scan_btn(self):
        logging.info('==========click_scan_btn==========')
        ele = self.get_presence_element(SelectMemberPage.ScanBtn)
        ele.click()

    # 点击“返回”按钮
    def click_back_btn(self):
        logging.info('==========click_back_btn==========')
        ele = self.get_presence_element(SelectMemberPage.BackBtn)
        ele.click()

class MembershipDetailOpn(BasePage):
    """
        会员详情页元素操作
    """
    # 点击“充值”按钮
    def click_recharge_btn(self):
        logging.info('==========click_recharge_btn==========')
        ele = self.get_presence_element(MembershipDetailsPage.RechargeBtn)
        ele.click()

    # 点击“选择会员”按钮
    def click_select_member_btn(self):
        logging.info('==========click_select_member_btn==========')
        ele = self.get_presence_element(MembershipDetailsPage.SelectMemberBtn)
        ele.click()

    # 获取“余额”
    def get_balance(self):
        logging.info('==========get_balance==========')
        ele = self.get_presence_element(MembershipDetailsPage.BalanceText)
        return ele.text

    # 点击“优惠券查看”按钮
    def click_coupon_btn(self):
        logging.info('==========click_coupon_btn==========')
        ele = self.get_presence_element(MembershipDetailsPage.CouponViewBtn)
        ele.click()

    # 获取“积分”
    def get_points(self):
        logging.info('==========get_points==========')
        ele = self.get_presence_element(MembershipDetailsPage.PointsText)
        return ele.text

    # 点击“积分兑换”按钮
    def click_points_exchange_btn(self):
        logging.info('==========click_points_exchange_btn==========')
        ele = self.get_presence_element(MembershipDetailsPage.PointsExchangeBtn)
        ele.click()

class MemberRechargeOpn(BasePage):
    """
        会员充值页面元素定位操作
    """
    # 选择指定充值项
    def select_recharge_item(self, item_no):
        logging.info('==========select_recharge_item==========')
        eles = self.get_elements(MemberRechargePage.RechargeItemList)
        eles[item_no].click()

    # 点击“现金”充值按钮
    def click_cash_btn(self):
        logging.info('==========click_cash_btn==========')
        ele = self.get_presence_element(MemberRechargePage.CashBtn)
        ele.click()

    # 点击“银联卡”充值按钮
    def click_union_btn(self):
        logging.info('==========click_union_btn==========')
        ele = self.get_presence_element(MemberRechargePage.UnionPayBtn)
        ele.click()

    # 点击“收款码”充值按钮
    def click_qrcode_btn(self):
        logging.info('==========click_qrcode_btn==========')
        ele = self.get_presence_element(MemberRechargePage.QRCodeBtn)
        ele.click()

    # 点击“支付宝”充值按钮
    def click_alipay_btn(self):
        logging.info('==========click_alipay_btn==========')
        ele = self.get_presence_element(MemberRechargePage.AliPayBtn)
        ele.click()

    # 点击“微信”充值按钮
    def click_wechat_btn(self):
        logging.info('==========click_wechat_btn==========')
        ele = self.get_presence_element(MemberRechargePage.WechatBtn)
        ele.click()

    # 点击“三福支付”充值按钮
    def click_sfpay_btn(self):
        logging.info('==========click_sfpay_btn==========')
        ele = self.get_presence_element(MemberRechargePage.SFPayBtn)
        ele.click()

    # 点击“确认充值”按钮
    def click_confirm_btn(self):
        logging.info('==========click_confirm_btn==========')
        ele = self.get_presence_element(MemberRechargePage.ConfirmRechargeBtn)
        ele.click()

    # 获取“充值成功后打印小票”选择框的状态，通过checked属性进行判断
    def get_print_receipt_status(self):
        logging.info('==========get_print_receipt_status==========')
        ele = self.get_presence_element(MemberRechargePage.PrintReceiptCheckBox)
        return ele.get_attribute('checked')

    # 点击“充值成功后打印小票”选择框
    def click_print_receipt_checkbox(self):
        logging.info('==========click_print_receipt_checkbox==========')
        ele = self.get_presence_element(MemberRechargePage.PrintReceiptCheckBox)
        ele.click()

class CouponOpn(BasePage):
    """
        优惠券页面元素操作
    """
    # 点击“不可用券”按钮
    def click_unavailable_coupon_btn(self):
        logging.info('==========click_unavailable_coupon_btn==========')
        ele = self.get_presence_element(CouponPage.UnavailableCouponBtn)
        ele.click()

class NotAvailableCouponOpn(BasePage):
    """
        不可用优惠券页面元素定位
    """
    # 获取“未生效优惠券”视图框列表的大小，并返回视图框左上角和右下角的坐标值
    def get_not_available_coupon_view_size(self):
        """
            :return: 视图框左上角x轴的值、视图框左上角y轴的值、视图框右下角x轴的值、视图框右下角y轴的值
        """
        logging.info('==========get_not_available_coupon_view_size==========')
        ele = self.get_presence_element(NotAvailableCouponPage.UnavailableCouponView)
        ele_bounds = ele.get_attribute('bounds')

        # 使用正则表达式提取两个坐标对
        matches = re.findall(r'\[(\d+),(\d+)\]', ele_bounds)
        top_left_x, top_left_y = int(matches[0][0]), int(matches[0][1])  # 第一个坐标对
        lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])  # 第二个坐标对

        return top_left_x, top_left_y, lower_right_x, lower_right_y

    # 获取当前显示在“未生效优惠券”视图框中，优惠券号码元素列表
    def get_not_available_coupon_number_list(self):
        logging.info('==========get_not_available_coupon_number_list==========')
        eles = self.get_elements(NotAvailableCouponPage.UnavailableCouponNum)
        return eles

class PointExchangeOpn(BasePage):
    """
        积分兑换页面元素相关操作
    """

    # 获取“积分兑换商品”列表元素
    def get_points_exchange_list(self):
        logging.info('==========get_points_exchange_list==========')
        eles = self.get_elements(PointExchangePage.PointsExchangeViewElem)
        return eles

    # 点击“积分兑换商品”列表中，指定序号的元素
    def click_points_exchange_item(self, item_no):
        logging.info('==========click_points_exchange_item==========')
        eles = self.get_points_exchange_list()
        eles[item_no].click()

    # 获取“积分兑换商品”列表中，指定序号元素的积分值
    def get_points_exchange_item_points(self, item_no):
        logging.info('==========get_points_exchange_item_points==========')
        eles = self.get_points_exchange_list()
        ele = self.get_presence_element(locator=PointExchangePage.PointsExchangeItemPoints, element=eles[item_no])
        return ele.get_attribute("text")

    # 获取"积分兑换商品"列表中,指定序号元素的品名
    def get_points_exchange_item_name(self, item_no):
        logging.info('==========get_points_exchange_item_name==========')
        eles = self.get_elements(PointExchangePage.PointsExchangeItemNames)
        return eles[item_no].get_attribute("text")

    # 点击“积分兑换”按钮
    def click_points_exchange_btn(self):
        logging.info('==========click_points_exchange_btn==========')
        ele = self.get_presence_element(PointExchangePage.ExchangeBtn)
        ele.click()

    # 获取“积分兑换商品”视图大小，并返回视图框左上角和右下角的坐标值
    def get_points_exchange_view_size(self):
        """
            :return: 视图框左上角x轴的值、视图框左上角y轴的值、视图框右下角x轴的值、视图框右下角y轴的值
        """
        logging.info('==========get_points_exchange_view_size==========')
        ele = self.get_presence_element(PointExchangePage.PointsExchangeView)
        ele_bounds = ele.get_attribute('bounds')

        # 使用正则表达式提取两个坐标对
        matches = re.findall(r'\[(\d+),(\d+)\]', ele_bounds)
        top_left_x, top_left_y = int(matches[0][0]), int(matches[0][1])  # 第一个坐标对
        lower_right_x, lower_right_y = int(matches[1][0]), int(matches[1][1])  # 第二个坐标对
        return top_left_x, top_left_y, lower_right_x, lower_right_y

    # 搜索框发送指定数据
    def send_keys_search_input(self, text):
        logging.info('==========send_keys_search_input==========')
        ele = self.get_presence_element(PointExchangePage.SearchInput)
        ele.send_keys(text)

class RechargeDetailOpn(BasePage):
    """
        结账详情页相关元素操作
    """
    # 点击"现金"按钮
    def click_cash_btn(self):
        logging.info('==========click_cash_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.CashBtn)
        ele.click()

    # 点击"储值卡"按钮
    def click_value_card_btn(self):
        logging.info('==========click_value_card_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.ValueCardBtn)
        ele.click()

    # 点击"银联卡"按钮
    def click_union_card_btn(self):
        logging.info('==========click_union_card_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.UnionPayBtn)
        ele.click()

    # 点击"收款码"按钮
    def click_qr_code_btn(self):
        logging.info('==========click_qr_code_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.QRCodeBtn)
        ele.click()

    # 点击"Zfb支付"按钮
    def click_ali_pay_btn(self):
        logging.info('==========click_ali_pay_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.AliPayBtn)
        ele.click()

    # 点击"预付卡"按钮
    def click_prepaid_card_btn(self):
        logging.info('==========click_prepaid_card_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.PrepaidCardBtn)
        ele.click()

    # 输入数字“1”
    def input_search_input_one(self):
        logging.info('==========input_one==========')
        ele = self.get_presence_element(RechargeDetailPage.OneBtn)
        ele.click()

    # 输入数字“2”
    def input_search_input_two(self):
        logging.info('==========input_two==========')
        ele = self.get_presence_element(RechargeDetailPage.TwoBtn)
        ele.click()

    # 输入数字“3”
    def input_search_input_three(self):
        logging.info('==========input_three==========')
        ele = self.get_presence_element(RechargeDetailPage.ThreeBtn)
        ele.click()

    # 输入数字“4”
    def input_search_input_four(self):
        logging.info('==========input_four==========')
        ele = self.get_presence_element(RechargeDetailPage.FourBtn)
        ele.click()

    # 输入数字“5”
    def input_search_input_five(self):
        logging.info('==========input_five==========')
        ele = self.get_presence_element(RechargeDetailPage.FiveBtn)
        ele.click()

    # 输入数字“6”
    def input_search_input_six(self):
        logging.info('==========input_six==========')
        ele = self.get_presence_element(RechargeDetailPage.SixBtn)
        ele.click()

    # 输入数字“7”
    def input_search_input_seven(self):
        logging.info('==========input_seven==========')
        ele = self.get_presence_element(RechargeDetailPage.SevenBtn)
        ele.click()

    # 输入数字“8”
    def input_search_input_eight(self):
        logging.info('==========input_eight==========')
        ele = self.get_presence_element(RechargeDetailPage.EightBtn)
        ele.click()

    # 输入数字“9”
    def input_search_input_nine(self):
        logging.info('==========input_nine==========')
        ele = self.get_presence_element(RechargeDetailPage.NineBtn)
        ele.click()

    # 输入数字“0”
    def input_search_input_zero(self):
        logging.info('==========input_zero==========')
        ele = self.get_presence_element(RechargeDetailPage.ZeroBtn)
        ele.click()

    # 输入数字“00”
    def input_search_input_zero_zero(self):
        logging.info('==========input_zero_zero==========')
        ele = self.get_presence_element(RechargeDetailPage.ZeroZeroBtn)
        ele.click()

    # 输入数字"."
    def input_search_input_dot(self):
        logging.info('==========input_dot==========')
        ele = self.get_presence_element(RechargeDetailPage.DotBtn)
        ele.click()

    # 点击"删除"按钮
    def click_delete_btn(self):
        logging.info('==========click_delete_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.DeleteBtn)
        ele.click()

    # 点击"确定"按钮
    def click_confirm_btn(self):
        logging.info('==========click_confirm_btn==========')
        ele = self.get_presence_element(RechargeDetailPage.ConfirmBtn)
        ele.click()

    # 获取“应收金额”文本信息
    def get_receivable_amount_text(self):
        logging.info('==========get_receivable_amount_text==========')
        ele = self.get_presence_element(RechargeDetailPage.ReceivableAmountText)
        return ele.text

    # 获取“实收金额”文本信息
    def get_actual_amount_text(self):
        logging.info('==========get_actual_amount_text==========')
        ele = self.get_presence_element(RechargeDetailPage.ActualAmountText)
        return ele.text