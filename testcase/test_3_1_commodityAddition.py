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

@ddt.ddt
class TestCaseInterface(StartEnd):
    """
            1、os.getcwd() 返回当前工作目录（即 Python 进程的当前目录）
            2、os.path.dirname(path) 返回指定路径的父目录
            3、这是字符串 "data"，它表示一个文件夹名称。接下来会把它拼接到路径中
            4、os.path.basename(__file__) 会从这个路径中提取出文件名部分。例如，如果脚本的路径是 /home/user/myproject/test.py，那么 os.path.basename(__file__) 返回的就是 "test.py"
            5、split(".") 将文件名根据 "." 分割成一个列表，[0] 获取文件名的第一部分（去掉扩展名）。比如，"test.py".split(".") 会得到 ["test", "py"]，取 [0] 后，得到 "test"
        """
    file_dir = os.path.join(os.path.dirname(os.getcwd()), "data",
                            os.path.basename(__file__).split(".")[0]) + ".csv"  # 拼接测试数据的路径

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
    def testAddGoods(self, trade_name, selling_price, purchase_price, inventory):
        """
            收银页新增商品
        """
        logging.info("==========test_MessageClear==========")
        # 获取系统权限请求页的文本信息，从而得到需要点击多少次“允许”按钮
        permission_page_text = LoginInPageOpn(self.driver).permission_page_text() # 文本信息类似于“第 1 项权限（共 3 项）”
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
        # e = (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until_not(lambda x: x.find_element(
        #     By.XPATH, "//*[@class='android.widget.Toast']")))
        CashInterfaceOpn(self.driver).wait_toast_disappear()
        time.sleep(15)  # 才进入收银页面时，应用不是全屏，所以需要等待一段时间，才能定位到元素。否则，定位到的元素位置是偏移的，进行不了任何操作

        # 点击“チキン”按钮
        # eles1 = (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_elements(
        #     By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/category_gv']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/root_rl']")))
        # eles1[3].click()

        # 获取“チキン”分类的文本信息
        # text_ele = (WebDriverWait(eles1[3], 10, 0.5, None)
        #         .until(lambda x: x.find_element(
        #     By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv']")))
        # print(text_ele.get_attribute("text"))
        # time.sleep(2)
        category_name = CashInterfaceOpn(self.driver).click_category_btn(3)

        # 在“チキン”分类下，点击“新增商品”按钮（即列表的最后一个元素）
        # eles2 = (WebDriverWait(self.driver, 10, 0.5, None)
        #         .until(lambda x: x.find_elements(
        #     By.XPATH,
        #     "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/product_rv']/*[@class='android.widget.RelativeLayout']")))
        # eles2[-1].click()
        CashInterfaceOpn(self.driver).click_add_product_btn()

        barCodes = []
        for i in range(2):
            # 在“新增商品”页面，点击“生成”按钮，生成随机条码
            # (WebDriverWait(self.driver, 10, 0.5, None)
            #  .until(lambda x: x.find_element(
            #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/generate_barcode"))
            #  .click())
            NewProductPageOpn(self.driver).click_generate_btn()

            # 获取生成的条码值
            # barCode = (WebDriverWait(self.driver, 10, 0.5, None)
            #         .until(lambda x: x.find_element(
            #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/number_et"))
            #         .get_attribute("text"))
            barCode = NewProductPageOpn(self.driver).get_barcode_input_text()
            barCodes.append(barCode)

        # 判断两次生成的条码值是否相等，若相等则报错
        self.assertNotEqual(barCodes[0], barCodes[1])

        # 获取“品名”输入框，输入商品名
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/name_et"))
        #  .send_keys(trade_name))
        NewProductPageOpn(self.driver).input_product_name(trade_name)

        # 获取“库存”输入框，输入库存
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/stock_et"))
        #  .send_keys(inventory))
        NewProductPageOpn(self.driver).input_stock(inventory)

        # 获取“售价”输入框，输入售价
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/price_et"))
        #  .send_keys(selling_price))
        NewProductPageOpn(self.driver).input_price(selling_price)

        # 获取“进价”输入框，输入进价
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/buy_price_et"))
        #  .send_keys(purchase_price))
        NewProductPageOpn(self.driver).input_purchase_price(purchase_price)

        # 点击分类下拉框
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/category_tv"))
        #  .click())
        NewProductPageOpn(self.driver).click_category_dropdown()

        # 点击搜索栏，并输入“チキン”
        # search_btn = (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/input_et")))
        # search_btn.send_keys("チキン")
        NewProductPageOpn(self.driver).input_category_search_input("チキン")

        # 点击第一个搜索结果
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x : x.find_element(By.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/ctg_rv']/*[@class='android.widget.LinearLayout']"))
        #  .click())
        NewProductPageOpn(self.driver).click_search_result()

         # 点击确认按钮，确定所选分类
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn"))
        #  .click())
        NewProductPageOpn(self.driver).click_category_save_btn()

         # 点击“保存”按钮，保存新增商品
        # (WebDriverWait(self.driver, 10, 0.5, None)
        #  .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/save_ll"))
        #  .click())
        NewProductPageOpn(self.driver).click_save_btn()

        # 进入新增商品的对应分类
        # category_eles = (WebDriverWait(self.driver, 10, 0.5, None)
        #          .until(lambda x: x.find_elements(
        #     By.XPATH,
        #     "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/category_gv']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/root_rl']")))
        # category_eles[3].click()
        _ = CashInterfaceOpn(self.driver).click_category_btn(3)

        # 新增商品被添加在最后，获取倒数第二个元素
        # eles3 = (WebDriverWait(self.driver, 10, 0.5, None)
        #          .until(lambda x: x.find_elements(
        #     By.XPATH,
        #     "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/product_rv']/*[@class='android.widget.RelativeLayout']")))
        # eles3[-2].click()
        #
        # new_trade_name = (WebDriverWait(eles3[-2], 10, 0.5, None)
        #            .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv"))
        #            .get_attribute("text"))  # 获取新增商品名
        # new_selling_price = (WebDriverWait(eles3[-2], 10, 0.5, None)
        #            .until(lambda x: x.find_element(
        #     By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/price_et"))
        #            .get_attribute("text"))
        new_trade_name, new_selling_price = CashInterfaceOpn(self.driver).get_new_product_name_price()
        new_selling_price = new_selling_price.split('￥')[-1] # 去掉符号后提取数字

        # 判断新增商品的名称和价格是否正确
        self.assertEqual(selling_price, new_selling_price)
        self.assertEqual(trade_name, new_trade_name)

if __name__ == '__main__':
    unittest.main()