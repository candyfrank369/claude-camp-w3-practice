# String Utils with Unit Tests

## Purpose

A small string utility library that exposes three functions:

- `reverse_words(s)` — reverse the order of words in a string.
- `count_vowels(s)` — count English vowels (`a`, `e`, `i`, `o`, `u`) in a string, case-insensitive.
- `is_palindrome(s)` — check whether a string is a palindrome, ignoring case and spaces.

The project also demonstrates how to write unit tests for Python functions with `pytest`, covering the normal path, edge cases (empty strings, mixed case), and error cases (`TypeError` on non-string input).

## Install pytest

```bash
pip install pytest
```

If your system has both Python 2 and Python 3 installed, use:

```bash
pip3 install pytest
```

## Run the tests

From this project directory:

```bash
pytest -v
```

The `-v` flag prints each test case name and its result.

## Behavior notes

- All three functions raise `TypeError` when passed `None` or any non-string value.
- Empty-string handling: `reverse_words("")` returns `""`, `count_vowels("")` returns `0`, `is_palindrome("")` returns `True`.
