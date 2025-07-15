# Automated Test Cases – WeChat (Appium)

> 自动化脚本目录： `scripts/wechat_tests/`
>
> 执行方式： `pytest -v scripts/wechat_tests/`

## 1. 工具与框架
* **Appium 2.x**  – 兼容 UiAutomator2 Driver
* **Python 3.11 + PyTest** – 轻量测试框架
* **allure-pytest** – 测试报告 (可选)
* **OpenAI / ChatGPT** – AI 辅助生成测试数据 (加分项)

## 2. 配置文件 – `config.yml`
```yaml
appium:
  server: http://127.0.0.1:4723/wd/hub
  desired_caps:
    platformName: Android
    deviceName: emulator-5554  # 修改为真机 ID
    appPackage: com.tencent.mm
    appActivity: .ui.LauncherUI
    noReset: true
    automationName: UiAutomator2
```

## 3. 自动化用例列表
| Script | 用例描述 | 相关模块 |
| ------ | -------- | -------- |
| `test_send_receive_text.py::test_send_text` | 发送文本消息并断言显示 | 聊天 |
| `test_send_receive_text.py::test_receive_text` | 模拟 ADB 推送通知，校验收信 | 聊天 |
| `test_contacts.py::test_search_contact` | 搜索联系人结果正确 | 通讯录 |
| `test_moments.py::test_post_text_moment` | 发布朋友圈文本并校验列表 | 发现-朋友圈 |
| `test_favorites.py::test_collect_image` | 收藏图片后在收藏页可见 | 我-收藏 |
| `test_settings.py::test_switch_language` | 切换语言后首页元素文本变化 | 我-设置 |
| `test_performance.py::test_cold_launch_time` | 启动时间 < 3s | 性能 |

> **示例脚本** 请查看 `scripts/wechat_tests/test_send_receive_text.py`，其他脚本结构相同，可按上述列表扩展。所有脚本均支持 `--alluredir` 输出报告。

## 4. CI 集成
```yaml
# .github/workflows/android-appium.yml
name: WeChat UI Tests
on: [push, pull_request]
jobs:
  ui-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Start Appium
        run: |
          npm install -g appium@next
          appium --log-level info &
      - name: Run tests
        run: pytest -v scripts/wechat_tests/ --alluredir=allure-results
```

## 5. AI 辅助 (加分)
* 使用 **ChatGPT** 生成大量随机文本/emoji，自动填充到数据驱动参数化中。
* 结合 **OpenAI Vision** API 做 UI 截图 OCR 断言，减少维护成本。