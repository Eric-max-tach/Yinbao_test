## 一、unittest框架结构

### 1、unittest框架的4个重要概念

#### 1.1 test fixture（测试固件）

在测试之前或者测试之后需要做的一些工作，例如打开浏览器，连接数据库等。unittest中常用的固件有`setUp`、`tearDown`、`setUpClass`、`tearDownClass`。

#### 1.2 test case（测试用例）

即测试用例，是用来执行测试的最小单元。unittest中提供了一个名为`TestCase`的基础类，可以用来创建测试用例。在unittest中测试用例的方法必须以test开头，并且执行顺序会按照方法名的ASCII值排序。

#### 1.3 test suite（测试套件）

作用是将多个测试用例放在一起，执行test suite就可以将其中的用例全部执行

#### 1.4 test runner（测试运行器）

用来执行测试用例，并返回测试用例执行结果。某些test runner还可以通过图形、表格、文本等方式把测试结果形象地展示出来。

### 2、unittest脚本示例

```python
import unittest

class TestStorm(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_first(self):
        self.assertEqual('storm', 'storm')

if __name__=='__main__':
    unittest.main()
```

**注意点**

> 1、导包 import unittest
>
> 2、新建测试类并继承 unittest.TestCase
>
> 3、测试用例名称必须以`test_`开头

## 二、测试固件

unittest框架一共包含4种测试固件：

- `setUp()`：在每个测试用例运行前运行，用于完成测试前的初始化工作
- `tearDown()`：在每个测试用例结束后运行，用于完成测试后的清理工作
- `setUpClass()`：在所有测试用例运行前运行，用于完成单元测试的前期准备工作，必须使用`@classmethod`装饰器进行装饰，在`setUp()`方法之前执行，整个测试过程只执行一次
- `tearDownClass()`：在所有测试用例结束后运行，用于完成单元测试的后期处理工作，必须使用`@classmethod`装饰器进行修饰，在`tearDown()`方法之后执行，整个测试过程只执行一次

```python
import unittest

class TestStorm(unittest.TestCase):
    @classmethod
    # 在所有测试用例运行前执行一次
    def setUpClass(cls):
        print("============setUpClass===============")
        return super().setUpClass()

    def setUp(self):    # 在每个测试用例执行前执行一次
        print('setUp')

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        print('tearDown')

    @classmethod
    # 在所有测试用例运行结束后执行一次
    def tearDownClass(cls):
        print("============tearDownClass===============")
        return super().tearDownClass()

    def test_first(self):
        print("first")
        self.assertEqual('storm', 'storm')

    def test_second(self):
        print("second")
        self.assertEqual('storm', 'storm')

if __name__=='__main__':
    unittest.main()	# 会收集当前文件中所有的测试用例并执行
```

**执行结果**

```python
====================== test session starts ===================
collecting ... collected 2 items

unittest1.py::TestStorm::test_first ============setUpClass===============
PASSED                               [ 50%]
setUp
first
tearDown

unittest1.py::TestStorm::test_second PASSED                              [100%]
setUp
second
tearDown
============tearDownClass===============


========================= 2 passed in 0.02s =======================
```

## 三、执行测试用例

### 1、通过class构造测试集合

**示例1**

```python
import unittest

class TestFirst(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_one(self):
        print("1")
        self.assertEqual('storm', 'storm')

    def test_two(self):
        print("2")
        self.assertEqual('storm', 'storm')

class TestSecond(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_three(self):
        print("3")
        self.assertEqual('storm', 'storm')

    def test_four(self):
        print("4")
        self.assertEqual('storm', 'storm')

if __name__=='__main__':
    unittest.main() # 会收集当前文件中所有的测试用例并执行
```

**运行结果**

```python
1
2
4
3
```



**示例2**

除了`main()`方法外，还可以通过`unittest.TestLoader().loadTestFromTestCase()`加载某个class下的所有用例

```python
import unittest
from unittest2 import TestFirst

if __name__ == '__main__':
    testCase = unittest.TestLoader().loadTestsFromTestCase(TestFirst)
    suite = unittest.TestSuite([testCase])
    unittest.TextTestRunner().run(suite)
```

**运行结果**

```python
1
2
```

**注意点**

如果在测试类文件里使用上述方法去加载测试用例，那么还是会执行所有的测试用例

```python
import unittest

class TestFirst(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_one(self):
        print("1")
        self.assertEqual('storm', 'storm')

    def test_two(self):
        print("2")
        self.assertEqual('storm', 'storm')

class TestSecond(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_three(self):
        print("3")
        self.assertEqual('storm', 'storm')

    def test_four(self):
        print("4")
        self.assertEqual('storm', 'storm')

if __name__=='__main__':
    testCase = unittest.TestLoader().loadTestsFromTestCase(TestSecond)
    suite = unittest.TestSuite([testCase])
    unittest.TextTestRunner().run(suite)
```

**执行结果**

```python
1
2
4
3
```

### 2、通过addTest()构建测试集合

可以通过`addTest()`将某个class下面的测试用例添加到集合，然后运行测试集合

```python
import unittest
from unittest2 import TestFirst, TestSecond

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFirst("test_one"))
    suite.addTest(TestSecond("test_three"))
    unittest.TextTestRunner().run(suite)
```

**执行结果**

```python
1
3
```

### 3、通过discover()构建测试集合

可以通过`unittest.TestLoader().discover('.')`在指定目录寻找符合条件的测试用例，并用他们组成测试集合。

```python
import unittest

if __name__ == '__main__':
    testSuite = unittest.TestLoader().discover("")
    unittest.TextTestRunner().run(testSuite)
```

`discover()`中传递的是“.”，代表当前用例文件所在目录。执行该测试用例时，就会在该文件所在目录中寻找所有符合条件的测试用例。

## 四、用例执行顺序

执行测试用例的顺序是按照方法名和函数名的ASCII值排序来决定的。因此，在上述文件中，包含两个class，类名分别为“TestFirst”和“TestSecond”，前四个字符相同，从第五个字符开始不同，而“F”排在“S”前面，因此TestFirst类先执行。而TestFirst类中有两个测试用例，分别为“test_one”和“test_two”，按照ASCII值排序，“test_one”比“test_two”先执行。

如何使测试用例按照指定的顺序执行测试有以下两种方法：

### 1、将用例按照顺序添加到集合

```python
import unittest
from unittest2 import TestFirst, TestSecond

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestFirst("test_one"))
    suite.addTest(TestFirst("test_two"))
    suite.addTest(TestSecond("test_three"))
    suite.addTest(TestSecond("test_four"))
```

**执行结果**

```python
1
2
3
4
```

### 2、调整测试用例名称

在“test”和“用例名”中间加上数字

```python
import unittest

class TestFirst(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_001_one(self):
        print("1")
        self.assertEqual('storm', 'storm')

    def test_002_two(self):
        print("2")
        self.assertEqual('storm', 'storm')

class TestSecond(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_003_three(self):
        print("3")
        self.assertEqual('storm', 'storm')

    def test_004_four(self):
        print("4")
        self.assertEqual('storm', 'storm')

if __name__=='__main__':
    unittest.main() # 会收集当前文件中所有的测试用例并执行
```

