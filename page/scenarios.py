from page.operations import *
from base.basepage import *

class LoginScenario(BasePage):
    """
        定义了与登录相关的场景
    """
    # 输入账号名和密码，并且点击登录按钮
    def fillin_account_pwd_and_login(self, username, password):
        LoginInPageOpn(self.driver).input_account(username) # 账号输入框输入账号名
        LoginInPageOpn(self.driver).input_password(password)    # 密码输入框输入密码
        LoginInPageOpn(self.driver).click_login_btn()   # 在输入账号和密码后点击登录按钮