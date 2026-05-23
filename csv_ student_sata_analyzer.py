# 读取 students.csv，统计学员总数 / 各国分布 / 对赌完成率，输出 report.json。
# 也支持按姓名查询单个学员：python "CSV Student Data Analyzer.py" <姓名片段>

import json
import sys
import pandas as pd

CSV_PATH = "students.csv"
REPORT_PATH = "report.json"


def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"文件没找到: {path}")
        sys.exit(1)


def compute_stats(df):
    total = int(len(df))
    completed = int((df["bet_status"] == "completed").sum())
    parsed = pd.to_datetime(df["joined_date"], format="%Y-%m-%d", errors="coerce")
    return {
        "total_students": total,
        "country_distribution": {k: int(v) for k, v in df["country"].value_counts().items()},
        "bet_completion_rate": round(completed / total, 4) if total else 0.0,
        "data_quality": {
            "total_rows": total,
            "email_missing": int(df["email"].isna().sum()),
            "date_unparseable": int(parsed.isna().sum()),
        },
    }


def find_student(df, query):
    matches = df[df["name"].str.contains(query, case=False, na=False)]
    if matches.empty:
        print(f"没找到匹配 '{query}' 的学员")
        return
    print(f"找到 {len(matches)} 条匹配：")
    for _, row in matches.iterrows():
        email = row["email"] if pd.notna(row["email"]) else "(缺失)"
        print("-" * 40)
        print(f"姓名: {row['name']}  邮箱: {email}")
        print(f"加入: {row['joined_date']}  国家: {row['country']}  对赌: {row['bet_status']}")


def print_summary(r):
    dq = r["data_quality"]
    countries = ", ".join(f"{k}={v}" for k, v in r["country_distribution"].items())
    print("=" * 40)
    print(f"总学员数: {r['total_students']}")
    print(f"各国分布: {countries}")
    print(f"对赌完成率: {r['bet_completion_rate'] * 100:.2f}%")
    print(f"数据质量: 总行数={dq['total_rows']}, email缺失={dq['email_missing']}, 日期异常={dq['date_unparseable']}")
    print("=" * 40)


def main():
    df = load_data(CSV_PATH)
    if len(sys.argv) >= 2:
        find_student(df, sys.argv[1])
        return
    report = compute_stats(df)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print_summary(report)


if __name__ == "__main__":
    main()
