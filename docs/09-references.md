# 技术规范与匿名分析入口

个人附件的作者、原件名、下载地址和项目出处不在公开版列出。其工程机制已重新组织成[匿名综合分析](deep-dive/11-source-integration.md)、[统一术语](../references/UNIFIED-INTERPRETATION.md)与[105类概念对照](../references/FIELD-CROSSWALK.md)，没有附带原文、源代码或原报告。

下面保留机器合同与通用技术的规范入口，用于技术核对；不提供个人文件出处，也不表示有关组织认可本方案。

| 技术规范 | 核对内容 | 边界 |
|---|---|---|
| [JSON Schema Draft 2020-12 core](https://json-schema.org/draft/2020-12/json-schema-core) | 结构化合同、联合值、封闭扩展 | 结构合法不能证明来源真实、同意有效或可激活 |
| [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) | 接口示例固定采用的版本 | 不声称为最新版本或已部署服务 |
| [jsonschema验证文档](https://python-jsonschema.readthedocs.io/en/stable/validate/) | meta验证与显式格式检查 | 不替代服务端业务不变量 |
| [PostgreSQL事务](https://www.postgresql.org/docs/current/tutorial-transactions.html) | 多对象提交与回滚 | 不自动覆盖外部供应商或独立控制域 |
| [PostgreSQL行级安全](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) | 数据库第二层租户隔离 | 不替代用途、来源、队列和对象存储授权 |

本仓库没有复制规范全文，也不会自动下载或执行外部项目。依赖安装按其各自许可。资料匿名处理及公开范围见[说明](../PUBLICATION.md)。
