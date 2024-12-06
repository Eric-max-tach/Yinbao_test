from appium.webdriver.common.appiumby import AppiumBy

class LoginInPageLocators(object):
    """
        登录页元素
    """
    # 在系统权限请求页面中，获取current_page_text中的文本信息，即“第 1 项权限（共 3 项）”
    PermissionPageText = (AppiumBy.ID, "com.android.packageinstaller:id/current_page_text")

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

class CashInterface(object):
    """
        收银页面元素
    """
    # 未读消息按钮
    UreadMessageBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/notice_ib")

    # 获取Toast
    Toast = (AppiumBy.XPATH, "//*[@class='android.widget.Toast']")

    # 分类集合
    CategoryList = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/category_gv']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/root_rl']")

    # 获取具体分类的文本框
    CategoryText = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv']")

    # 某一分类下商品集合
    GoodsList = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/product_rv']/*[@class='android.widget.RelativeLayout']")

    # 某一分类下,某个商品的商品名
    GoodsNameText = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv']")

    # 某一分类下,某个商品的价格
    GoodsPriceText = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/price_et']")

    # “点击选择会员”按钮
    SelectMemberBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/customer_rl")

    # “订单”视图框
    OrderView = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls")

    # 当前屏幕中订单视图框内所有商品的序号的元素集合
    OrderViewGoodsNums = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/no_tv']")

    # 当前屏幕中订单视图框内所有商品的名称的元素集合
    OrderViewGoodsNames = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/plu_name_tv']")

    # 当前屏幕中订单视图框内所有商品的单价的元素集合
    OrderViewGoodsPrices = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/price_tv']")

    # 当前屏幕中订单视图框内所有商品的折扣的元素集合
    OrderViewGoodsDiscounts = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/sale_ls']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/discount_tv']")

    # “收银”按钮
    CashBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/checkout_action_ll")

    # “实收金额”文本值
    ReceiptPriceText = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/checkout_action_ll']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/amount_tv']")

    # “总额”文本值
    TotalPriceText = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/cart_rl']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/subtotal_tv']")

    # “折扣”文本值
    DiscountText = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/cart_rl']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/discount_tv']")

    # “优惠券”图标按钮
    CouponBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_ll")

class SelectCouponInterface(object):
    """
        在收银页面的订单栏下方点击“优惠券”图标按钮后进入的选择优惠券页面元素定位
    """
    # “普通优惠券”按钮
    GeneralCouponBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/general_coupon_rb")

    # “通用券码”按钮
    CommentCouponBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/comment_coupon_rb")

    # “券扫码下单”按钮
    CouponScanBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/scanning_code_order_rb")

    # “优惠券列表”视图框
    CouponListView = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupons_recycle_view")

    # “优惠券列表”中优惠券的“添加”按钮集合
    CouponAddBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/add_iv")

    # “优惠券列表”中优惠券的“删除”按钮集合
    CouponDeleteBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/sub_iv")

    # “优惠券列表”中优惠券的“已添加优惠券数量”文本值集合
    CouponAddedNumText = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/qty_tv")

    # “优惠券列表”中优惠券的“名称”文本值集合
    CouponNameText = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_name_tv")

    # “确定”按钮
    ConfirmBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")

class NewProductPage(object):
    """
        新增商品页面元素
    """
    # “生成”按钮，生成随机条码
    GenerateBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/generate_barcode")

    # 商品条码文本框
    BarcodeInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/number_et")

    # “品名”文本框
    NameInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/name_et")

    # “库存”文本框
    StockInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/stock_et")

    # “售价”文本框
    PriceInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/price_et")

    # “进价”文本框
    PurchasePriceInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/buy_price_et")

    # “保存”按钮
    SaveBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/save_ll")

    # “分类”下拉框
    CategoryDropdown = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/category_tv")

    # “分类”下拉框中的搜索框
    CategorySearchInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/input_et")

    # “分类”下拉框中的搜索结果
    CategorySearchResult = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/ctg_rv']/*[@class='android.widget.LinearLayout']")

    # “分类”下拉框中的确定按钮
    CategorySearchConfirmBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")


class MessageCenterPageLocators(object):
    """
        消息中心页面元素
    """
    # 库存预警按钮
    StockWarningBtn = (AppiumBy.XPATH, "//*[@text='库存预警']")

    # 库存预警的数量
    StockWarningCount = (AppiumBy.XPATH, "//*[@text='库存预警']/following-sibling::*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/count_tv']")

    # 全选按钮
    SelectAllBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/select_all_iv")

    # 忽略此商品按钮
    IgnoreThisGoodsBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/left_btn")

    # 返回按钮
    BackBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/back_tv")

class SelectMemberPage(object):
    """
        选择会员页面元素定位
    """
    # 搜索框“输入卡号/手机/姓名搜索会员”
    SearchInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/input_et")

    # 数字“1”
    OneBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_1")

    # 数字“2”
    TwoBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_2")

    # 数字“3”
    ThreeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_3")

    # 数字“4”
    FourBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_4")

    # 数字“5”
    FiveBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_5")

    # 数字“6”
    SixBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_6")

    # 数字“7”
    SevenBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_7")

    # 数字“8”
    EightBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_8")

    # 数字“9”
    NineBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_9")

    # 数字“0”
    ZeroBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_0")

    # 数字“00”
    ZeroZeroBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_00")

    # 数字“.”
    DotBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_dot")

    # “删除”按钮
    DeleteBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_del")

    # “确定”按钮
    ConfirmBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")

    # “添加会员”按钮
    AddMemberBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/add_btn")

    # “扫描”按钮
    ScanBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/scan_mode_ib")

    # “返回”按钮
    BackBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/back_tv")

