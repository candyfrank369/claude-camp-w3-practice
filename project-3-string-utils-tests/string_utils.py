"""String utility functions: reverse_words, count_vowels, is_palindrome."""


def reverse_words(s):
    """Reverse the order of words in a string.

    Args:
        s: Input string. Words are separated by whitespace.

    Returns:
        A string with the order of words reversed. Empty string if input is empty.

    Raises:
        TypeError: If s is None or not a string.

    Examples:
        >>> reverse_words("hello world")
        'world hello'
        >>> reverse_words("")
        ''
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return " ".join(s.split()[::-1])


def count_vowels(s):
    """Count English vowels (a, e, i, o, u) in a string, case-insensitive.

    Args:
        s: Input string.

    Returns:
        The number of vowel characters in the string. 0 for empty string.

    Raises:
        TypeError: If s is None or not a string.

    Examples:
        >>> count_vowels("Hello")
        2
        >>> count_vowels("")
        0
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return sum(1 for c in s if c.lower() in "aeiou")


def is_palindrome(s):
    """Check if a string is a palindrome, ignoring case and spaces.

    Args:
        s: Input string.

    Returns:
        True if the string reads the same forwards and backwards
        (ignoring case and spaces). True for empty string.

    Raises:
        TypeError: If s is None or not a string.

    Examples:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("")
        True
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
