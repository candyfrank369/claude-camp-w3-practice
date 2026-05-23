# CLI editor for config.json: prompt user to change settings, validate, write back.

import json
import sys

CONFIG_PATH = "config.json"
VALID_KEYS = ("theme", "language", "font_size", "notifications_enabled")


def load_config(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"Error: {path} not found.")
    except json.JSONDecodeError as e:
        sys.exit(f"Error: {path} is not valid JSON ({e.msg}).")


def save_config(path, cfg):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)


def print_config(cfg):
    print("\nCurrent settings:")
    for k, v in cfg.items():
        print(f"  {k} = {v!r}")


def normalize_key(raw):
    k = raw.strip().lower()
    if k not in VALID_KEYS:
        raise ValueError(f"unknown key '{raw.strip()}'. Valid keys: {', '.join(VALID_KEYS)}")
    return k


def parse_value(key, raw):
    v = raw.strip().lower()
    if key == "theme":
        if v in ("light", "dark"): return v
        raise ValueError("theme must be 'light' or 'dark'")
    if key == "language":
        if v in ("en", "zh", "ja"): return v
        raise ValueError("language must be one of: en, zh, ja")
    if key == "font_size":
        if v.isdigit() and 8 <= int(v) <= 32: return int(v)
        raise ValueError("font_size must be an integer between 8 and 32")
    if v == "true": return True
    if v == "false": return False
    raise ValueError("notifications_enabled must be 'true' or 'false'")


def edit_loop(cfg):
    while True:
        print_config(cfg)
        raw_key = input("\nWhich setting to change? (Enter to exit): ").strip()
        if not raw_key:
            print("Exiting.")
            return
        try:
            key = normalize_key(raw_key)
            cfg[key] = parse_value(key, input(f"New value for {key}: "))
        except ValueError as e:
            print(f"Error: {e}")
            continue
        save_config(CONFIG_PATH, cfg)
        print("Setting updated.")


def main():
    try:
        edit_loop(load_config(CONFIG_PATH))
    except KeyboardInterrupt:
        print("\nCancelled.")


if __name__ == "__main__":
    main()
