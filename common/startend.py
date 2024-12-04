import os
import time
import traceback
import unittest
from appium import webdriver
from base.parse_yaml import parse_yaml
import logging
import logging.config

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
SCREENSHOT_DIR = '../screenshot/'

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("=========setUp===========")
        desired_caps = parse_yaml("../config/my_yaml.yml", "yinbao")

        self.driver = webdriver.Remote(parse_yaml("../config/my_yaml.yml", "yinbao", "remoteurl"), desired_caps)

        # # 等待页面加载，可以根据实际情况调整等待时间
        # self.driver.implicitly_wait(15)

        """
            因为StartEnd类继承自unittest.TestCase类。而unittest.TestCase类中存在一个属性failureException。
            测试用例类继承自StartEnd类，所以测试用例类也存在failureException属性。
            当测试用例调用unittest提供的断言方法出现断言失败时，实际上调用的是测试用例类的self.failureException属性。
            而这个属性调用了重写的AssertionError（python提供的异常类），从而获得了断言失败截图的功能
        """
        self.failureException = self.failure_monitor()

    def failure_monitor(self):
        """
        截图，保存在screenshot目录下，命名以当前时间戳命名
        :return:
        """
        test_case = self  # 将self赋值给test_case，以便让AssertionErrorPlus内部类可以调用外部类的方法

        class AssertionErrorPlus(AssertionError):
            def __init__(self, msg):
                try:
                    # cur_method = test_case._testMethodName  # 获取当前 test() 方法名
                    cur_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) # 获取当前时间戳
                    # file_name = '{}_{}.png'.format(cur_method, cur_time)
                    file_name = '{}.png'.format(cur_time)
                    test_case.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name))    # 截图生成 png 文件
                    logging.info("失败截图已保存到：{}".format(file_name))
                except BaseException:
                    logging.error("截图失败：{}".format(traceback.format_exc()))     # logging.error("截图失败：{}".format(traceback.format_exc()))
                super(AssertionErrorPlus, self).__init__(msg)   # 调用父类 AssertionError 的构造方法，将错误消息 msg 传递给父类

        return AssertionErrorPlus # 返回自定义的异常类，这意味着你可以在其他地方使用 failure_monitor 来动态生成一个自定义异常，并且通过 raise 语句抛出它


    def tearDown(self):
        logging.info("========tearDown=========")
        time.sleep(2)
        self.driver.quit()