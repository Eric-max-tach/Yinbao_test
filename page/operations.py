from selenium.common import NoSuchElementException, TimeoutException

from page.locators import *
from base.basepage import *
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
logging = logging.getLogger()

class LoginInPageOpn(BasePage):
    """
        登录页元素操作
    """
    # 在系统权限请求页面中，获取current_page_text中的文本信息，即“第 1 项权限（共 3 项）”
    def permission_page_text(self):
        logging.info('==========permission_page_text==========')
        # 获取文本信息元素的文本内容，即获取内容“第 1 项权限（共 3 项）”
        ele = self.get_presence_element(LoginInPageLocators.PermissionPageText)
        return ele.get_attribute("text")

    # 在系统权限请求页面中，点击“同意”按钮
    def click_permission_allow_btn(self):
        logging.info('==========click_permission_allow_btn==========')
        # 查找点击元素
        # ele = self.driver.find_element(*LoginInPageLocators.PermissionAllowBtn)
        ele = self.get_clickable_element(LoginInPageLocators.PermissionAllowBtn)    # 替换为添加了显示等待的元素定位方法
        ele.click()


    # 账号输入框输入账号名
    def input_account(self, username):
        logging.info('==========input_account==========')
        # ele = self.driver.find_element(*LoginInPageLocators.AccountInput)
        ele = self.get_visible_element(LoginInPageLocators.AccountInput)    # 替换为添加了显示等待的元素定位方法
        ele.send_keys(username)

    # 密码输入框输入密码
    def input_password(self, password):
        logging.info('==========input_password==========')
        # ele = self.driver.find_element(*LoginInPageLocators.PasswordInput)
        ele = self.get_visible_element(LoginInPageLocators.PasswordInput)   # 替换为添加了显示等待的元素定位方法
        ele.send_keys(password)

    # 在输入账号和密码后点击登录按钮
    def click_login_btn(self):
        logging.info('==========click_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.LoginBtn)
        ele = self.get_clickable_element(LoginInPageLocators.LoginBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 获取Toast文本信息
    def get_toast_text(self) -> str:
        logging.info('==========get_toast_text==========')
        # ele = self.driver.find_element(*LoginInPageLocators.Toast)
        ele = self.get_presence_element(LoginInPageLocators.Toast)  # 替换为添加了显示等待的元素定位方法
        return ele.text

    # 体验账号按钮点击
    def try_login_btn(self):
        logging.info('==========try_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.TryAccountBtn)
        ele = self.get_clickable_element(LoginInPageLocators.TryAccountBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 免费注册按钮点击
    def free_login_btn(self):
        logging.info('==========free_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.FreeRegistBtn)
        ele = self.get_clickable_element(LoginInPageLocators.FreeRegistBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 联系客服按钮点击
    def contact_service_btn(self):
        logging.info('==========contact_service_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.ContactServiceBtn)
        ele = self.get_clickable_element(LoginInPageLocators.ContactServiceBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 账号+工号登录按钮点击
    def account_cashier_login_btn(self):
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
        logging.info('==========retail_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.RetailBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.RetailBtn)   # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 餐饮行业按钮点击
    def food_industry_btn(self):
        logging.info('==========food_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.FoodBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FoodBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 服装鞋帽按钮点击
    def clothes_shoes_industry_btn(self):
        logging.info('==========clothes_shoes_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.ClothesShoesBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.ClothesShoesBtn) # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 生活服务按钮点击
    def service_industry_btn(self):
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

class MemberRechargeOpn(BasePage):
    """
        会员充值页面元素定位
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