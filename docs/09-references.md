# 参考入口与采用边界

以下提供公开规范和原型入口，便于读者自行核对。它们各自版本与许可独立；本仓库没有镜像其完整源码、附件或作者规格，也不声称作者认可本设计。

| 公开来源 | 可参考的问题 | 本项目的边界 |
|---|---|---|
| [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12) | 结构化合同、联合值与封闭扩展 | 结构合法不能证明来源真实、同意有效或状态可激活 |
| [PostgreSQL事务](https://www.postgresql.org/docs/current/tutorial-transactions.html) | 多对象提交与回滚 | 业务事务不自动覆盖外部供应商或独立控制域 |
| [PostgreSQL行级安全](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) | 数据库第二层租户隔离 | 不替代服务端用途、来源、对象存储与队列授权 |
| [pgvector](https://github.com/pgvector/pgvector) | 可选向量召回与存储测量 | 向量结果不是权威，相关性不授予权限 |
| [dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | Agent原型的研究入口 | 仅作公开研究入口，不据此宣称已采用、跑通或获得源码许可 |
| [dsh-identity](https://github.com/Anarrogantcat/dsh-identity) | 身份/记忆/接续原型的设计研究 | 单机文件和游标不直接等价生产多实例或交付证明 |
| [dsh-mem-weave](https://github.com/QuaonY/dsh-mem-weave) | 分层记忆与组织机制的原型研究 | 不把原型安装或字段存在视为效果验证 |
| [Stemem](https://github.com/JOJO-Adam/Stemem) | 状态、装配与表达机制的原型研究 | AI角色状态不作为用户心理事实或证据 |

未确认可公开再分发权利的原始私人材料不随仓库发布。引用外部工作不表示把通用工程机制据为独有原创；具体文章、作者规格或实现如进一步采用，应补精确版本、适用范围和许可核对。

这些链接是来源入口，不提供最新版本、功能或价格承诺。发布版工具不访问这些网站，不会下载或执行第三方代码。

## v0.2机器工件的规范入口

- [JSON Schema Draft 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core)：本版结构示例采用的方言。
- [jsonschema验证文档](https://python-jsonschema.readthedocs.io/en/stable/validate/)：meta验证、显式格式检查及其职责边界。
- [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html)：本版接口示例固定采用的版本，不声称是最新版本。

本仓库没有复制这些规范全文；依赖安装遵循各自许可，工件只是可审阅的示例。
