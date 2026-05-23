# Student Data Analysis Practice

## Purpose

Read a student roster CSV and compute totals, country distribution, and bet completion rate, then output a JSON report. The focus is on practicing how to handle "dirty data" — preserving valid fields and transparently reporting data quality issues, rather than blindly discarding rows.

## How to run

```bash
pip install pandas
python csv_student_data_analyzer.py
```

The script reads `students.csv` in the same directory, prints a human-readable summary to the terminal, and writes `report.json`. If `students.csv` is missing, the script prints a notice and exits with code `1`.

### Look up a single student

```bash
python csv_student_data_analyzer.py alice
```

Pass any name (or name fragment) as a positional argument. Matching is **case-insensitive substring**. Multiple matches are all listed; if nothing matches, you get a "not found" message. When a query argument is passed, only the lookup runs — `report.json` is not regenerated.

## report.json field reference

- `total_students` (int): Total student count. Includes rows with dirty fields (since dirty fields don't invalidate the statistic).
- `country_distribution` (dict): Student count per country. Key is the country name, value is the count.
- `bet_completion_rate` (float, 0~1): Completion rate = count of `bet_status == "completed"` / total students, rounded to 4 decimals. Example: `0.3333` means 33.33%.
- `data_quality` (dict): Data quality report, for assessing dirty-row prevalence.
  - `total_rows`: Total rows in the CSV (denominator for the dirty-row ratio).
  - `email_missing`: Number of rows with a missing `email`.
  - `date_unparseable`: Number of rows whose `joined_date` doesn't match `YYYY-MM-DD` and failed parsing.
