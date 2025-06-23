import pytest 
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" hello world", "hello world"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected
    

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("    ", ""),
    ("python   ", "python   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sb", [
    ("skypro", "s"),
    ("hello", "l"),
    ("skypro python ", "y"),
])
def test_contains(input_str, input_sb):
    assert  string_utils.contains(input_str, input_sb)

 
@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sb", [
    ("skypro", "a"),
    ("hello", ""),
    ("skypro python ", "po"),
])
def test_contains_negative(input_str, input_sb):
    assert  string_utils.contains(input_str, input_sb) is False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sb, exp", [
    ("skypro", "y", "skpro"),
    ("hello", "l", "heo"),
    ("skypro python", "p", "skyro ython"),
])
def test_delete_symbol(input_str, input_sb, exp):
    assert string_utils.delete_symbol(input_str, input_sb) == exp
    

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sb, exp", [
    ("skypro", "a", "skypro"),
    ("hello", "", "hello"),
    ("skypro python", "p ", "skypro python"),
])
def test_delete_symbol_negative(input_str, input_sb, exp):
    assert string_utils.delete_symbol(input_str, input_sb) == exp
    