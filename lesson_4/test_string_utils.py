import pytest
from string_utils import StringUtils

# Тесты для метода capitilize
def test_capitilize():
    util = StringUtils()
    assert util.capitilize("skypro") == "Skypro"
    assert util.capitilize("SkyPro") == "Skypro"
    assert util.capitilize("") == ""

# Тесты для метода trim
def test_trim():
    util = StringUtils()
    assert util.trim(" skypro") == "skypro"
    assert util.trim("skypro ") == "skypro"
    assert util.trim("  skypro  ") == "skypro"

# Тесты для метода to_list
def test_to_list():
    util = StringUtils()
    assert util.to_list("a,b,c") == ["a", "b", "c"]
    assert util.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert util.to_list("") == []

# Тесты для метода contains
def test_contains():
    util = StringUtils()
    assert util.contains("SkyPro", "S") == True
    assert util.contains("SkyPro", "U") == False

# Тесты для метода delete_symbol
def test_delete_symbol():
    util = StringUtils()
    assert util.delete_symbol("SkyPro", "k") == "SyPro"
    assert util.delete_symbol("SkyPro", "Pro") == "Sky"
    assert util.delete_symbol("SkyPro", "x") == "SkyPro"

# Тесты для метода starts_with
def test_starts_with():
    util = StringUtils()
    assert util.starts_with("SkyPro", "S") == True
    assert util.starts_with("SkyPro", "P") == False

# Тесты для метода end_with
def test_end_with():
    util = StringUtils()
    assert util.end_with("SkyPro", "o") == True
    assert util.end_with("SkyPro", "y") == False

# Тесты для метода is_empty
def test_is_empty():
    util = StringUtils()
    assert util.is_empty("") == True
    assert util.is_empty(" ") == True
    assert util.is_empty("SkyPro") == False

# Тесты для метода list_to_string
def test_list_to_string():
    util = StringUtils()
    assert util.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert util.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert util.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert util.list_to_string([]) == ""

# Негативные тесты
def test_invalid_inputs():
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.capitilize(None)
    with pytest.raises(AttributeError):
        util.trim(None)
    with pytest.raises(AttributeError):
        util.to_list(None)
    with pytest.raises(AttributeError):
        util.contains(None, "S")
    with pytest.raises(AttributeError):
        util.delete_symbol(None, "k")
    with pytest.raises(AttributeError):
        util.starts_with(None, "S")
    with pytest.raises(AttributeError):
        util.end_with(None, "o")
    with pytest.raises(AttributeError):
        util.is_empty(None)
    with pytest.raises(AttributeError):
        util.list_to_string(None)