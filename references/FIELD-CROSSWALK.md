# 105类人物概念与33项记忆字段的兼容性对照

本表为匿名综合分析，重新组织概念、目标合同与采用限制，不公开原作者、原件名称、下载入口或原规格。105类概念的存在不表示均适合生产；逐行覆盖不等于逐行采用。

[机器表](field-crosswalk.json)提供概念、输入值类型、目标政策与限制。本表不是105到33的无损转换程序，没有运行外部软件或将数据导入业务。对象名称仅指应单独建模的方向，不代表已实现其完整Schema或数据库。

目标维持[33字段、初始建议21开／12关](../examples/field-registry.json)。字段初始开只表示设计初值；每次使用仍须来源、主体、类型、性质、支持、确认、Grant与版本门。不同系统的active／confirmed不自动继承，关闭项不能靠转换或点击确认开启。

## 处置类别

| 类别 | 概念数 |
|---|---:|
| 关闭扩展 | 23 |
| 条件语义映射 | 26 |
| 保留原话或局部假设 | 5 |
| 独立对象映射 | 8 |
| 对象投影 | 12 |
| 窄化本人自述 | 2 |
| 入口适配后开启 | 3 |
| 敏感专项关闭 | 1 |
| 同名受限映射 | 3 |
| 关系扩展待审 | 14 |
| 关闭研究 | 8 |

- 条件语义映射：仅在具体值符合目标语义时承接，不把推断改称本人自述。
- 对象投影／独立对象：用有来源的Context、NarrativeSegment、GoalContext等承接元数据，不塞进万能Claim字段。
- 保留原话或局部假设：本人说法与AI解释分别存；局部解释不自动变成人格。
- 关闭／待审／入口适配后开启：当前没有直接写入通道，必须另有能力和验收。

所有行automatic_import_allowed=false、adds_public_registry_field=false、implemented=false、manual_approval=null。人工批准未代填。

## 完整105项

