import time
import pytest
from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures("driver")
class TestMoments:
    def open_moments(self, driver: WebDriver):
        """导航到发现->朋友圈。"""
        driver.find_element("xpath", "//android.widget.TextView[@text='发现']").click()
        driver.find_element("xpath", "//android.widget.TextView[@text='朋友圈']").click()

    def post_text_moment(self, driver: WebDriver, text: str):
        """发布纯文本朋友圈动态。"""
        # 点击右上角相机按钮
        driver.find_element("id", "com.tencent.mm:id/ewt").click()
        driver.find_element("id", "com.tencent.mm:id/g5f").send_keys(text)
        driver.find_element("id", "com.tencent.mm:id/g5h").click()  # 发布按钮

    def test_post_text_moment(self, driver: WebDriver):
        text = f"自动化{int(time.time())}"
        self.open_moments(driver)
        self.post_text_moment(driver, text)
        # 朋友圈界面会自动回到列表，等待刷新顶部
        time.sleep(3)
        top_text = driver.find_element("id", "com.tencent.mm:id/bxa").text  # 动态文本 id 需确认
        assert text in top_text