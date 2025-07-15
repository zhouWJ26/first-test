import pytest
from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures("driver")
class TestContacts:
    def goto_contacts_tab(self, driver: WebDriver):
        """点击底栏“通讯录”。"""
        driver.find_element("xpath", "//android.widget.TextView[@text='通讯录']").click()

    def test_search_contact(self, driver: WebDriver):
        """搜索指定联系人应在结果中出现。"""
        self.goto_contacts_tab(driver)
        driver.find_element("id", "com.tencent.mm:id/f_r").click()  # 搜索输入框按钮 (占位)
        keyword = "张三"
        driver.find_element("id", "com.tencent.mm:id/dkc").send_keys(keyword)  # 输入框 id 需按版本确认
        results = driver.find_elements("xpath", f"//android.widget.TextView[contains(@text,'{keyword}')]")
        assert len(results) > 0, f"Search results for {keyword} not found!"