| # | 概念标识／名称 | 处置 | 目标字段及初值 | 独立对象方向 | 兼容性限制 |
|---:|---|---|---|---|---|
| 1 | `traits.big_five.openness`／开放性 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 2 | `traits.big_five.conscientiousness`／尽责性 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 3 | `traits.big_five.extraversion`／外向性 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 4 | `traits.big_five.agreeableness`／宜人性 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 5 | `traits.big_five.negative_emotionality`／负性情绪倾向 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 6 | `traits.facets.sociability`／社交性 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 7 | `traits.facets.assertiveness`／果断性 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 8 | `traits.facets.energy_level`／活力 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 9 | `traits.facets.compassion`／同情 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 10 | `traits.facets.respectfulness`／尊重 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 11 | `traits.facets.trust`／信任倾向 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 12 | `traits.facets.organization`／条理 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 13 | `traits.facets.productiveness`／勤勉 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 14 | `traits.facets.responsibility`／责任 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 15 | `traits.facets.anxiety`／焦虑倾向 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 16 | `traits.facets.depression`／低落倾向 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 17 | `traits.facets.emotional_volatility`／情绪波动 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 18 | `traits.facets.intellectual_curiosity`／求知 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 19 | `traits.facets.aesthetic_sensitivity`／审美敏感 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 20 | `traits.facets.creative_imagination`／创造想象 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 21 | `traits.contextual_pattern`／带情境的行为倾向 | 关闭扩展 | `trait.stable_pattern`（关）；`assessment.result`（关） | — | 倾向描述与标准测量分流；两目标均关闭。局部工作假设另用hypothesis.contextual_pattern并保范围，不能借原字段自动写稳定人格。 |
| 22 | `values.self_direction`／自主 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 23 | `values.stimulation`／刺激 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 24 | `values.hedonism`／享乐 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 25 | `values.achievement`／成就 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 26 | `values.power`／权力 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 27 | `values.security`／安全 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 28 | `values.conformity`／遵从 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 29 | `values.tradition`／传统 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 30 | `values.benevolence`／仁爱 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 31 | `values.universalism`／普遍主义 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 32 | `values.custom`／用户自定义价值 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 33 | `needs.autonomy`／自主需要 | 保留原话或局部假设 | `self.reported_experience`（开）；`hypothesis.contextual_pattern`（开） | — | 分开需要与动机；本人原话保持reported，AI解释只能为受限hypothesis；不是新增needs/motives生产命名空间。 |
| 34 | `needs.competence`／胜任需要 | 保留原话或局部假设 | `self.reported_experience`（开）；`hypothesis.contextual_pattern`（开） | — | 分开需要与动机；本人原话保持reported，AI解释只能为受限hypothesis；不是新增needs/motives生产命名空间。 |
| 35 | `needs.relatedness`／联结需要 | 保留原话或局部假设 | `self.reported_experience`（开）；`hypothesis.contextual_pattern`（开） | — | 分开需要与动机；本人原话保持reported，AI解释只能为受限hypothesis；不是新增needs/motives生产命名空间。 |
| 36 | `motives.current`／当前动机 | 保留原话或局部假设 | `self.reported_experience`（开）；`hypothesis.contextual_pattern`（开） | — | 分开需要与动机；本人原话保持reported，AI解释只能为受限hypothesis；不是新增needs/motives生产命名空间。 |
| 37 | `motives.instrumental_role`／工具性动机 | 保留原话或局部假设 | `self.reported_experience`（开）；`hypothesis.contextual_pattern`（开） | — | 分开需要与动机；本人原话保持reported，AI解释只能为受限hypothesis；不是新增needs/motives生产命名空间。 |
| 38 | `values.tradeoff`／价值取舍 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 39 | `values.conflict`／价值冲突 | 条件语义映射 | `value.user_defined`（开） | — | 只接本人明确的文本价值表达，保留原意，不强制Schwartz分类；测量另走关闭的Assessment，隐含取舍不能伪装reported。 |
| 40 | `identity.role`／身份角色 | 条件语义映射 | `identity.role`（开） | — | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 41 | `identity.life_chapter`／人生章节 | 独立对象映射 | `narrative.segment`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 42 | `identity.turning_point`／转折意义 | 独立对象映射 | `narrative.segment`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 43 | `identity.self_interpretation`／自我解释 | 独立对象映射 | `narrative.segment`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 44 | `identity.future_self`／未来自我 | 独立对象映射 | `narrative.future_self`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 45 | `identity.meaning`／意义来源 | 独立对象映射 | `narrative.segment`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 46 | `identity.community`／共同体 | 独立对象映射 | `narrative.segment`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 47 | `identity.belonging`／归属 | 独立对象映射 | `narrative.segment`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 48 | `identity.role_conflict`／角色冲突 | 独立对象映射 | `narrative.role_conflict`（关） | NarrativeSegment | 角色自述可窄化为text；人生章节/意义等通过有来源NarrativeSegment组织，事件与叙事独立版本；不强制归类或积极化。 |
| 49 | `goal.description`／目标 | 条件语义映射 | `goal.current`（开） | — | 目标/反目标/硬边界/沟通偏好分开，来源值类型缩为text；禁止将原boolean/category/reference静默转成相同含义。保存与外部行动分别核权。 |
| 50 | `goal.success_criteria`／成功判据 | 对象投影 | `goal.current`（开） | GoalContext | 成功判据/优先级/约束/依赖/状态进入GoalContext有源投影，goal.current只是目标内容引用，不把这些元数据塞进自由field_id；截止日期不创建提醒。 |
| 51 | `goal.priority`／优先级 | 对象投影 | `goal.current`（开） | GoalContext | 成功判据/优先级/约束/依赖/状态进入GoalContext有源投影，goal.current只是目标内容引用，不把这些元数据塞进自由field_id；截止日期不创建提醒。 |
| 52 | `goal.constraint`／目标约束 | 对象投影 | `goal.current`（开） | GoalContext | 成功判据/优先级/约束/依赖/状态进入GoalContext有源投影，goal.current只是目标内容引用，不把这些元数据塞进自由field_id；截止日期不创建提醒。 |
| 53 | `goal.dependency`／目标依赖 | 对象投影 | `goal.current`（开） | GoalContext | 成功判据/优先级/约束/依赖/状态进入GoalContext有源投影，goal.current只是目标内容引用，不把这些元数据塞进自由field_id；截止日期不创建提醒。 |
| 54 | `goal.status`／目标状态 | 对象投影 | `goal.current`（开） | GoalContext | 成功判据/优先级/约束/依赖/状态进入GoalContext有源投影，goal.current只是目标内容引用，不把这些元数据塞进自由field_id；截止日期不创建提醒。 |
| 55 | `antigoal.description`／反目标 | 条件语义映射 | `antigoal.current`（开） | — | 目标/反目标/硬边界/沟通偏好分开，来源值类型缩为text；禁止将原boolean/category/reference静默转成相同含义。保存与外部行动分别核权。 |
| 56 | `boundary.hard`／硬边界 | 条件语义映射 | `boundary.explicit`（开） | — | 目标/反目标/硬边界/沟通偏好分开，来源值类型缩为text；禁止将原boolean/category/reference静默转成相同含义。保存与外部行动分别核权。 |
| 57 | `preference.communication`／沟通偏好 | 条件语义映射 | `preference.communication`（开） | — | 目标/反目标/硬边界/沟通偏好分开，来源值类型缩为text；禁止将原boolean/category/reference静默转成相同含义。保存与外部行动分别核权。 |
| 58 | `capability.knowledge`／概念知识 | 窄化本人自述 | `capability.self_evaluation`（开） | — | 仅保本人能力/知识自述，不证掌握或稳定会做；任务级能力证据进入CapabilityView。 |
| 59 | `capability.declared_belief`／声明信念 | 窄化本人自述 | `capability.self_evaluation`（开） | — | 仅保本人能力/知识自述，不证掌握或稳定会做；任务级能力证据进入CapabilityView。 |
| 60 | `capability.observed_behavior`／行为表现 | 对象投影 | `event.behavior`（开） | Behavior、CapabilityView | 从合法行为材料构造有版本Behavior引用，observed须受信回执；不凭源字段名升级为实际观测。 |
| 61 | `capability.experience`／经历 | 对象投影 | `event.description`（开） | Event、CapabilityView | 经历先成为性质明确的Event引用，不能仅凭自述次数判技能。 |
| 62 | `capability.demonstrated_skill`／任务技能 | 关闭扩展 | 无直接Claim字段 | CapabilityView | 展示技能的独立表现、支持、难度、失败等通过独立对象处理；无当前可直接生产写入的Claim字段。 |
| 63 | `capability.outcome`／结果 | 入口适配后开启 | `outcome.observation`（关） | Outcome | Outcome须有真实观察窗口/来源，不能将单次结果当稳定能力；当前目标字段仍关闭。 |
| 64 | `state.emotion`／情绪 | 条件语义映射 | `state.emotion`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 65 | `state.stress`／压力 | 条件语义映射 | `state.stress`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 66 | `state.energy`／精力 | 条件语义映射 | `state.energy`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 67 | `state.attention`／注意 | 条件语义映射 | `state.attention`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 68 | `state.cognitive_load`／认知负荷 | 条件语义映射 | `state.cognitive_load`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 69 | `state.stance`／当前立场 | 条件语义映射 | `state.position`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 70 | `state.intention`／意图 | 条件语义映射 | `state.intention`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 71 | `state.physical_self_report`／身体状态自述 | 敏感专项关闭 | `state.physical_discomfort`（关） | — | 源身体状态范围大于目标身体不适，不做等价转换；仅未来获准且确为不适自述时才窄化，目标保持关闭。 |
| 72 | `state.sleep_self_report`／睡眠自述 | 关闭扩展 | 无直接Claim字段 | — | 当前33项没有睡眠结构字段，不借state.energy绕过敏感许可；仅原话本轮处理不获得新长期保存权。 |
| 73 | `state.resources`／可用资源 | 条件语义映射 | `state.resources`（开） | — | 只接受文本自述，保时间与未知，不接原schema的通用category/measurement。 |
| 74 | `relationship.type`／关系类型 | 对象投影 | 无直接Claim字段 | Relationship | 映射已有关系实体类型/视角，不新增relationship.type Claim；各方关系称谓可不同。 |
| 75 | `relationship.stage`／关系阶段 | 同名受限映射 | `relationship.stage`（关） | RelationshipView | 同名不等同值类型/性质相同：目标只接受reported text；源inferred改走合法局部假设，不能直接写同名reported。关系敏感下限至少third_party_restricted。 |
| 76 | `relationship.expectation`／互动期待 | 同名受限映射 | `relationship.expectation`（开） | RelationshipView | 同名不等同值类型/性质相同：目标只接受reported text；源inferred改走合法局部假设，不能直接写同名reported。关系敏感下限至少third_party_restricted。 |
| 77 | `relationship.norm`／已协商规范 | 入口适配后开启 | `relationship.agreement`（关） | RelationshipView | 已协商规范不凭文本当共同同意；构造有各方确认/出处的约定引用；目标保持关闭。 |
| 78 | `relationship.need`／关系需要 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 79 | `relationship.boundary`／关系边界 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 80 | `relationship.trust`／方向性信任 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 81 | `relationship.attraction`／自述吸引 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 82 | `relationship.intimacy`／自述亲近 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 83 | `relationship.commitment`／承诺 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 84 | `relationship.reciprocity`／互惠 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 85 | `relationship.conflict`／冲突 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 86 | `relationship.repair`／修复 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 87 | `relationship.power`／权力结构 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 88 | `relationship.safety`／关系安全 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 89 | `relationship.family_role`／家庭角色 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 90 | `relationship.attachment_anxiety`／关系特异焦虑体验 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 91 | `relationship.attachment_avoidance`／关系特异回避体验 | 关系扩展待审 | 无直接Claim字段 | RelationshipView | 在八维RelationshipView保方向、情境、时间和证据；当前33项没有对应生产field_id，不能藏进任意dimension JSON。权力/安全/依恋体验需更严数据策略。 |
| 92 | `event.description`／事件描述 | 同名受限映射 | `event.description`（开） | Event | 目标值为Event引用，原text/category不能直接粘贴；需来源、发生时间与事件性质，保reported/observed区别。 |
| 93 | `behavior.description`／行为描述 | 对象投影 | `event.behavior`（开） | Behavior | 目标值为Behavior引用；原描述先校验来源/动作/对象，不把摘要当真实工具观测。 |
| 94 | `behavior.status`／行为完成状态 | 入口适配后开启 | `action.execution`（关） | Action | 拆execution_phase与verification_basis、completion_object；不能把draft/confirmed直接当现实完成。 |
| 95 | `development.domain`／领域标签 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 96 | `development.perspective_mode`／视角模式 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 97 | `development.phase`／发展阶段假设 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 98 | `development.integration_gap`／整合证据缺口 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 99 | `development.channel`／持续投入Episode | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 100 | `development.catalyst`／催化事件 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 101 | `development.archetype`／局部摘要 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 102 | `development.metatype`／阶段摘要 | 关闭研究 | `development.framework_view`（关） | DevelopmentEpisode | 领域/视角/阶段/整合缺口/Episode/催化均需受管研究合同。摘要archetype/metatype不回写事实，不自动扩生产字段。 |
| 103 | `context.constraint`／情境约束 | 对象投影 | 无直接Claim字段 | Context | 情境约束/场景角色/资源进入当前Context引用；场景角色不等同身份认同，不凭属性名推断长期价值或财务事实。 |
| 104 | `context.role`／场景角色 | 对象投影 | 无直接Claim字段 | Context | 情境约束/场景角色/资源进入当前Context引用；场景角色不等同身份认同，不凭属性名推断长期价值或财务事实。 |
| 105 | `context.resource`／情境资源 | 对象投影 | 无直接Claim字段 | Context | 情境约束/场景角色/资源进入当前Context引用；场景角色不等同身份认同，不凭属性名推断长期价值或财务事实。 |

## 不能用字段同名掩盖的差异

1. 输入text/category/boolean/measurement可能比目标text更宽，不能全部转字符串后声称兼容。未知不转0或false；测量分不等于概率。
2. `event.description`目标是Event引用；自由文本需要先形成合法、有来源的事件对象。
3. `relationship.expectation`目标仅接本人reported text。对关系的推测不能写进同名reported字段；他人内心不能靠本人叙述得到核验。
4. 一般身体状态的范围大于身体不适；身体不适目标默认关闭，也不是医学诊断字段。
5. 价值偏好只接本人明确表达；理论分类不能伪装成用户原话。能力自述、任务表现和稳定能力证明分开。
6. 关系扩展、发展模型、量表和稳定特质维持独立评审。不能把未采纳维度藏进任意JSON以制造“全覆盖”。
7. 对没有承接的细节记录原因，不追求填满105类概念；任务需要与用户控制优先。
