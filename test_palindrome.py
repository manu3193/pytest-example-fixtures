import pytest
from palindrome import is_palindrome

def test_is_palindrome_empty_string():
    assert is_palindrome("") == False

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob") == True

def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even") == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?") == True

def test_is_palindrome_date():
    assert is_palindrome("12/02/2021")

def test_is_palindrome_not_palindrome():
    assert is_palindrome("abc") == False

def test_is_palindrome_not_quite():
    assert is_palindrome("abab") == False
