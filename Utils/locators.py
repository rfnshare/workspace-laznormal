class IntroPageLocator(object):
    skip = 'com.daraz.android.dev:id/intro_skip_btn'  # id
    language = 'android:id/button1'  # id
    country = '//android.widget.TextView[@text="Bangladesh"]'  # xpath
    location = 'com.daraz.android.dev:id/btn_trade_confirm_dialog_negative'  # id
    add_skip = 'com.daraz.android.dev:id/iv_close_btn'  # id
    log_deny = '//*[@text="android:id/log_access_dialog_deny_button"]'


class HomePageLocator(object):
    back = "//android.widget.ImageButton"
    account_tab = "(//*[@resource-id='com.daraz.android.dev:id/icon'])[3]"  # xpath
    login = "com.daraz.android.dev:id/txt_login_signup"  # id
    signin_with_email = "com.daraz.android.dev:id/tv_signin"  # id
    email_field = "(//android.widget.EditText)[1]"  # xpath
    pass_field = "(//*[@resource-id='com.daraz.android.dev:id/et_input_text'])[2]"  # xpath
    final_login = "com.daraz.android.dev:id/btn_next"  # id
    val_name = "com.daraz.android.dev:id/txt_name"  # id


class NotificationsPageLocator(object):
    check_notifications = "android:id/status_bar_latest_event_content"
    entry = "//android.widget.TextView[@text='TestEntry: Online']"
    mtop = "//android.widget.Button[@text='MTOP Env']"
    stage_option = "//android.widget.CheckedTextView[@text='Stage']"
    online_option = "//android.widget.CheckedTextView[@text='Online']"
