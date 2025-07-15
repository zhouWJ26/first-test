import pytest
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures("driver")
class TestFavorites:
    def goto_first_chat(self, driver: WebDriver):
        # 确保在微信主页
        try:
            driver.find_element("xpath", "//android.widget.TextView[@text='微信']").click()
        except Exception:
            pass
        driver.find_elements("id", "com.tencent.mm:id/bhp")[0].click()

    def long_press_last_image(self, driver: WebDriver):
        images = driver.find_elements("id", "com.tencent.mm:id/ijm")  # 图片 message id placeholder
        last_img = images[-1]
        TouchAction(driver).long_press(last_img).perform()
        driver.find_element("xpath", "//android.widget.TextView[@text='收藏']").click()
        time.sleep(1)

    def open_favorites(self, driver: WebDriver):
        driver.find_element("xpath", "//android.widget.TextView[@text='我']").click()
        driver.find_element("xpath", "//android.widget.TextView[@text='收藏']").click()

    def test_collect_image(self, driver: WebDriver):
        self.goto_first_chat(driver)
        self.long_press_last_image(driver)
        self.open_favorites(driver)
        assert len(driver.find_elements("id", "com.tencent.mm:id/h_w")) > 0  # 收藏项 id placeholder