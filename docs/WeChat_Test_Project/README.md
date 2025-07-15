# WeChat App Testing Course Project

本项目提供针对 **微信 (WeChat) Android 版** 的系统化测试方案与交付物示例，适用于软件测试课程设计 / 毕业设计。

项目目录结构

```
WeChat_Test_Project/
├── README.md                # 项目总览
├── Test_Plan.md             # 测试设计与方案
├── Manual_Test_Cases.md     # 手工测试用例
├── Automated_Test_Cases.md  # 自动化测试用例说明
├── Test_Report_Template.md  # 测试报告模板
└── scripts/
    └── wechat_tests/
        ├── config.yml       # Appium 启动配置
        └── test_send_receive_text.py  # 自动化脚本示例
```

快速开始
1. 安装依赖 `pip install -r requirements.txt`。
2. 按 `scripts/wechat_tests/config.yml` 配置手机与 WeChat 包名版本。
3. 启动 Appium Server (`appium --log-level info`).
4. 执行示例脚本 `pytest scripts/wechat_tests/`。

> ⚠️ 注意：本仓库不包含微信安装包，请自行在手机或模拟器中预置。

---

若需扩展脚本、增加测试数据或生成 Word/Excel 版本文档，请参考各 Markdown 内的说明并提交 PR/Issue。