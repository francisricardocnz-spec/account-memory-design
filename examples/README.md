# 完全虚构的示例

[memory-lifecycle.json](memory-lifecycle.json)用一句“回复请简短一些。”演示当前自述、待用途授权、明确保存、拒绝旧理解与删除回执。ID、账号、原话、时间、Grant和操作均为虚构，不来自真实个人或运行日志。

这是局部讲解片段，不是完整快照、生产Schema或有效授权凭据。字段目录是设计示例，不会启用任何服务。支持/确认/授权等现实检查必须由未来实现完成。

| 场景 | 应怎样理解 |
|---|---|
| 当前输入 | 可以在本轮尊重明确偏好，但尚未跨会话保存 |
| 内容已确认但缺长期许可 | confirmed不等于获得长期用途；卡片只提示缺授权 |
| 本人明确保存 | 分别记录确认与Grant，合法事务提交后才提示已保存 |
| 本人拒绝一项AI解释并补新说明 | 先停止旧解释；新说明失败也保持停止，不能报完整更正成功 |
| 删除处理中 | blocked/durable表示相应新使用已阻断，物理副本和外部状态另报 |

[capacity-scenario.json](capacity-scenario.json)是合成容量输入；工具只复算公式，不测试吞吐或成本。示例日期固定，读取时不自动变成今天仍有效的许可。

## v0.2新增结构示例

[proposal.json](proposal.json)、[context-bundle.json](context-bundle.json)、[correction-receipt.json](correction-receipt.json)分别是三份Schema的正向讲解片段；包装中的synthetic明确说明全部虚构。

[contract-check-results.json](contract-check-results.json)只记录公开工件的结构检查及边界，不是服务/数据库/真人验收。[cost-scenario.json](cost-scenario.json)使用归一化虚构单位，可运行tools/cost_sensitivity.py比较输入、输出、额外调用和缓存的敏感性。

继续读[完整12轮故事](../docs/deep-dive/02-complete-story.md)，理解这些结构在产品中何时可提交、何时必须保持未知。

## v0.3匿名整理检查记录

[design-integration-check-results.json](design-integration-check-results.json)是离线检查的实际记录，验证105类概念的公开表述、目标33字段政策和相关文件哈希。它本身不是虚构用户数据，也不验证外部原件、外部软件、生产服务或用户收益。
