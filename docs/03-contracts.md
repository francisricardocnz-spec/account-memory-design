# 领域与数据合同

> 本页保留概览；深度阅读：[接口/存储完整说明](deep-dive/03-api-and-storage.md)、[机器合同的边界](deep-dive/10-machine-contracts.md)。

以下是设计合同与示例，不是现成生产Schema。字段和权限必须由服务端校验，不能只依赖提示词。

## 三个分类轴

memory_type面向用户组织：self_report、event、temporary_state、goal、ai_understanding、communication_preference、action_result、relationship_issue。

person_layer组织理解对象：traits、values_motives、identities_narratives、goals_antigoals、capabilities、current_states、relationships、events_behaviors。逻辑存储职责分事件、语义/自述、假设、方法、目标与公共知识；分类不要求复制正文或拆成多个数据库。

`applicability`表示说法在什么主体/情境/时间成立；`usage_scope`表示允许用于账号、人物关系、议题或当前会话。二者还须同时通过目的、接收方与实际Grant检查。

## 对象

| 对象 | 最小内容与约束 |
|---|---|
| Envelope | 不透明ID、服务端owner、schema/revision、记录时间、保留政策、敏感分类、授权及来源引用 |
| Evidence | source_ref/版本/坐标、说话者与被描述者、采集/事件时间、独立组、源谱系、观测方法 |
| Claim | subject/perspective/target、注册field/value、性质、生命周期、内容确认、支持、范围、时间、支持与反证 |
| Memory | Claim/Evidence的受管检索展示载体；停用后不能经Claim旁路重新注入 |
| SourceBinding | 独立最小片段、出处、版本、保留许可、谱系与可删除content_ref |
| ConsentGrant | 实际授权人、目的、字段/记录范围、接收方、起止/撤回、版本与说明版本 |
| Dependency | 父子有类型引用、作用、片段和产生操作；正反向索引，派生图不循环增强证据 |
| Proposal/Confirmation | 类型化操作、对象及控制预期版本；精确确认文本/性质/范围/依据版本 |
| Action/Outcome | 执行阶段、证明依据、完成对象、观察窗、真实来源、未观察项与后续修订 |
| DeletionJob/Ledger | 停止意图、独立持久回执、受管副本清单、分副本清理与恢复覆盖 |

ID不授予权限。引用校验包含类型、owner、版本和当前用途；跨账号对象经单独授权投影引用，不作任意跨租户外键。

## 相互独立的状态

| 轴 | 枚举/含义 |
|---|---|
| epistemic_status | reported / observed / inferred / measured / independently_verified |
| lifecycle | proposed / active / disputed / superseded / retracted / expired / deleted |
| confirmation | unasked / confirmed / rejected |
| support | insufficient / provisional / supported / corroborated |
| save_state | not_requested / awaiting_confirmation / awaiting_grant / processing / committed / failed / stopped |

确认不提高支持或核验地位。长期推断需范围内supported/corroborated、精确内容确认、来源保留和用途许可同时有效；用户一次明确偏好可以按reported处理。稳定模式即使将来采用“3独立事件/14天/2情境”候选门，也只是工程初值，不证明心理规律。

缺门用pending_requirements表达：content_confirmation、candidate_retention_grant、source_retention_grant、long_term_grant、sensitive_grant、support_sufficient。禁用字段、失效来源、版本冲突和配额不足是blocked_reasons，不能提示用户再点确认就能修复。

## 值与时间

value使用text/category/boolean/measurement/reference标签联合。具体字段只接受目录允许的kind；通用类型存在不表示每字段都开放。measurement必须关联合格Assessment和计分版本。概率初始为null，不能把模型信心或量表分当校准概率。

未知值配missing_reason：unknown、not_asked、declined、unobservable、not_applicable、deleted。未知不转0/false，空数组不证明现象不存在。

分别记录事情有效时间valid_time、需要复核review_due_at、存储保留retention_until及Grant期限。复核到期不自动删，事实到期不恢复更旧画像；历史问法仍受今天的授权与删除状态限制。

新原文坐标采用0起始Unicode代码点、左闭右开，并绑定源版本。旧UTF-16协议保留原义，显式转换并回验。规范化文本要另存版本/映射，不悄悄改变定位。

## Action与输出

execution_phase为intended/attempted/completed/cancelled；verification_basis为self_report/tool_receipt/internal_task，另标completion_object。草稿完成不等于外部发送；发送不等于对方接受；无回访是missing。

检索、核权读取、实际纳入请求、回答引用与有效输出各有不同回执。DeliveryCursor可用prepared/dispatched/dispatch_unknown/provider_accepted/output_received/committed/discarded/failed。只有有效输出提交后推进该generation准确覆盖的ID/版本；不按最大序号跳过空洞，不推断模型理解。

## 最小接口提案

| 动作 | 建议接口 | 关键合同 |
|---|---|---|
| 管理列表 | GET /v1/memory/management/entries | keyset分页、逐页核权、coverage与失效cursor |
| 任务上下文 | POST /v1/memory/context | 受信内部宿主、任务/用途/预算、来源版本和遗漏理由 |
| 确认 | POST /v1/memory/proposals/{id}/confirm | 精确确认、选择许可、expected_versions与幂等 |
| 纠正 | POST /v1/memory/corrections | 预览绑定，停用与替代子操作分别回执 |
| 停止/删除 | POST /v1/memory/controls/stops 或 /deletions | 本人控制准入、独立登记与分副本状态 |
| 核对 | GET /v1/memory/operations/{id} | 只读原操作，不重新派发 |

内容写统一expected_versions：model_revision、consent_version、deletion_epoch、objects、schema_version、registry_version、policy_version；revision按十进制字符串传输。缺前置返回428、冲突409，异步202只表示处理/未知。控制退出对明确范围作单调处理，不因无关账号版本变化无限拒绝。
