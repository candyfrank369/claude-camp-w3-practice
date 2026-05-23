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

---

# Config Editor Practice

## Purpose

A small command-line "settings panel" for a JSON config file. Reads `config.json`, lets the user change settings interactively with input validation, and writes results back. Focus: input validation, type coercion (especially the string-to-bool gotcha), and graceful exception handling.

## How to run

```bash
python3 json_file_reader_writer.py
```

The script prints the current config, then loops: prompts for a setting name, prompts for a new value, validates, and saves. Press Enter on the setting prompt — or Ctrl+C — to exit. Multiple settings can be changed in one session.

## config.json fields

| Field | Type | Valid values | Default |
|-------|------|--------------|---------|
| `theme` | string | `light`, `dark` | `light` |
| `language` | string | `en`, `zh`, `ja` | `en` |
| `font_size` | int | integer between 8 and 32 (inclusive) | `14` |
| `notifications_enabled` | bool | `true`, `false` | `true` |

**Input handling:**
- Key names are case-insensitive (`Theme`, `theme`, ` THEME ` all work).
- String enum values (`theme`, `language`) are also case-insensitive.
- Unknown keys are rejected with the list of valid keys printed.
- Invalid values are rejected with the allowed range shown.

**Error handling:**
- Missing `config.json` → friendly message + exit code `1`.
- Malformed JSON in `config.json` → friendly message + exit code `1`.
- Ctrl+C → `Cancelled.` + clean exit (no traceback).
