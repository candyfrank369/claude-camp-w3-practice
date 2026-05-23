# Read students.csv, compute totals / country distribution / bet completion rate, write report.json.
# Also supports looking up a student by name: python analyzer.py <name_fragment>

import json
import sys
import pandas as pd

CSV_PATH = "students.csv"
REPORT_PATH = "report.json"


def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
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
        print(f"No student found matching '{query}'")
        return
    print(f"Found {len(matches)} match(es):")
    for _, row in matches.iterrows():
        email = row["email"] if pd.notna(row["email"]) else "(missing)"
        print("-" * 40)
        print(f"Name: {row['name']}  Email: {email}")
        print(f"Joined: {row['joined_date']}  Country: {row['country']}  Status: {row['bet_status']}")


def print_summary(r):
    dq = r["data_quality"]
    countries = ", ".join(f"{k}={v}" for k, v in r["country_distribution"].items())
    print("=" * 40)
    print(f"Total students: {r['total_students']}")
    print(f"Country distribution: {countries}")
    print(f"Bet completion rate: {r['bet_completion_rate'] * 100:.2f}%")
    print(f"Data quality: total_rows={dq['total_rows']}, email_missing={dq['email_missing']}, date_unparseable={dq['date_unparseable']}")
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
