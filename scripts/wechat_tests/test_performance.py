import time
import pytest
from appium.webdriver.webdriver import WebDriver
from .utils import load_caps
from appium import webdriver


@pytest.mark.performance
def test_cold_launch_time():
    """测量冷启动耗时，应 < 3 秒 (示例阈值)。"""
    server, caps = load_caps()
    caps["noReset"] = False  # 冷启动：关闭后台、清理状态
    start = time.time()
    driver = webdriver.Remote(server, caps)
    driver.implicitly_wait(10)
    # 判断首页出现（底栏“微信”可见）
    driver.find_element("xpath", "//android.widget.TextView[@text='微信']")
    elapsed = time.time() - start
    driver.quit()
    assert elapsed < 3.0, f"Cold launch took {elapsed:.2f}s > 3s"