## 五、内置装饰器

**应用场景**

在某些场景下，测试用例不需要执行，但又舍不得删除测试用例

### 1、无条件跳过装饰器

```python
import unittest

"""
    @unittest.skip("skip info")，无条件跳过
"""
class MyTest(unittest.TestCase):
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    @unittest.skip("skip info")
    def test_aaa(self):
        print("test_aaa")

    def test_ddd(self):
        print("test_ddd")

    def test_bbb(self):
        print("test_bbb")

    def test_ccc(self):
        print("test_ccc")

if __name__=='__main__':
    unittest.main()
```

**执行结果**

```python
Skipped: skip info
bbb
ccc
ddd
```

### 2、满足条件跳过装饰器

```python
import unittest
import sys

"""
    @unittest.skipIf(a==6, "skip info")，满足条件跳过
"""
class MyTest(unittest.TestCase):
    a = 6
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_aaa(self):
        print("test_aaa")

    def test_ddd(self):
        print("test_ddd")

    @unittest.skipIf(a==6, "skip info")
    def test_bbb(self):
        print("test_bbb")

    def test_ccc(self):
        print("test_ccc")

if __name__=='__main__':
    unittest.main()
```

**执行结果**

```python
aaa
Skipped: skip info
ccc
ddd
```

### 3、不满足条件跳过装饰器

```python
import unittest
import sys

"""
    @unittest.skipUnless(a==5, "skip info")，满足条件跳过
"""
class MyTest(unittest.TestCase):
    a = 6
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_aaa(self):
        print("test_aaa")

    def test_ddd(self):
        print("test_ddd")

    @unittest.skipUnless(a==5, "skip info")
    def test_bbb(self):
        print("test_bbb")

    def test_ccc(self):
        print("test_ccc")

if __name__=='__main__':
    unittest.main()
```

**执行结果**

```python
aaa
Skipped: skip info
ccc
ddd
```

## 六、命令行执行测试

unittest框架支持以命令行模式运行测试模块、类、单独的测试方法。通过命令行模式，可以在命令行传入任何模块明、有效的测试类和测试方法参数列表。

支持以下三种方法：

**1、通过命令直接运行整个测试文件**

```shell
# python -m unittest -v 文件名
python -m unittest -v unittest_skip.py
```

**2、通过命令执行测试文件中的某个测试类**

```shell
# python -m unittest -v 文件名.类名
python -m unittest -v unittest_skip.MyTest
```

**3、通过命令执行某个文件中某个类下的某个测试用例**

```shell
# python -m unittest -v 文件名.类名.方法名
python -m unittest -v unittest_skip.MyTest.test_bbb
```

**注意点**

> -munittest参数，代表以unittest框架执行用例
>
> -v参数，代表输出结果为详细模式

## 七、批量执行测试文件

在“Storm_12_1”包下创建三个文件“test_001.py”、“test_002.py”、“run.py”

```python
"""
	test_001.py
"""
import unittest

class MyTest(unittest.TestCase):
    a = 6
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_aaa(self):
        print("test_aaa")

    def test_bbb(self):
        print("test_bbb")

if __name__=='__main__':
    unittest.main()
```

```python
"""
	test_002.py
"""
import unittest

class MyTest(unittest.TestCase):
    a = 6
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_ddd(self):
        print("test_ddd")

    def test_ccc(self):
        print("test_ccc")

if __name__=='__main__':
    unittest.main()
```

```python
"""
	run.py
"""
import unittest

if __name__=='__main__':
    testSuite = unittest.TestLoader().discover(".")
    unittest.TextTestRunner(verbosity=2).run(testSuite)
```

**分析**

> 1、`testSuite = unittest.TestLoader().discover(".")`表示`discover(".")`方法训在指定目录下符合条件的测试用例；
>
> 2、“.”代表当前目录；
>
> 3、以“test”开头的测试文件名对应的测试用例为符合条件的测试用例；

## 八、测试断言

unittest框架中集成了很多断言方法

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("TearDown")

    def test_001(self):
        j = 5
        self.assertEqual(j + 1, 6)  # 判断相等
        self.assertNotEqual(j, 6)   # 判断不相等

    def test_002(self):
        j = True
        f = False
        self.assertTrue(j)  # 判断j为True
        self.assertFalse(f)  # 判断f为False

    def test_003(self):
        j = "storm"
        self.assertIs(j, "storm")   # 判断j为"storm"
        self.assertIsNot(j, "Storm")    # 判断j不为"Storm"，区分大小写

    def test_004(self):
        j = "storm"
        self.assertIn(j, "storms")   # 判断j在"storms"中
        self.assertNotIn(j, "xxx")  # 判断j不在"xxx"中

    def test_005(self):
        j = None
        t = "storm"
        self.assertIsNone(j)    # 判断j为None
        self.assertIsNotNone(t) # 判断t不为None

    def test_006(self):
        j = "storm"
        self.assertIsInstance(j, str)   # 判断j为字符串
        self.assertNotIsInstance(j, int) # 判断j不为整数

if __name__=="__main__":
    unittest.main()
```

## 九、HTMLTestRunner测试报告

使用 HtmlTestRunner 类替代 TestRunner 类，来批量执行测试用例。

安装 HtmlTestRunner 包

```shell
pip install html-testRunner
```

创建“storm_12_10”包，新建文件“test_001.py”、“test_002.py”、“run.py”

```python
"""
	test_001.py
"""
import unittest

class MyTest(unittest.TestCase):
    a = 6
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_aaa(self):
        print("test_aaa")

    def test_bbb(self):
        print("test_bbb")

if __name__=='__main__':
    unittest.main()
```

```python
"""
	test_002.py
"""
import unittest

class MyTest(unittest.TestCase):
    a = 6
    def setUp(self):    # 在每个测试用例执行前执行一次
        pass

    def tearDown(self): # 在每个测试用例执行结束后执行一次
        pass

    def test_ddd(self):
        print("test_ddd")

    def test_ccc(self):
        print("test_ccc")

if __name__=='__main__':
    unittest.main()
```

```python
"""
	run.py
"""

import unittest
import HtmlTestRunner
import time

if __name__=='__main__':
    # 查找当前目录的测试用例文件
    testSuite = unittest.TestLoader().discover(".")
    # 定义文件名，文件名由年、月、日、时、分、秒构成
    filename = ".\\report\\Storm_{}".format(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))

    # 通过HtmlTestRunner执行测试用例，并生成报告
    HtmlTestRunner.HTMLTestRunner(output=filename).run(testSuite)
