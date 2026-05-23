"""Unit tests for string_utils."""

import pytest

from string_utils import count_vowels, is_palindrome, reverse_words


class TestReverseWords:
    def test_normal(self):
        assert reverse_words("hello world") == "world hello"

    def test_empty_string(self):
        assert reverse_words("") == ""

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            reverse_words(None)


class TestCountVowels:
    def test_normal(self):
        assert count_vowels("Hello") == 2

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_mixed_case(self):
        assert count_vowels("AEIOUaeiou") == 10

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            count_vowels(None)


class TestIsPalindrome:
    def test_normal(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            is_palindrome(None)
