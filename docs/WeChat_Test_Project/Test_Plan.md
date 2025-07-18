# Test Plan – WeChat Android App

| 版本 | 作者 | 日期 |
| ---- | ---- | ---- |
| v1.0 | <Your Name> | 2025-07-15 |

---

## 1. 引言

本测试计划旨在阐述针对 **微信 Android 版 v8.x** 的测试活动范围、策略与资源安排，以验证以下模块在指定设备上的功能、性能及稳定性：

* 微信聊天页 (Chat)
* 通讯录 (Contacts)
* 发现 – 朋友圈 (Moments)
* 我 – 收藏 & 设置 (Me – Favorites & Settings)

## 2. 目标
1. 发现并定位上述模块中的功能缺陷、性能瓶颈与兼容性问题。
2. 输出全面覆盖的手动 + 自动化测试用例及执行结果。
3. 形成可复用的自动化脚本，集成到回归流水线。
4. 提交完整、规范的测试报告，为产品质量评估提供依据。

## 3. 范围

| 项 | 说明 |
| --- | --- |
| **测试范围 (IN)** | 功能、UI、易用性、性能 (启动时间、消息收发耗时)、兼容性 (Android 8–14, 多品牌机型) |
| **非测试范围 (OUT)** | 支付、视频号、小程序、公众号、深度 IM 安全加密算法 |

## 4. 参考资料
* 微信官方版本更新日志 & API 文档
* 项目需求说明书 (PRD)
* 课程设计评分细则

## 5. 测试策略

### 5.1 测试类型 & 方法
| 类型 | 目标 | 方法 | 工具 |
| ---- | ---- | ---- | ---- |
| 功能测试 | 验证需求实现正确性 | 手动 + 自动化 | Appium / UIAutomator2 |
| UI 兼容性 | 不同分辨率适配 | 真机遍历、截图对比 | fastlane/screengrab, Galen |
| 性能测试 | 启动 & 关键操作耗时、内存、CPU | 稳态 & 峰值监控 | Android Studio Profiler, PerfDog |
| 稳定性测试 | 长时间Monkey压测 | Monkey, Stall监控 | adb, PerfDog |
| 回归测试 | 版本迭代验证 | CI 触发自动跑脚本 | GitHub Actions + Appium |

### 5.2 进入/退出准则
* **进入**：目标 APK 内测包、需求冻结、测试环境可用。
* **退出**：阻断级缺陷 0；严重缺陷 ≤2 且均有已排修复计划；测试用例通过率 ≥95%。

### 5.3 测试流程
1. 需求分析 & 用例设计
2. 环境搭建 & 账户/数据准备
3. 手动测试执行 & 缺陷提交
4. 自动化脚本编写、调试
5. 回归 & 结果分析
6. 测试报告评审 & 归档

## 6. 环境
| 组件 | 版本 / 规格 |
| ---- | ---------- |
| 手机设备 | 小米 12 (Android 14), 华为 P40 (Android 12)、OPPO R17 (Android 10) |
| 微信 APK | 8.0.x 内测签名包 |
| Appium Server | 2.0+ |
| Python | 3.11 |
| Java (UiAutomator) | 17 |
| CI | GitHub Actions – ubuntu-latest |

## 7. 角色与职责
| 角色 | 成员 | 职责 |
| ---- | ---- | ---- |
| 测试负责人 | 你 | 计划、进度、风险把控 |
| 手动测试 | A 同学 | 用例设计 & 执行 |
| 自动化 | B 同学 | 框架搭建 & 脚本维护 |
| 评审 / 讲师 | 指导老师 | 过程监督、验收 |

## 8. 进度计划 (示例)

| 周次 | 任务 | 产出 |
| --- | --- | --- |
| 第 1 周 | 需求评审、环境搭建 | 需求澄清记录、VM & 真机就绪 |
| 第 2 周 | 用例设计 | 《Manual_Test_Cases.md》v0.9 |
| 第 3 周 | 手动测试执行、缺陷跟踪 | 缺陷单、日报 |
| 第 4 周 | 自动化框架 & 样例脚本 | `scripts/wechat_tests` 初始化 |
| 第 5 周 | 自动化用例补充、CI 集成 | GitHub Actions 工作流 |
| 第 6 周 | 回归 & 性能测试 | 性能报告、脚本优化 |
| 第 7 周 | 输出测试报告 & 课程汇报 | 《Test_Report》v1.0 |

## 9. 风险 & 缓解措施
| 风险 | 影响 | 缓解 |
| ---- | ---- | ---- |
| 真机数量不足 | 兼容性覆盖受限 | 租赁云真机、共享测试机 |
| APK 更新频繁 | 回归压力增加 | 引入 CI 自动跑脚本 |
| Appium 与系统权限冲突 | 用例不稳定 | 统一使用 rooted 模拟器或开启权限 |

## 10. 交付物清单
1. 《Test_Plan.md》
2. 《Manual_Test_Cases.md》
3. 自动化脚本 & 说明
4. CI 配置文件
5. 《Test_Report》

## 11. 审批
| 姓名 | 职位 | 日期 | 同意 |
| ---- | ---- | ---- | ---- |
| 指导老师 | | | ✅ |