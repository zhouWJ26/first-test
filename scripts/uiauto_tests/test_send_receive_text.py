import pytest, time
from .utils_uia import get_device

d = get_device()

@pytest.fixture(scope="module", autouse=True)
def prepare_chat():
    """打开微信并进入最近聊天首个会话"""
    d.app_start("com.tencent.mm")
    # 点击底栏“微信”（可能已在首页）
    if d(text="微信").exists(timeout=2):
        d(text="微信").click_exists()
    # 进入第一个聊天会话
    d(resourceId="com.tencent.mm:id/bhp").click_exists()
    yield
    d.app_stop("com.tencent.mm")

def send_text(msg: str):
    d(resourceId="com.tencent.mm:id/bsb").set_text(msg)
    d(resourceId="com.tencent.mm:id/bw_").click_exists()

def last_msg_text():
    items = d(resourceId="com.tencent.mm:id/ie9").all()
    return items[-1].get_text() if items else None


def test_send_text():
    txt = f"uia_{int(time.time())}"
    send_text(txt)
    assert last_msg_text() == txt


def test_receive_text():
    """等待对端把消息发过来"""
    before = len(d(resourceId="com.tencent.mm:id/ie9"))
    time.sleep(5)
    after = len(d(resourceId="com.tencent.mm:id/ie9"))
    assert after > before, "未检测到新消息"