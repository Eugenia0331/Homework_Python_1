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
    (None, None),           # None
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
    (None, None),            # None
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
    (None, "a"),
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
    (" ", " ", ""),             # строка из пробела
    (None, "a", None),          # None вместо строки
    ([], "a", []),              # пустой список (если метод принимает список)
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# ---------- starts_with ----------
@pytest.mark.positive
@pytest.mark.parametrize("string, prefix", [
    ("SkyPro", "S"),
    ("hello world", "hello"),
    ("12345", "123"),
])
def test_starts_with_positive(string, prefix):
    assert string_utils.starts_with(string, prefix) is True


@pytest.mark.negative
@pytest.mark.parametrize("string, prefix", [
    ("SkyPro", "sky"),     # регистр не совпадает
    ("", "a"),             # пустая строка
    (" test", "t"),        # пробел перед текстом
    (None, "S"),           # None вместо строки
])
def test_starts_with_negative(string, prefix):
    assert string_utils.starts_with(string, prefix) is False


# ---------- to_list ----------
@pytest.mark.positive
@pytest.mark.parametrize("string, delimiter, expected", [
    ("apple,banana,orange", ",", ["apple", "banana", "orange"]),
    ("1;2;3", ";", ["1", "2", "3"]),
    ("тест строка", " ", ["тест", "строка"]),
    ("04 апреля 2023", " ", ["04", "апреля", "2023"]),
])
def test_to_list_positive(string, delimiter, expected):
    assert string_utils.to_list(string, delimiter) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, delimiter, expected", [
    ("", ",", []),          # пустая строка
    (None, ",", None),      # None
    (" ", ",", [" "]),      # строка только из пробела
])
def test_to_list_negative(string, delimiter, expected):
    assert string_utils.to_list(string, delimiter) == expected
