# JSON Config Editor

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
