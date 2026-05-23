# 学员数据分析练习

## 项目目的

读取学员名单 CSV，统计总人数、各国分布、对赌完成率，输出 JSON 报告。重点是练习面对"脏数据"时的处理思路——保留有效字段、如实暴露数据质量问题，而不是一刀切丢弃。

## 怎么运行

```bash
pip install pandas
python analyzer.py
```

脚本会读取同目录下的 `students.csv`，在终端打印一份人类可读的摘要，并生成 `report.json`。如果 `students.csv` 不存在，脚本会打印提示并以退出码 `1` 异常退出。

### 查询单个学员

```bash
python analyzer.py alice
```

直接在命令行后接姓名（或姓名片段）即可，按**子串匹配、不区分大小写**。命中多人会全部列出，没命中会提示"没找到"。注意：带查询参数时只做查询、不会生成 `report.json`。

## report.json 字段说明

- `total_students` (int)：学员总数。包含含脏数据的行（脏字段不影响统计有效性时不丢弃）。
- `country_distribution` (dict)：各国学员数。key 是国家名，value 是该国学员数。
- `bet_completion_rate` (float, 0~1)：对赌完成率 = `bet_status == "completed"` 的人数 / 总人数，保留 4 位小数。例：`0.3333` 表示 33.33%。
- `data_quality` (dict)：数据质量报告，便于评估"脏数据占比"。
  - `total_rows`：CSV 总行数（脏数据占比的分母参照）。
  - `email_missing`：`email` 字段缺失的行数。
  - `date_unparseable`：`joined_date` 不符合 `YYYY-MM-DD` 格式、解析失败的行数。
