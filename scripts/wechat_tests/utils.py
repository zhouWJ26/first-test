import yaml
import os
from appium.webdriver.webdriver import WebDriver
from typing import Tuple

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.yml")


def load_caps() -> Tuple[str, dict]:
    """读取 Appium server 地址及 desired capabilities."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["appium"]["server"], data["appium"]["desired_caps"]


def launch_driver() -> WebDriver:
    """启动 Appium driver."""
    from appium import webdriver  # 延迟导入避免未安装时报错
    server, caps = load_caps()
    driver = webdriver.Remote(server, caps)
    driver.implicitly_wait(10)
    return driver