```

**执行结果**

![image-20241127160222465](../images/image-20241127160222465.png)

**如何将unittest和appium结合**

> 1、将desired_caps、初始化driver都放大setUp()中，作为初始化内容
>
> 2、将退出driver放到tearDown()中，作为测试后的收尾动作
>
> 3、使用unittest内置的断言assert来进行用例检查
>
> 4、最后新建run.py文件，用于生成测试报告

## 十、unittest参数化

**应用场景**

例如编写一条测试用例：打开银豹app，然后在“账号”和“密码”文本框分别输入“admin_001”和“password_001”，然后再点击登录按钮。如果此时，我还想输入其它的账号和密码，我就得再写一次测试用例，除了参数和第一个测试用例不同之外，其余代码部分大量重合，导致代码冗余。

因此，我们需要借助第三方插件将数据与脚本代码抽离出来。

### 1、unittest+DDT（Data Driver Test）

**步骤**

> 1、安装ddt，`pip install ddt`
>
> 2、在代码头部导入ddt模块，`import ddt`
>
> 3、在测试类名上声明使用`@ddt.ddt`
>
> 4、在测试方法上使用`@ddt.data([data11, data12], [data21, data22])`来定义数据
>
> 5、在`@ddt.data()`下方使用`@ddt.unpack`对数据进行解析
>
> 6、`@ddt.data()`中定义数据的个数和顺序必须与测试方法的形参一一对应

```python
import time
from time import sleep

