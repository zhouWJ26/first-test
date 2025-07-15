import pytest
from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures("driver")
class TestSettings:
    def open_language_settings(self, driver: WebDriver):
        driver.find_element("xpath", "//android.widget.TextView[@text='我']").click()
        driver.find_element("xpath", "//android.widget.TextView[@text='设置']").click()
        driver.find_element("xpath", "//android.widget.TextView[@text='通用']").click()
        driver.find_element("xpath", "//android.widget.TextView[@text='多语言']").click()

    def select_language(self, driver: WebDriver, lang: str):
        driver.find_element("xpath", f"//android.widget.TextView[@text='{lang}']").click()
        driver.find_element("id", "com.tencent.mm:id/hd_" ).click()  # 完成按钮 id placeholder

    def test_switch_language_to_english_and_back(self, driver: WebDriver):
        # 切换到 English
        self.open_language_settings(driver)
        self.select_language(driver, "English")
        # 断言首页文本变为 English (Chats)
        driver.find_element("id", "com.tencent.mm:id/h83").click()  # 返回首页
        assert driver.find_element("xpath", "//android.widget.TextView[@text='Chats']")
        # 切回 简体中文
        self.open_language_settings(driver)
        self.select_language(driver, "简体中文")
        driver.find_element("id", "com.tencent.mm:id/h83").click()
        assert driver.find_element("xpath", "//android.widget.TextView[@text='微信']")