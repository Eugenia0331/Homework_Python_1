import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# ---------- capitalize ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("zZz", "Zzz"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),   # первая не буква
    ("", ""),               # пустая строка
    ("   ", "   "),         # только пробелы
    ("!test", "!test"),     # начинается с символа
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ---------- trim ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("      hello", "hello"),
    ("world", "world"),      # без пробелов
    (" sky pro", "sky pro"), # пробел только в начале
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                # пустая строка
    ("   ", ""),             # только пробелы
    ("\ttext", "\ttext"),    # табуляция не убирается
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ---------- contains ----------
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"),
    ("SkyPro", "P"),
    ("12345", "3"),
    ("hello", "e"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "U"),
    ("", "a"),
    ("12345", "9"),
    ("test", " "),
])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False


# ---------- delete_symbol ----------
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", " ", "helloworld"),
    ("banana", "a", "bnn"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),  # символа нет
    ("", "a", ""),              # пустая строка
    ("test", "", "test"),       # пустой символ
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

