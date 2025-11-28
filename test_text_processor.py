import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    assert processor.capitalize_text("hello") == "HELLO"


def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    assert processor.capitalize_text("world") != "world"


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    reversed_text = processor.reverse_text("abcde")
    assert "edc" in reversed_text
    assert "cba" in reversed_text


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    reversed_text = processor.reverse_text("abcde")
    assert "xyz" not in reversed_text


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    word_count = processor.count_words("This is a test")
    assert isinstance(word_count, int)
    assert isinstance(word_count, str) is False


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    word_count = processor.count_words("One two three four five")
    word_count2 = processor.count_words("One two")
    word_count3 = processor.count_words("One two three four five six seven eight nine ten")
    assert word_count2 < word_count3
    assert word_count3 > word_count
    assert word_count > 3
    assert word_count < 10
    assert word_count >= 5
    assert word_count <= 5


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    assert processor.count_words("") == 0

def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    assert processor.is_palindrome("Anna") is True
    assert processor.is_palindrome("Hello") is False
    assert processor.is_palindrome("Not a palindrome") is not None
    assert processor.is_palindrome("Indul a görög aludni") is True


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    processor = TextProcessor()
    result = processor.remove_spaces("A B C D E")
    assert result == "ABCDE"
    assert " " not in result
    assert len(result) == 5