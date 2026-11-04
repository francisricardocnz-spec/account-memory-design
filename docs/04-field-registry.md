# 初始字段目录

这是可评审的33项字段设计目录：21项初始建议开放、12项关闭。enabled_initially表示未来按合同实施的建议，不表示仓库有可用写入器或已经开启服务。主体、类型、性质、敏感规则、确认、用途、期限和版本均需独立验证。

模型只能提出注册字段的候选，不能任意创建JSON路径。字段允许reported不意味着同名字段也允许inferred；reference必须引用有来源的实体，不能字符串化偷换类型。关闭项不能借候选区或用户一次授权绕过。

机器目录见[field-registry.json](../examples/field-registry.json)。每个字段默认不开放匹配、A2A、研究、评测、训练和外部行动。字段变更须版本化，并回归相应合同和删除行为。

| field_id | value.kind | 允许性质 | 初始开关 | 主体/引用限制 |
|---|---|---|---|---|
| `self.reported_experience` | text | reported | 开 | 本人、事件/时间引用 |
| `event.description` | reference | reported,observed | 开 | Event；observed需受信观察 |
| `event.behavior` | reference | reported,observed | 开 | Behavior；不含动机事实化 |
| `state.emotion` | text | reported | 开 | 本人状态 |
| `state.energy` | text | reported | 开 | 本人状态；数字原话不当量表 |
| `state.stress` | text | reported | 开 | 本人状态 |
| `state.attention` | text | reported | 开 | 本人状态 |
| `state.cognitive_load` | text | reported | 开 | 本人状态 |
| `state.position` | text | reported | 开 | 本人当前立场；限定问题 |
| `state.intention` | text | reported | 开 | 本人当前意图；不是已行动 |
| `state.physical_discomfort` | text | reported | 关 | 本人身体不适自述；非诊断 |
| `state.life_context` | text | reported | 开 | 本人生活情境 |
| `state.resources` | text | reported | 开 | 本人本任务可用资源；敏感内容另门控 |
| `preference.communication` | text | reported | 开 | 本人沟通偏好及适用情境 |
| `boundary.explicit` | text | reported | 开 | 本人明确边界 |
| `goal.current` | text | reported | 开 | 本人目标/明确截止 |
| `antigoal.current` | text | reported | 开 | 本人不希望发生的目标 |
| `identity.role` | text | reported | 开 | 本人角色自述 |
| `narrative.segment` | reference | reported,inferred | 关 | NarrativeSegment/有来源Claim |
| `narrative.future_self` | text | reported | 关 | 本人对未来自我的表达；非预测 |
| `narrative.role_conflict` | reference | reported,inferred | 关 | 角色Claim集合及情境；不贴诊断 |
| `relationship.stage` | text | reported | 关 | Relationship+本人视角 |
| `relationship.expectation` | text | reported | 开 | Relationship/关系类型+本人视角 |
| `relationship.agreement` | reference | reported,observed | 关 | 约定对象+各方确认receipt；仅本人报告时标本人视角 |
| `hypothesis.contextual_pattern` | text | inferred | 开 | 明确局部情境/关系，反证引用 |
| `trait.stable_pattern` | text | inferred | 关 | 不自动跨关系推广 |
| `capability.self_evaluation` | text | reported | 开 | 本人能力自述；不造量表分 |
| `assessment.result` | measurement | measured | 关 | 获准Assessment及metric/计分版本 |
| `action.execution` | reference | reported,observed | 关 | Action及真实completion_object |
| `outcome.observation` | reference | reported,observed | 关 | Outcome及观察窗口/来源 |
| `value.user_defined` | text | reported | 开 | 本人明确价值表达；不是隐含动机 |
| `development.framework_view` | reference | inferred | 关 | DevelopmentEpisode与框架权利 |
| `causal.hypothesis` | reference | inferred | 关 | CausalHypothesis，初始状态有限 |

## 开放规则

明确本人自述、偏好、边界和目标可按精确保存动作形成reported记录；必要用途/保留许可仍须成立。当前状态保观察时间和情境，复核建议不能代替事实有效期。局部推断从proposed/inferred起步，支持不足不驱动建议，长期激活需更严格门控。

capability.self_evaluation是本人自评原话，不是能力测量。assessment.result需有权使用的Assessment；稳定特质、发展框架和因果研究保持关闭，默认概率为null。关系期待保本人视角；声称共同约定时需各方相应确认，不将单方描述写进对方账号。