from appium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import unittest
import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.pospal.www.pospal_pos_android_new.pospal'
        desired_caps['appActivity'] = 'cn.pospal.www.pospal_pos_android_new.activity.main.MainActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        # 等待页面加载，可以根据实际情况调整等待时间
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    """
        1、@ddt.data()，圆括号中可以传递列表或元组
        2、这里传递的是两个列表，代表两个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    @ddt.data(["admin_001", "password_001"], ["admin_002", "password_002"])
    @ddt.unpack
    def test_login(self, username, password):
        def click_until_disappear(driver, element_id, timeout=10, interval=0.5):
            try:
                WebDriverWait(driver, timeout, interval).until_not(
                    lambda x: click_if_exists(x, element_id)
                )
                print(f"Element with ID '{element_id}' has disappeared.")
            except TimeoutException:
                print(f"Element with ID '{element_id}' did not disappear within {timeout} seconds.")

        def click_if_exists(driver, element_id):
            try:
                # 查找并点击元素
                element = driver.find_element(By.ID, element_id)
                element.click()
                return True  # 如果点击成功，返回 True 表示元素仍存在
            except NoSuchElementException:
                return False  # 如果元素不存在，返回 False 表示它已经消失

        # 目标是不断点击“允许”按钮（permission_allow_button），直到它被页面移除：
        click_until_disappear(self.driver, "com.android.packageinstaller:id/permission_allow_button", timeout=5,
                              interval=0.5)

        # 检查“用户名”输入框元素是否存在在DOM中，但元素不一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.presence_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_tv")))
            ele.send_keys(username)
        except Exception as e:
            raise e
        finally:
            sleep(2)

        # 检查“密码”输入框元素是否存在在DOM中，且元素一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.visibility_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/password_tv")))
            ele.send_keys(password)
        except Exception as e:
            raise e
        finally:
            sleep(2)

        # 检查“登录”按钮元素是否可见并且可以单击
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.element_to_be_clickable((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn")))
            ele.click()
        except Exception as e:
            raise e
        finally:
            sleep(2)

        # 获取 Toast 的文本信息
        text = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text

        # 判断 Toast 的文本信息时候匹配
        self.assertIs(text, "输入的账号密码错误")

        # 截图
        self.driver.get_screenshot_as_file(r"homepage.png")
if __name__ == '__main__':
    unittest.main()
```

### 2、unittest+parameterized

**步骤**

> 1、安装ddt，`pip install parameterized`
>
> 2、在代码头部导入ddt模块，`from parameterized import parameterized`
>
> 3、在测试方法上使用`@parameterized.expand([(data11, data12), (data21, data22)])`来定义数据
>
> 4、`@parameterized.expand()`中定义数据的个数和顺序必须与测试方法的形参一一对应

```python
import unittest

from parameterized import parameterized
from appium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin(unittest.TestCase):
    def setUp(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.pospal.www.pospal_pos_android_new.pospal'
        desired_caps['appActivity'] = 'cn.pospal.www.pospal_pos_android_new.activity.main.MainActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        # 等待页面加载，可以根据实际情况调整等待时间
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    """
        1、@parameterized.expand()，元括号中传递列表
        2、列表中存放的是元组，每一个元组代表一个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    @parameterized.expand([("admin_001", "password_001"), ("admin_002", "password_002")])
    def test_login(self, username, password):
        def click_until_disappear(driver, element_id, timeout=10, interval=0.5):
            try:
                WebDriverWait(driver, timeout, interval).until_not(
                    lambda x: click_if_exists(x, element_id)
                )
                print(f"Element with ID '{element_id}' has disappeared.")
            except TimeoutException:
                print(f"Element with ID '{element_id}' did not disappear within {timeout} seconds.")

        def click_if_exists(driver, element_id):
            try:
                # 查找并点击元素
                element = driver.find_element(By.ID, element_id)
                element.click()
                return True  # 如果点击成功，返回 True 表示元素仍存在
            except NoSuchElementException:
                return False  # 如果元素不存在，返回 False 表示它已经消失

        # 目标是不断点击“允许”按钮（permission_allow_button），直到它被页面移除：
        click_until_disappear(self.driver, "com.android.packageinstaller:id/permission_allow_button", timeout=5,
                              interval=0.5)

        # 检查“用户名”输入框元素是否存在在DOM中，但元素不一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.presence_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_tv")))
            ele.send_keys(username)
        except Exception as e:
            raise e

        # 检查“密码”输入框元素是否存在在DOM中，且元素一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.visibility_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/password_tv")))
            ele.send_keys(password)
        except Exception as e:
            raise e

        # 检查“登录”按钮元素是否可见并且可以单击
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.element_to_be_clickable((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn")))
            ele.click()
        except Exception as e:
            raise e

        # 获取 Toast 的文本信息
        text = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text

        # 判断 Toast 的文本信息时候匹配
        self.assertEqual(text, "输入的账号密码错误")

        # 截图
        self.driver.get_screenshot_as_file(r"homepage.png")
if __name__ == '__main__':
    unittest.main()
```

## 十一、测试配置及数据分离

### 1、测试配置分离

**应用场景**

对于代码中公共的、可能发生变更的部分，应该将其从代码中分离出来。例如，我们应该将Capability中的值抽离，保存到一个文件中。每一条测试用例在需要用到Capability时，从文件中读取值即可。

**YAML配置文件**

1、YAML中存在三种数据类型，分别为scalar、list、object

```yaml
# scalar：纯量指单个的、不可再分割的值
Storm

# list：数组类似于python中的list，list元素使用“-”开头
- Jack
- Harry
- Sunny
或者 [Jack,Harry,Sunny]

# object：对象是键值对的集合，使用冒号进行表示，类似于python中的字典
platformName: Android
platformVersion: 7.1
```

2、YAML文件操作

```yaml
# 1、安装python的yaml包
pip install PyYAML

# 2、创建my_yaml_1.yml文件
platformName: Android
platformVersion: 9
deviceName: emulator-5554
appPackage: cn.pospal.www.pospal_pos_android_new.pospal
appActivity: cn.pospal.www.pospal_pos_android_new.activity.main.MainActivity

# 3、编写脚本，读取.yml文件
with open("my_yaml.yml", "r", encoding="utf8") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    
# 4、运行结果
{'platformName': 'Android', 'platformVersion': 9, 'deviceName': 'emulator-5554', 'appPackage': 'cn.pospal.www.pospal_pos_android_new.pospal', 'appActivity': 'cn.pospal.www.pospal_pos_android_new.activity.main.MainActivity'}
```

3、在Appium自动化测试中，通常将经常用到的配置信息保存在.yml文件中，然后还需要封装一个函数来读取该文件中的信息，文件名为“parse_yaml.py”。在测试用例中通过读取配置文件，来初始化app信息。

```yaml
# my_yaml.yml

yinbao:
  platformName: Android
  platformVersion: "9"	# 注意，当只有一个数字时，应该加上双引号，否则会被识别为数字，而不是字符串
  deviceName: emulator-5554
  appPackage: cn.pospal.www.pospal_pos_android_new.pospal
  appActivity: cn.pospal.www.pospal_pos_android_new.activity.main.MainActivity
  remoteurl: "http://localhost:4723/wd/hub"
```

```python
# parse_yaml.py

import yaml

def parse_yaml(file, section, key=None) -> dict:
    """
    :param file: 文件名
    :param section: 段落名
    :param key: 键名，如果不传递key，则返回整个字典，如果传递key，则返回单个key
    :return:
    """

    with open(file, 'r', encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if key:
            return data[section][key]
        else:
            return data[section]
```

```python
# test_1_1_login.py

import unittest

import ddt
import yaml
from appium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from parse_yaml import parse_yaml


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        # desired_caps = dict()
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '9'
        # desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['appPackage'] = 'cn.pospal.www.pospal_pos_android_new.pospal'
        # desired_caps['appActivity'] = 'cn.pospal.www.pospal_pos_android_new.activity.main.MainActivity'
        desired_caps = parse_yaml("my_yaml.yml", "yinbao")

        self.driver = webdriver.Remote(parse_yaml("my_yaml.yml", "yinbao", "remoteurl"), desired_caps)

        # 等待页面加载，可以根据实际情况调整等待时间
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()

    """
        1、@ddt.data()，圆括号中可以传递列表或元组
        2、这里传递的是两个列表，代表两个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    @ddt.data(["admin_001", "password_001"], ["admin_002", "password_002"])
    @ddt.unpack
    def test_login(self, username, password):
        def click_until_disappear(driver, element_id, timeout=10, interval=0.5):
            try:
                WebDriverWait(driver, timeout, interval).until_not(
                    lambda x: click_if_exists(x, element_id)
                )
                print(f"Element with ID '{element_id}' has disappeared.")
            except TimeoutException:
                print(f"Element with ID '{element_id}' did not disappear within {timeout} seconds.")

        def click_if_exists(driver, element_id):
            try:
                # 查找并点击元素
                element = driver.find_element(By.ID, element_id)
                element.click()
                return True  # 如果点击成功，返回 True 表示元素仍存在
            except NoSuchElementException:
                return False  # 如果元素不存在，返回 False 表示它已经消失

        # 目标是不断点击“允许”按钮（permission_allow_button），直到它被页面移除：
        click_until_disappear(self.driver, "com.android.packageinstaller:id/permission_allow_button", timeout=5,
                              interval=0.5)

        # 检查“用户名”输入框元素是否存在在DOM中，但元素不一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.presence_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_tv")))
            ele.send_keys(username)
        except Exception as e:
            raise e

        # 检查“密码”输入框元素是否存在在DOM中，且元素一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.visibility_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/password_tv")))
            ele.send_keys(password)
        except Exception as e:
            raise e

        # 检查“登录”按钮元素是否可见并且可以单击
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.element_to_be_clickable((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn")))
            ele.click()
        except Exception as e:
            raise e

        # 获取 Toast 的文本信息
        text = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text

        # 判断 Toast 的文本信息时候匹配
        self.assertEqual(text, "输入的账号密码错误")

        # 截图
        self.driver.get_screenshot_as_file(r"homepage.png")
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()
```

### 2、测试固件与用例代码分离

创建“startend.py”文件，用来继承“unittest.TestCase”类。在该类下定义两个方法，分别是“setUp()”和“tearDown()”

```python
import time
import unittest
from appium import webdriver
from parse_yaml import parse_yaml

class StartEnd(unittest.TestCase):
    def setUp(self):
        desired_caps = parse_yaml("my_yaml.yml", "yinbao")

        self.driver = webdriver.Remote(parse_yaml("my_yaml.yml", "yinbao", "remoteurl"), desired_caps)

        # 等待页面加载，可以根据实际情况调整等待时间
        self.driver.implicitly_wait(15)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
```

改写“test_1_1_login.py”文件，删除该文件中的“setUp()”和“tearDown()”，将该文件中所有类的继承对象更换为继承“StartEnd”类

```python
"""
	“test_1_1_login.py
"""

import unittest

import ddt
import yaml
from appium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from startend import StartEnd


@ddt.ddt
class TestLogin(StartEnd):

    """
        1、@ddt.data()，圆括号中可以传递列表或元组
        2、这里传递的是两个列表，代表两个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    @ddt.data(["admin_001", "password_001"], ["admin_002", "password_002"])
    @ddt.unpack
    def test_login(self, username, password):
        def click_until_disappear(driver, element_id, timeout=10, interval=0.5):
            try:
                WebDriverWait(driver, timeout, interval).until_not(
                    lambda x: click_if_exists(x, element_id)
                )
                print(f"Element with ID '{element_id}' has disappeared.")
            except TimeoutException:
                print(f"Element with ID '{element_id}' did not disappear within {timeout} seconds.")

        def click_if_exists(driver, element_id):
            try:
                # 查找并点击元素
                element = driver.find_element(By.ID, element_id)
                element.click()
                return True  # 如果点击成功，返回 True 表示元素仍存在
            except NoSuchElementException:
                return False  # 如果元素不存在，返回 False 表示它已经消失

        # 目标是不断点击“允许”按钮（permission_allow_button），直到它被页面移除：
        click_until_disappear(self.driver, "com.android.packageinstaller:id/permission_allow_button", timeout=5,
                              interval=0.5)

        # 检查“用户名”输入框元素是否存在在DOM中，但元素不一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.presence_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_tv")))
            ele.send_keys(username)
        except Exception as e:
            raise e

        # 检查“密码”输入框元素是否存在在DOM中，且元素一定可见
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.visibility_of_element_located((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/password_tv")))
            ele.send_keys(password)
        except Exception as e:
            raise e

        # 检查“登录”按钮元素是否可见并且可以单击
        try:
            ele = WebDriverWait(self.driver, 10, 0.5, None).until(
                EC.element_to_be_clickable((By.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn")))
            ele.click()
        except Exception as e:
            raise e

        # 获取 Toast 的文本信息
        text = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text

        # 判断 Toast 的文本信息时候匹配
        self.assertEqual(text, "输入的账号密码错误")

        # 截图
        self.driver.get_screenshot_as_file(r"homepage.png")
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()
```

### 3、测试数据分离

在自动化测试中，参数化数据的格式类似“["admin_001", "password_001"], ["admin_002", "password_002"]”。因此我们需要构造一个公共函数来读取CSV文件。在读取文件时，文件的每一行都会返回一个列表，行与行之间用逗号分隔。

```python
# parse_csv.py

import csv

def parse_csv(file, startline=1):
    """
    :param file: 文件名
    :param startline: 开始行数，默认值为1，即从文件的第二行开始读取，因为一般文件第一行为标题行
    :return:
    """

    mylist = []
    with open(file, "r", encoding="utf8") as f:
        data = csv.reader(f)
        for value in data:
            mylist.append(value)
        if startline == 1:
            del mylist[0]  # 删除标题行数据
        else:
            pass
        return mylist

if __name__ == '__main__':
    data = parse_csv("login_data.csv", 1)
    print(*data)
    print(data)
    
# 运行结果
['admin_001', 'password_001'] ['admin_002', 'password_002']
[['admin_001', 'password_001'], ['admin_002', 'password_002']]

# 因此需要使用*data来参数化用例数据
```

```python
"""
	“test_1_1_login.py
"""

import unittest

import ddt
import yaml
from appium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from startend import StartEnd
from parse_csv import parse_csv


@ddt.ddt
class TestLogin(StartEnd):

    """
        1、@ddt.data()，圆括号中可以传递列表或元组
        2、这里传递的是两个列表，代表两个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    # @ddt.data(["admin_001", "password_001"], ["admin_002", "password_002"])
    @ddt.data(*parse_csv("./login_data.csv"))
    @ddt.unpack
    def test_login(self, username, password):
```

## 十二、Page Object设计模式

所谓的Page Object模式是指，将页面元素的定位以及元素操作从测试用例脚本中分离出来，测试用例脚本直接调用封装好的元素操作来组织测试用例，从而实现测试用例脚本和元素定位、操作分离的效果。

将用例代码划分为3层：

- 第一层：将所有元素对象定位器放到一个文件中
- 第二层：将所有元素操作放到同一个文件中
- 第三层：将公共的业务场景封装到一个文件中

**Page Object实践**

1、在page包下的“locators.py”文件下保存元素定位器

```python
from appium.webdriver.common.appiumby import AppiumBy

class LoginInPageLocators(object):
    """
        登录页元素
    """
    # 系统权限请求的同意按钮
    PermissionAllowBtn = (AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")

    # 账号输入框
    AccountInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_tv")

    # 密码输入框
    PasswordInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/password_tv")

    # 账号登录按钮
    LoginBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn")

    # Toast
    Toast = (AppiumBy.XPATH, "//*[@class='android.widget.Toast']")

    # 体验账号按钮
    TryAccountBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/try_tv")

    # 免费注册按钮
    FreeRegistBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/regist_tv")

    # 联系客服按钮
    ContactServiceBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/contact_customer_service_ll")

    # 账号+工号登录按钮
    AccountCashierLoginBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_cashier_login_ll")

class IndustrySelectionPageLocators(object):
    """
        在登录页选择体验账号后，进入的行业选择页面
    """
    # 零售行业按钮
    RetailBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/retail_version_ll")

    # 餐饮行业按钮
    FoodBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/food_version_ll")

    # 服装鞋帽按钮
    ClothesShoesBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/clothing_version_ll")

    # 生活服务按钮
    ServiceBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/service_version_ll")

    # 母婴行业按钮
    MaternalSupplyBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/maternal_supply_version_ll")

    # 宠物行业按钮
    PetBtn = (AppiumBy, "cn.pospal.www.pospal_pos_android_new.pospal:id/pet_version_ll")

    # 烘焙行业按钮
    BakeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/bake_version_ll")

    # 生鲜称重按钮
    FreshBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/fresh_version_ll")

    # 美妆休闲按钮
    LeisureBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/leisure_version_ll")

    # 尽请期待按钮
    FutureBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/future_version_ll")

class TryLoginInPageLocators(object):
    """
        体验账号登录页元素
    """
    # 账号输入框
    AccountInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_account_tv")

    # 工号输入框
    JobNumberInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/account_tv")

    # 密码输入框
    PasswordInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/password_tv")

    # 员工登录按钮
    EmployeeLoginBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/login_btn")

    # 管理后台按钮
    ManagerBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/manager_ll")

    # 联系客服按钮
    ContactServiceBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/contact_customer_service_ll")

    # 交接班记录按钮
    HistoryHandoverBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/history_handover_ll")

    # Toast
    Toast = (AppiumBy.XPATH, "//*[@class='android.widget.Toast']")
```

2、在page包下的“operations.py”文件下保存对应元素的操作

```python
from selenium.common import NoSuchElementException

from Chapter_14.page.locators import *

class BasePage(object):
    # 构造一个基础类
    def __init__(self, driver):
        self.driver = driver

class LoginInPageOpn(BasePage):
    """
        登录页元素操作
    """
    # 在系统权限请求页面中，点击“同意”按钮
    def click_permission_allow_btn(self):
        print(*LoginInPageLocators.PermissionAllowBtn)
        try:
            print(*LoginInPageLocators.PermissionAllowBtn)
            # 查找点击元素
            ele = self.driver.find_element(*LoginInPageLocators.PermissionAllowBtn)
            ele.click()
            return True # 如果点击成功，返回 True 表示元素仍存在
        except NoSuchElementException:
            return False # 如果元素不存在，返回 False 表示它已经消失

    # 账号输入框输入账号名
    def input_account(self, username):
        ele = self.driver.find_element(*LoginInPageLocators.AccountInput)
        ele.send_keys(username)

    # 密码输入框输入密码
    def input_password(self, password):
        ele = self.driver.find_element(*LoginInPageLocators.PasswordInput)
        ele.send_keys(password)

    # 在输入账号和密码后点击登录按钮
    def click_login_btn(self):
        ele = self.driver.find_element(*LoginInPageLocators.LoginBtn)
        ele.click()

    # 获取Toast文本信息
    def get_toast_text(self) -> str:
        ele = self.driver.find_element(*LoginInPageLocators.Toast)
        return ele.text

    # 体验账号按钮点击
    def try_login_btn(self):
        ele = self.driver.find_element(*LoginInPageLocators.TryAccountBtn)
        ele.click()

    # 免费注册按钮点击
    def free_login_btn(self):
        ele = self.driver.find_element(*LoginInPageLocators.FreeRegistBtn)
        ele.click()

    # 联系客服按钮点击
    def contact_service_btn(self):
        ele = self.driver.find_element(*LoginInPageLocators.ContactServiceBtn)
        ele.click()

    # 账号+工号登录按钮点击
    def account_cashier_login_btn(self):
        ele = self.driver.find_element(*LoginInPageLocators.AccountCashierLoginBtn)
        ele.click()

class IndustrySelectionPageOpn(BasePage):
    """
        在登录页选择体验账号后，进入的行业选择页面的相关操作
    """
    # 零售行业按钮点击
    def retail_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.RetailBtn)
        ele.click()

    # 餐饮行业按钮点击
    def food_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.FoodBtn)
        ele.click()

    # 服装鞋帽按钮点击
    def clothes_shoes_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.ClothesShoesBtn)
        ele.click()

    # 生活服务按钮点击
    def service_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.ServiceBtn)
        ele.click()

    # 母婴行业按钮点击
    def maternal_supply_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.MaternalSupplyBtn)
        ele.click()

    # 宠物行业按钮点击
    def pet_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.PetBtn)
        ele.click()

    # 烘焙行业按钮点击
    def bake_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.BakeBtn)
        ele.click()

    # 生鲜称重按钮点击
    def fresh_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.FreshBtn)
        ele.click()

    # 美妆休闲按钮点击
    def leisure_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.LeisureBtn)
        ele.click()

    # 尽请期待按钮点击
    def future_industry_btn(self):
        ele = self.driver.find_element(*IndustrySelectionPageLocators.FutureBtn)
        ele.click()

class TryLogInPageOpn(BasePage):
    """
        体验账号登录页元素操作
    """
    # 账号输入框文本获取
    def get_account_input_text(self) -> str:
        ele = self.driver.find_element(*TryLoginInPageLocators.AccountInput)
        return ele.text

    # 工号输入框获取工号
    def get_job_number_input_text(self) -> str:
        ele = self.driver.find_element(*TryLoginInPageLocators.JobNumberInput)
        return ele.text

    # 工号输入框输入工号
    def input_job_number(self, job_number):
        ele = self.driver.find_element(*TryLoginInPageLocators.JobNumberInput)
        if len(self.get_job_number_input_text()) != 0:
            ele.clear() #   如果工号输入框中有内容，则先清空内容
        ele.send_keys(job_number)

    # 密码输入框输入密码
    def input_password(self, password):
        ele = self.driver.find_element(*TryLoginInPageLocators.PasswordInput)
        ele.clear()
        ele.send_keys(password)

    # 员工登录按钮点击
    def click_employee_login_btn(self):
        ele = self.driver.find_element(*TryLoginInPageLocators.EmployeeLoginBtn)
        ele.click()

    # 管理后台按钮点击
    def click_manager_btn(self):
        ele = self.driver.find_element(*TryLoginInPageLocators.ManagerBtn)
        ele.click()

    # 联系客服按钮点击
    def click_contact_service_btn(self):
        ele = self.driver.find_element(*TryLoginInPageLocators.ContactServiceBtn)
        ele.click()

    # 交接班记录按钮
    def click_history_handover_btn(self):
        ele = self.driver.find_element(*TryLoginInPageLocators.HistoryHandoverBtn)
        ele.click()

    # 获取Toast文本信息
    def get_toast_text(self) -> str:
        ele = self.driver.find_element(*TryLoginInPageLocators.Toast)
        return ele.text
```

3、在page包下的“scenarios.py”文件下封装常用的业务场景

```python
from Chapter_14.page.operations import *

class LoginScenario(BasePage):
    """
        定义了与登录相关的场景
    """
    # 输入账号名和密码，并且点击登录按钮
    def fillin_account_pwd_and_login(self, username, password):
        LoginInPageOpn(self.driver).input_account(username) # 账号输入框输入账号名
        LoginInPageOpn(self.driver).input_password(password)    # 密码输入框输入密码
        LoginInPageOpn(self.driver).click_login_btn()   # 在输入账号和密码后点击登录按钮
```

4、修改测试用例文件“test_1_1_login.py”

```python
import sys
sys.path.append(r"C:\Users\Administrator\PycharmProjects\PythonProject")

import unittest

import ddt
import yaml
from appium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from Chapter_14.case.startend import StartEnd
from Chapter_14.case.parse_csv import parse_csv
from Chapter_14.page.operations import LoginInPageOpn
from Chapter_14.page.scenarios import LoginScenario


@ddt.ddt
class TestLogin(StartEnd):

    """
        1、@ddt.data()，圆括号中可以传递列表或元组
        2、这里传递的是两个列表，代表两个测试用例
        3、每个测试用例包含两个参数：
            1）用户名
            2）密码
    """
    # @ddt.data(["admin_001", "password_001"], ["admin_002", "password_002"])
    @ddt.data(*parse_csv("./login_data.csv"))
    @ddt.unpack
    def test_login(self, username, password):
        # 在系统权限请求页面中，点击“同意”按钮
        def click_until_disappear(driver, element_id, timeout=10, interval=0.5):
            try:
                WebDriverWait(driver, timeout, interval).until_not(
                    lambda x: LoginInPageOpn(self.driver).click_permission_allow_btn()
                )
                print(f"Element with ID '{element_id}' has disappeared.")
            except TimeoutException:
                print(f"Element with ID '{element_id}' did not disappear within {timeout} seconds.")

        # 目标是不断点击“允许”按钮（permission_allow_button），直到它被页面移除：
        click_until_disappear(self.driver, "com.android.packageinstaller:id/permission_allow_button", timeout=5,
                              interval=0.5)

        # 执行输入账号名和密码，并且点击登录按钮的命令
        LoginScenario(self.driver).fillin_account_pwd_and_login(username, password)

        # 获取 Toast 的文本信息
        text = LoginInPageOpn(self.driver).get_toast_text()

        # 判断 Toast 的文本信息时候匹配
        self.assertEqual(text, "输入的账号密码错误")

        # 截图
        self.driver.get_screenshot_as_file(r"homepage.png")
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()
```

最后总体项目结构为：

![image-20241128182134781](../images/image-20241128182134781.png)

### **目前还存在的问题：**

#### 1、目录结构混乱

case目录中存放了测试用例、测试数据、配置数据和一些封装好的公共函数文件，整个目录结构显得非常混乱

#### 2、缺乏测试日志

如果测试执行失败，没有对应的日子，较难定位问题，需要添加日志功能

#### 3、缺乏错误截图

在元素定位失败或者测试用例发生异常是，如果有错误截图，可以更加直观的定位问题

#### 4、缺乏显式等待

如果为每个定位元素都加上显式等待，代码会显得非常冗长，后续需要封装Appium元素定位API来解决该问题

## 十三、自动化测试框架开发

![image-20241129154713172](../images/image-20241129154713172.png)

### 1、优化目录层级

因为项目的结构发生了变化，因此需要对文件中模块的引用关系进行调整。在调整测试文件中目录引用和文件引用的时候们，需要使用相对路径，尽量少用绝对路径，以避免更换项目后，代码需要大量调整。

#### 1.1 Python os模块

**（1）获取操作系统信息**

- `os.sep`用来获取当前系统路径的分隔符，Windows为“\”，而Linux和macOS则是使用的“/”
- `os.name`用于获取当前使用的工作平台，“nt”表示Windows，“posix”表示Linux或macOS
- `os.getcwd`用于获取当前文件的路径

**（2）目录操作**

- `os.listdir(目录)`：返回指定目录下的所有文件和目录
- `os.mkdir('D:\\ABC')`：创建一个目录
- `os.rmdir('D:\\ABC')`：删除空目录，若目录不为空则不能删除
- `os.makedirs('D:\\ABC\DEF\')`：可以生成多层递归目录，如果目录存在，则创建失败
- `os.removedirs('D:\\ABC\DEF\')`：可以删除多层递归目录，若目录中有文件，这不能删除
- `os.rename('D:\\ABC\\DEF', 'D:\\abc\\xyz')`：重命名目录货文件，命名后的文件或目录名罗存在，则重命名失败
- `os.path.basename('D:\\ABC\\DEF\\a.txt')`：返回指定路径的文件名（即文件名）
- `os.path.dirname('D:\\ABC\\DEF\\a.txt')`：返回指定路径的父路径
- `os.path.abspath(name)`：返回文件的绝对路径
- `os.path.join(path, name)`：将多个文件路径或文件名连接到一起

**（3）判断操作**

- `os.path.exists(path)`：判断文件或目录是否存在
- `os.path.isfile(path)`：判断传参是否为文件
- `os.path.isdir(path)`：判断是否为目录

#### 1.2 调整模块引用

（1）新增basepage.py文件

方便后续对driver进行个性化定制

```python
class BasePage(object):
    # 构造一个基础类
    def __init__(self, driver):
        self.driver = driver
```

（2）调整测试用例文件中的路径信息

```python
@ddt.ddt
class TestLogin(StartEnd):
    """
        1、os.getcwd() 返回当前工作目录（即 Python 进程的当前目录）
        2、os.path.dirname(path) 返回指定路径的父目录
        3、这是字符串 "data"，它表示一个文件夹名称。接下来会把它拼接到路径中
        4、os.path.basename(__file__) 会从这个路径中提取出文件名部分。例如，如果脚本的路径是 /home/user/myproject/test.py，那么 os.path.basename(__file__) 返回的就是 "test.py"
        5、split(".") 将文件名根据 "." 分割成一个列表，[0] 获取文件名的第一部分（去掉扩展名）。比如，"test.py".split(".") 会得到 ["test", "py"]，取 [0] 后，得到 "test"
    """
    file_dir = os.path.join(os.path.dirname(os.getcwd()), "data", os.path.basename(__file__).split(".")[0]) + ".csv"    # 拼接测试数据的路径

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
    def test_login(self, username, password):
        logging.info("==========test_login==========")
```

### 2、增加日志信息

#### 2.1 日志概述

（1）日志的作用

日志能够帮助我们查找自动化测试用例执行失败的节点，如果测试项目在linux服务器上运行，没有PyCharm控制台输出日志，那么就无法采集到日志信息。

（2）日志级别

- DEBUG：输出最详细的日志信息
- INFO：证明软件按预期工作
- WARNING：表明软件发生了一些意外，或者在将来会出现问题
- ERROR：软件出现严重问题
- CRITICAL：出现严重错误，表明软件不能再运行了

注意：日志级别越高，输出的日志内容越少

#### 2.2 Python logging

Python的logging模块提供了两种日志记录方式：

- 使用logging提供的模块级别的函数
- 使用logging日志系统的四大组件记录

**（1）使用logging提供的模块级别的函数**

```python
# 导入logging 模块
import logging

# 设置日志级别和日志保存路径
logging.basicConfig(filename='F:\\example.log', level=logging.DEBUG)

# 定制化显示消息时间
logging.basicConfig(format='%(asctime)s %(message)s')

# 输出日志信息
logging.INFO("  ")
logging.ERROR("   ")
```

**（2）使用logging日志系统的四大组件记录**

**1. Logger，日志记录器**

用于设置日志采集，使用之前必须创建Logger实例

```python
logger = logging.getLogger(logger_name)
```

**2. Handler，日志处理器**

处理器负责将日志记录发送至目标路径显示或存储。比较常用的Handler有三种：StreamHandler、FileHandler、NullHandler

```python
ch = logging.StreamHandler(stream=None)
```

**3. Filter，日志过滤器**

过滤器用来对输出日志进行粒度控制，它可以决定输出那些日志记录

```python
filter = logging.Filter(name='')
```

**4. Formatter，日志格式化器**

格式化器致命了最终输出日志的格式

```python
formatter = logging.Formatter(fmt=None, datafmt=None)
```

#### 2.3 为测试用例增加日志

（1）日志格式配置文件

在conf目录中新建log.conf文件，内容为日志格式的配置信息

```python
[loggers]
keys=root,infoLogger

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[logger_infoLogger]
handlers=consoleHandler,fileHandler
qualname=infoLogger
propagate=0

[handlers]
keys=consoleHandler,fileHandler

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=form02
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=form01
args=('..\\log\\runlog.log', 'a')

[formatters]
keys=form01,form02

[formatter_form01]
format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s

[formatter_form02]
format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s
```

（2）修改startend.py文件

```python
import time
import traceback
import unittest
from appium import webdriver
from src.base import parse_yaml
import logging
import logging.config

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
SCREENSHOT_DIR = '../src/screenshot/'


class StartEnd(unittest.TestCase):
```

（3）为需要输出日志的类，添加输出日志

例如在operation.py中添加日志输出

```python
from src.page.locators import *
from src.base import *
import logging

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
```

### 3、增加页面截图功能

#### 3.1 断言失败截图

因为StartEnd类继承自unittest.TestCase类。而unittest.TestCase类中存在一个属性failureException。测试用例类继承自StartEnd类，所以测试用例类也存在failureException属性。当测试用例调用unittest提供的断言方法出现断言失败时，实际上调用的是测试用例类的self.failureException属性。而这个属性调用了重写的AssertionError（python提供的异常类），从而获得了断言失败截图的功能。

```python
import os
import time
import traceback
import unittest
from appium import webdriver
from src.base import parse_yaml
import logging
import logging.config

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
SCREENSHOT_DIR = '../src/screenshot/'


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("=========setUp===========")
        desired_caps = parse_yaml("../src/config/my_yaml.yml", "yinbao")

        self.driver = webdriver.Remote(parse_yaml("../src/config/my_yaml.yml", "yinbao", "remoteurl"), desired_caps)

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
                    cur_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间戳
                    # file_name = '{}_{}.png'.format(cur_method, cur_time)
                    file_name = '{}.png'.format(cur_time)
                    test_case.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name))  # 截图生成 png 文件
                    logging.info("失败截图已保存到：{}".format(file_name))
                except BaseException:
                    logging.error("截图失败：{}".format(
                        traceback.format_exc()))  # logging.error("截图失败：{}".format(traceback.format_exc()))
                super(AssertionErrorPlus, self).__init__(msg)  # 调用父类 AssertionError 的构造方法，将错误消息 msg 传递给父类

        return AssertionErrorPlus  # 返回自定义的异常类，这意味着你可以在其他地方使用 failure_monitor 来动态生成一个自定义异常，并且通过 raise 语句抛出它

    def tearDown(self):
        logging.info("========tearDown=========")
        time.sleep(2)
        self.driver.quit()
```

#### 3.2 元素定位失败截图

在basepage.py文件中封装元素定位方法，当元素获取失败时自动生成截图

具体代码详见第4节——增加显式等待功能

### 4、增加显式等待功能

（1）对basepage.py文件进行二次封装，增加显式等待功能。使得operations.py中的所有方法都使用统一的元素定位方法

```python
import time, os
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SCREENSHOT_DIR = '../sreenshot/'    # 截图保存目录，相对路径
cur_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))   # 获取当前时间
file_name = '{}.png'.format(cur_time)

class BasePage(object):
    # 构造一个基础类
    def __init__(self, driver):
        self.driver = driver

    def get_presence_element(self, locator, timeout = 10):
        """
            获取存在，但不一定可见的元素，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :return: 返回存在，但不一定可见的元素
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))

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

    def get_elements(self, locator, timeout = 10):
        """
            获取一组存在的元素，但不一定可见，在元素定位的时候添加显式等待功能
            :param locator: By方法定位元素，如（By.XPATH, "//*[@class='frank]"）
            :param timeout:
            :return: 返回一组存在的元素
        """
        try:
            return self.driver.find_elements(locator)
        except Exception as e:
            # 截图、日志
            self.driver.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name)) # 截图生成png文件
            logging.error("元素定位失败：{}".format(file_name))
```

（2）修改operation.py中的元素定位方法，使用basepage.py文件中的统一定位方法

```python
from selenium.common import NoSuchElementException

from src.page.locators import *
from src.base import *
import logging

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
        ele = self.get_clickable_element(LoginInPageLocators.PermissionAllowBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 账号输入框输入账号名
    def input_account(self, username):
        logging.info('==========input_account==========')
        # ele = self.driver.find_element(*LoginInPageLocators.AccountInput)
        ele = self.get_visible_element(LoginInPageLocators.AccountInput)  # 替换为添加了显示等待的元素定位方法
        ele.send_keys(username)

    # 密码输入框输入密码
    def input_password(self, password):
        logging.info('==========input_password==========')
        # ele = self.driver.find_element(*LoginInPageLocators.PasswordInput)
        ele = self.get_visible_element(LoginInPageLocators.PasswordInput)  # 替换为添加了显示等待的元素定位方法
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
        ele = self.get_clickable_element(LoginInPageLocators.TryAccountBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 免费注册按钮点击
    def free_login_btn(self):
        logging.info('==========free_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.FreeRegistBtn)
        ele = self.get_clickable_element(LoginInPageLocators.FreeRegistBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 联系客服按钮点击
    def contact_service_btn(self):
        logging.info('==========contact_service_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.ContactServiceBtn)
        ele = self.get_clickable_element(LoginInPageLocators.ContactServiceBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 账号+工号登录按钮点击
    def account_cashier_login_btn(self):
        logging.info('==========account_cashier_login_btn==========')
        # ele = self.driver.find_element(*LoginInPageLocators.AccountCashierLoginBtn)
        ele = self.get_clickable_element(LoginInPageLocators.AccountCashierLoginBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()


class IndustrySelectionPageOpn(BasePage):
    """
        在登录页选择体验账号后，进入的行业选择页面的相关操作
    """

    # 零售行业按钮点击
    def retail_industry_btn(self):
        logging.info('==========retail_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.RetailBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.RetailBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 餐饮行业按钮点击
    def food_industry_btn(self):
        logging.info('==========food_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.FoodBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FoodBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 服装鞋帽按钮点击
    def clothes_shoes_industry_btn(self):
        logging.info('==========clothes_shoes_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.ClothesShoesBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.ClothesShoesBtn)  # 替换为添加了显示等待的元素定位方法
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
        ele = self.get_clickable_element(IndustrySelectionPageLocators.MaternalSupplyBtn)  # 替换为添加了显示等待的元素定位方法
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
        ele = self.get_clickable_element(IndustrySelectionPageLocators.BakeBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 生鲜称重按钮点击
    def fresh_industry_btn(self):
        logging.info('==========fresh_industry_btn==========')
        # ele = self.driver.find_element(*IndustrySelectionPageLocators.FreshBtn)
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FreshBtn)  # 替换为添加了显示等待的元素定位方法
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
        ele = self.get_clickable_element(IndustrySelectionPageLocators.FutureBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()


class TryLogInPageOpn(BasePage):
    """
        体验账号登录页元素操作
    """

    # 账号输入框文本获取
    def get_account_input_text(self) -> str:
        logging.info('==========get_account_input_text==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.AccountInput)
        ele = self.get_visible_element(TryLoginInPageLocators.AccountInput)  # 替换为添加了显示等待的元素定位方法
        return ele.text

    # 工号输入框获取工号
    def get_job_number_input_text(self) -> str:
        logging.info('==========get_job_number_input_text==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.JobNumberInput)
        ele = self.get_visible_element(TryLoginInPageLocators.JobNumberInput)  # 替换为添加了显示等待的元素定位方法
        return ele.text

    # 工号输入框输入工号
    def input_job_number(self, job_number):
        logging.info('==========input_job_number==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.JobNumberInput)
        ele = self.get_visible_element(TryLoginInPageLocators.JobNumberInput)  # 替换为添加了显示等待的元素定位方法
        if len(self.get_job_number_input_text()) != 0:
            ele.clear()  # 如果工号输入框中有内容，则先清空内容
        ele.send_keys(job_number)

    # 密码输入框输入密码
    def input_password(self, password):
        logging.info('==========input_password==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.PasswordInput)
        ele = self.get_visible_element(TryLoginInPageLocators.PasswordInput)  # 替换为添加了显示等待的元素定位方法
        ele.clear()
        ele.send_keys(password)

    # 员工登录按钮点击
    def click_employee_login_btn(self):
        logging.info('==========click_employee_login_btn==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.EmployeeLoginBtn)
        ele = self.get_clickable_element(TryLoginInPageLocators.EmployeeLoginBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 管理后台按钮点击
    def click_manager_btn(self):
        logging.info('==========click_manager_btn==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.ManagerBtn)
        ele = self.get_clickable_element(TryLoginInPageLocators.ManagerBtn)  # 替换为添加了显示等待的元素定位方法
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
        ele = self.get_clickable_element(TryLoginInPageLocators.HistoryHandoverBtn)  # 替换为添加了显示等待的元素定位方法
        ele.click()

    # 获取Toast文本信息
    def get_toast_text(self) -> str:
        logging.info('==========get_toast_text==========')
        # ele = self.driver.find_element(*TryLoginInPageLocators.Toast)
        ele = self.get_presence_element(TryLoginInPageLocators.Toast)  # 替换为添加了显示等待的元素定位方法
        return ele.text
```

