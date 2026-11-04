# 机器示例怎样使用，哪里不能据此下结论

## 本版提供的工件

| 工件 | 限定范围 |
|---|---|
| [proposal.schema.json](../../schemas/proposal.schema.json) | 非受信模型抽取的结构子集；只允许初始21字段、reported/inferred候选、有限源handle与原话 |
| [context-bundle.schema.json](../../schemas/context-bundle.schema.json) | 受信宿主应产生的五段bundle形状、来源绑定与计量元数据 |
| [correction-receipt.schema.json](../../schemas/correction-receipt.schema.json) | 停用与替代分项回执的一部分结构约束 |
| [OpenAPI](../../api/openapi.json) / [操作清单](../../api/operations.json) | 9个接口、请求/响应、版本及错误的评审示例 |
| [检查脚本](../../tools/check_contract_examples.py) | 3份Schema meta检查、样例/反例、接口清单与本地引用核对 |

这些是本公开版新整理的结构示例，不是任何第三方完整工程包、业务服务或生产迁移的再发布。完整33字段目录保留12关闭项，不因Schema出现而启用；提案Schema的21字段子集也不代表每一合法形状都允许持久保存。

## 运行离线检查

建议Python3.10或更新版本；先建立独立虚拟环境，避免改变产品环境。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -B tools/check_contract_examples.py
```

基础文档检查和容量工具只需标准库；此处可选开发依赖用于JSON Schema Draft 2020-12与format检查。Windows可使用虚拟环境中的对应Python路径。

OpenAPI当前检查操作清单、必需响应与本地引用，不声称完成所有OpenAPI规范规则认证，更没有与真实服务端逐路由匹配。服务器地址是不可用于生产的example.invalid。

## 三层拒绝

| 检查层 | 例子 | 本仓库是否执行 |
|---|---|---|
| 结构 | 未注册字段、错误value.kind、额外owner/active、超长、非法日期、缺五段 | 执行结构样例检查 |
| 运行权威 | handle实际归属/许可、原文回读、现在已撤回、scope、当前预算、独立登记是否真持久 | 只有设计，未来服务必须实施 |
| 语义与效用 | 原话是否真正支持提案、反例是否充分、下一轮是否有帮助 | 需真实模型与独立人工/用户证据 |

例如，一个形状合法的source_handle可能不存在或已撤回；Schema无法回读数据库。support=insufficient的局部提案在结构上可被表示，宿主仍须禁止用它驱动个性化建议。token元数据是合法整数，也不证明完整wire在预算内或供应商收费正确。

## 四个刻意保留的边界样例

| 检查ID | 结构会怎样 | 还需什么 |
|---|---|---|
| P13 等长但不同的原话 | 形状合法 | 回读真实源版本、校验坐标/原话和当前许可 |
| P14 支持不足的局部假设 | 形状合法 | 使用阶段支持门，禁止不足支持驱动建议或长期激活 |
| C03 完整输入加预留超过窗口 | 各字段形状合法 | 宿主核真实总量/误差界/模型限制 |
| C04 旧许可版本 | 版本字符串合法 | 查询当前权威水位，不能让旧bundle自证合法 |

这些不是“攻击通过率”或产品质量分数，而是说明结构校验的职责边界。报告里runtime_check_still_required=true的样例仍需要后续实现检查。

## 一次实际检查中暴露的问题

初次只安装基础jsonschema包时，非法日期样例P12被接受：代码虽然传了FormatChecker，但对应可选日期检查依赖没有安装。修正为带format-nongpl的开发依赖，并在脚本入口显式检查date-time checker存在；没有时直接拒绝运行，避免悄悄放行。

这说明“写了format=date-time”“调用了一个验证器”和“当前环境实际执行该断言”仍是不同证据。修正前的失败保留在本地修订记录，公开[结构检查结果](../../examples/contract-check-results.json)只陈述当前工件的检查范围，未覆盖生产数据库、真实同意或真人效果。

## 对未来实现的约束

- 人类命令与模型提案分离；模型不授owner、Grant、确认、独立核验或执行成功。
- 确认继承服务端已展示提案的精确文本/性质/范围；要扩大范围先生成新预览，不在confirm body里偷偷改。
- 结构错误拒相应提案，正常当前回答可独立处理；不能修复成另一条用户未确认的事实后报成功。
- API错误不回显私密payload；操作回读核当前性，不恢复已删正文或自动重派。
- 内容替代与独立停止分项处理，API中blocked要求durable只是结构一致性，真实持久证据仍由宿主验证。

相关规范入口：[JSON Schema](https://json-schema.org/draft/2020-12/json-schema-core)、[jsonschema验证文档](https://python-jsonschema.readthedocs.io/en/stable/validate/)、[OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html)。本仓库固定此示例版本，不声称使用最新规范或所有实现都兼容。