class MembershipDetailsPage(object):
    """
        会员详情页元素定位
    """
    # “充值”按钮
    RechargeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/recharge_btn")

    # “选择会员”按钮
    SelectMemberBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/choose_btn")

    # “余额”文本值
    BalanceText = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/balance_tv")

    # “积分”文本值
    PointsText = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/point_tv")

    # “优惠券查看”按钮
    CouponViewBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_check_btn")

    # “积分兑换”按钮
    PointsExchangeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/exchange_btn")

class MemberRechargePage(object):
    """
        会员充值页面元素定位
    """
    # 充值项列表
    RechargeItemList = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/pass_product_list']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/root_rl']")

    # “现金”充值按钮
    CashBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv' and @text='现金']")

    # “银联卡”充值按钮
    UnionPayBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv' and @text='银联卡']")

    # “收款码”充值按钮
    QRCodeBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv' and @text='收款码']")

    # “支付宝”充值按钮
    AliPayBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv' and @text='Zfb支付']")

    # “微信”充值按钮
    WechatBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv' and @text='微信']")

    # “三福”充值按钮
    SFPayBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/name_tv' and @text='三福支付']")

    # “确认充值”按钮
    ConfirmRechargeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")

    # “充值成功后打印小票”选择框
    PrintReceiptCheckBox = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/checkbox_ll']/*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/checkbox']")

class CouponPage(object):
    """
        优惠券页面元素定位
    """
    # “不可用券”按钮
    UnavailableCouponBtn = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/action_1_tv' and @text='不可用券']")

    # “优惠券”列表视图
    CouponListView = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/customer_coupon_rv']")

class NotAvailableCouponPage(object):
    """
        不可用优惠券页面元素定位
    """
    # “未生效优惠券”视图框
    UnavailableCouponView = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv")

    # “已过期优惠券”视图框
    ExpiredCouponView = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/expired_customer_coupon_rv']")

    # “未生效优惠券”的优惠券编号
    UnavailableCouponNum = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_code_tv']")

    # “未生效优惠券”的优惠券名称
    UnavailableCouponName = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/invalid_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_name_tv']")

    # “已过期优惠券”的优惠券编号
    ExpiredCouponNum = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/expired_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_code_tv']")

    # “已过期优惠券”的优惠券名称
    ExpiredCouponName = (AppiumBy.XPATH, "//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/expired_customer_coupon_rv']//*[@resource-id='cn.pospal.www.pospal_pos_android_new.pospal:id/coupon_name_tv']")

class PointExchangePage(object):
    """
        积分兑换页面元素定位
    """
    # “积分兑换商品”视图列表元素项
    PointsExchangeViewElem = (
        AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/root_ll")

    # “积分兑换商品”列表中商品项的积分值
    PointsExchangeItemPoints = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/need_point_tv")

    # "积分兑换商品"列表中商品项的品名
    PointsExchangeItemNames = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/product_name_tv")

    # “兑换”按钮
    ExchangeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")

    # “积分兑换商品”视图
    PointsExchangeView = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/product_list")

    # 搜索框
    SearchInput = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/input_et")

class RechargeDetailPage(object):
    """
        结账详情页元素定位
    """
    # "现金"按钮
    CashBtn = (AppiumBy.XPATH, "//*[@text='现金']")

    # "储值卡"按钮
    ValueCardBtn = (AppiumBy.XPATH, "//*[@text='储值卡']")

    # "银联卡"按钮
    UnionPayBtn = (AppiumBy.XPATH, "//*[@text='银联卡']")

    # "收款码"按钮
    QRCodeBtn = (AppiumBy.XPATH, "//*[@text='收款码']")

    # "Zfb支付"按钮
    AliPayBtn = (AppiumBy.XPATH, "//*[@text='Zfb支付']")

    # "预付卡"按钮
    PrepaidCardBtn = (AppiumBy.XPATH, "//*[@text='预付卡']")

    # 数字“1”
    OneBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_1")

    # 数字“2”
    TwoBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_2")

    # 数字“3”
    ThreeBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_3")

    # 数字“4”
    FourBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_4")

    # 数字“5”
    FiveBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_5")

    # 数字“6”
    SixBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_6")

    # 数字“7”
    SevenBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_7")

    # 数字“8”
    EightBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_8")

    # 数字“9”
    NineBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_9")

    # 数字“0”
    ZeroBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_0")

    # 数字“00”
    ZeroZeroBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_00")

    # 数字“.”
    DotBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_dot")

    # “删除”按钮
    DeleteBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/num_del")

    # “确定”按钮
    ConfirmBtn = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/ok_btn")

    # “应收金额”文本信息
    ReceivableAmountText = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/after_amount_tv")

    # “实收金额”文本信息
    ActualAmountText = (AppiumBy.ID, "cn.pospal.www.pospal_pos_android_new.pospal:id/real_take_et")
