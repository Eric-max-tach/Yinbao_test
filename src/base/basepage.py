import time, os
import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SCREENSHOT_DIR = '../sreenshot/'    # 截图保存目录，相对路径
cur_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))   # 获取当前时间
file_name = '{}.png'.format(cur_time)

class BasePage(object):
    # 构造一个基础类
    def __init__(self, driver):
        self.driver = driver

    def get_presence_element(self, locator, timeout = 10, element = None):
        """
            获取存在，但不一定可见的元素，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :param element: 通过所提供的元素查找该元素的子元素
            :return: 返回存在，但不一定可见的元素
        """
        try:
            if element == None:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            else:
                return WebDriverWait(element, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))

    def get_presence_element_need_exception(self, locator, timeout = 10, element = None, need_screenshot = 1):
        """
            该方法会返回异常信息
            获取存在，但不一定可见的元素，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :param element: 通过所提供的元素查找该元素的子元素
            :param need_screenshot: 判断是否出现异常时需要截图，默认值为1，表示需要异常截图。0表示不需要异常截图
            :return: 返回存在，但不一定可见的元素
        """
        try:
            if element == None:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            else:
                return WebDriverWait(element, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            if need_screenshot == 1:
                # 截图、日志
                self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
                logging.error("元素定位失败：{}".format(file_name))
            raise e

    def get_visible_element(self, locator, timeout = 10):
        """
            获取可见元素，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :return: 返回可见元素
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))

    def get_clickable_element(self, locator, timeout = 10):
        """
            获取可见，同时可点击的元素，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :return: 返回可见，同时可点击的元素
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))

    def get_presence_until_not_element(self, locator, timeout = 10):
        """
            添加的是until not显式等待方法，在规定时间内，代码每隔一段时间就调用一次该方法，直到`until_not`的返回值为False
            获取存在，但不一定可见的元素，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :return: 返回存在，但不一定可见的元素
        """
        try:
            return WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))

    def get_elements(self, locator, timeout = 10):
        """
            获取一组存在的元素，但不一定可见，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :return: 返回一组存在的元素
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))

    def swipe_screen(self, start_x, start_y, end_x, end_y, duration=None):
        """
            屏幕滑动
            :param start_x: 滑动起始点横坐标
            :param start_y: 滑动起始点纵坐标
            :param end_x: 滑动结束点横坐标
            :param end_y: 滑动结束点纵坐标
            :param duration: 滑动持续时间，单位为s，即滑动屏幕的时候是否需要惯性，默认为空值即有惯性，若值越大则不存在惯性，一般设置为0.5s
            :return:

            注意：上述位置信息指的是百分比，例如x轴的二分之一处，传入的值则为0.5
        """
        # 获取屏幕窗口的大小
        size_dict = self.driver.get_window_size()
        actions = ActionChains(self.driver)
        # 输入源设备列表为空
        actions.w3c_actions.devices = []
        # =============从屏幕指定位置滑动到另一个指定位置===========
        # 添加新的输入源到设备中
        new_input = actions.w3c_actions.add_pointer_input("touch", "finger1")
        # 指针移动到x轴的0.1875的位置，y轴的0.4741的位置
        new_input.create_pointer_move(x=size_dict['width'] * start_x, y=size_dict['height'] * start_y)
        # 按住鼠标左键
        new_input.create_pointer_down()
        # 向上滑动
        new_input.create_pointer_move(x=size_dict["width"] * end_x, y=size_dict["height"] * end_y)
        # # 暂停duration秒
        # if duration is not None:
        #     new_input.create_pause(duration)
        # 释放鼠标左键
        new_input.create_pointer_up(MouseButton.LEFT)
        # 执行动作
        actions.perform()

    def click_screen(self, start_x, start_y, duration):
        """
            屏幕点击
            :param start_x: 点击横坐标
            :param start_y: 点击纵坐标
            :param duration: 点击持续时间，单位为s
            :return:
        """
        # 获取屏幕窗口的大小
        size_dict = self.driver.get_window_size()
        actions = ActionChains(self.driver)
        # 输入源设备列表为空
        actions.w3c_actions.devices = []
        # =============点击屏幕指定位置，“库存预警”按钮位于屏幕的（0.1875, 0.4741）的位置===========
        # 添加新的输入源到设备中
        new_input = actions.w3c_actions.add_pointer_input("touch", "finger1")
        # 指针移动到x轴的0.1875的位置，y轴的0.4741的位置
        new_input.create_pointer_move(x=size_dict['width'] * start_x, y=size_dict['height'] * start_y)
        # 按住鼠标左键
        new_input.create_pointer_down()
        # 等待1秒
        new_input.create_pause(duration)
        # 释放鼠标左键
        new_input.create_pointer_up(MouseButton.LEFT)
        # 执行动作
        actions.perform()