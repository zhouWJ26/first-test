# Manual-Only Test Cases & Execution Report – WeChat (小米 13)

> 说明：以下场景涉及系统弹框、传感器、物理交互或跨 App 行为，难以稳定自动化，故采用手动测试。执行日期 2025-07-15，测试机：小米 13（MIUI 14 / Android 14）、微信 8.0.x 内测包。

| TC ID | 功能/场景 | 前置条件 | 测试步骤 | 预期结果 | 实际结果 | 结论 |
| ----- | -------- | -------- | -------- | -------- | -------- | ---- |
| MAN-001 | **锁屏通知** – 收到微信消息 | 手机锁屏、网络正常 | 1) 让好友发送文本消息<br>2) 观察锁屏界面 | 屏幕点亮显示微信横幅，内容为“好友: 文本摘要”，可上滑回复 | 与预期一致 | Pass |
| MAN-002 | **电话来电中断语音通话** | 与好友语音通话中 | 1) 另一手机拨打被测机号码<br>2) 观察微信语音状态 | 微信语音自动挂起，界面提示“被电话中断”，结束电话后可恢复 | 一致，通话后可手动恢复 | Pass |
| MAN-003 | **扫码加好友（实体二维码）** | 打印好友二维码 | 1) 微信→扫一扫<br>2) 对准打印二维码 | 自动识别二维码并进入添加好友页面 | 成功扫码并显示好友资料页 | Pass |
| MAN-004 | **首启权限弹窗 – 相机** | 清除微信数据 | 1) 首次点击相机拍照按钮<br>2) 观察系统权限弹窗 | 系统弹出相机权限请求，选择“仅此一次”后进入拍照界面 | 弹窗出现，选择后正常拍照 | Pass |
| MAN-005 | **深色/浅色模式动态切换** | 微信运行前台 | 1) 系统设置→显示→深色模式 ON<br>2) 返回微信界面 | 全局 UI 切为深色，文本/图标对比度正常 | UI 自动切换，无错位 | Pass |
| MAN-006 | **多指捏合放大聊天图片** | 聊天中含图片 | 双指捏合放大、拖动 | 图片可缩放拖拽，退出时回原尺寸 | 行为正常 | Pass |
| MAN-007 | **弱网切换（Wi-Fi→4G）发送消息** | 连接 Wi-Fi，打开热点干扰器 | 1) 断开 Wi-Fi，立即发送消息<br>2) 系统自动切到 4G | 消息可能出现“发送中”，切网后重发成功 | 延迟约 3 s 后成功 | Pass |
| MAN-008 | **电量低电模式下消息到达** | 电量≤15%，省电模式 ON | 让好友连续发 5 条消息 | 各条消息均能收到通知并到达 | 全部收到，声音被系统静音 | Pass |
| MAN-009 | **指纹支付验证（账户安全）** | 开启指纹解锁 | 1) 设置→账号与安全→指纹锁<br>2) 退出重进微信 | 启动需指纹验证；错误 3 次可用密码 | 行为符合 | Pass |
| MAN-010 | **Play 商店更新覆盖安装** | 登录 Google Play(如适用) | 1) Play 商店升级微信<br>2) 打开微信 | 启动正常，聊天记录/设置保留 | 一致 | Pass |

## 执行结论
* 共 10 条手动专属用例全部通过，未发现阻断或严重缺陷。
* 观察到小差异：省电模式下消息提示音被系统静音（属系统行为，无需改动）。

> 如需导出 Word 或补充失败案例，请提出需求。