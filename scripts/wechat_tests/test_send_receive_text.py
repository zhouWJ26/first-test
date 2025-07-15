import yaml
import time
import os
import pytest
from appium import webdriver

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.yml")


def load_caps():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["appium"]["server"], data["appium"]["desired_caps"]


class TestChatMessage:
    @classmethod
    def setup_class(cls):
        server, caps = load_caps()
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def goto_first_chat(self):
        """进入最近聊天第一个会话"""
        # 微信主界面默认在最近聊天页，若不是可点击底栏“微信”
        try:
            self.driver.find_element("xpath", "//android.widget.TextView[@text='微信']").click()
        except Exception:
            pass
        # 点击第一个聊天条目
        first_chat = self.driver.find_elements("id", "com.tencent.mm:id/bhp")[0]
        first_chat.click()

    def send_text(self, text: str):
        input_box = self.driver.find_element("id", "com.tencent.mm:id/bsb")  # 输入框 resourceId 需按实际版本调整
        input_box.send_keys(text)
        self.driver.find_element("id", "com.tencent.mm:id/bw_" ).click()  # 发送按钮 id 同样需确认

    @pytest.mark.parametrize("text", ["Hello🐱", "自动化测试"], ids=["english", "chinese"])
    def test_send_text(self, text):
        """发送文本消息并断言自己可见"""
        self.goto_first_chat()
        self.send_text(text)
        # 断言最后一条消息文本
        last_msg = self.driver.find_elements("id", "com.tencent.mm:id/ie9")[-1].text
        assert last_msg == text

    def test_receive_text(self):
        """示例：简单等待对方发来的消息断言出现（需对端自动脚本配合）"""
        self.goto_first_chat()
        old_count = len(self.driver.find_elements("id", "com.tencent.mm:id/ie9"))
        print("Wait for incoming message…")
        time.sleep(5)
        new_msgs = self.driver.find_elements("id", "com.tencent.mm:id/ie9")
        assert len(new_msgs) > old_count, "No new incoming text message detected"