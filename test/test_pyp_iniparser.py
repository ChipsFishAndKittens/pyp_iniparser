"""
test_pyp_iniparser.py

Test cases for PYP_Iniparser class


"""


from unittest.mock import mock_open, patch
import sys

sys.path.append("..")

from pyp_iniparser import PYP_Iniparser


def test_read_successful():
    iniparser = PYP_Iniparser()
    with patch("builtins.open", mock_open(read_data="line1\nline2\nline3")):
        result = iniparser._read("dummy_filename.ini")
    assert result is True
    assert iniparser._lines == ["line1", "line2", "line3"]


def test_read_unsuccessful():
    iniparser = PYP_Iniparser()
    with patch("builtins.open", side_effect=IOError("File not found")):
        result = iniparser._read("nonexistent_file.ini")
    assert result is False
    assert iniparser._lines == []


def test_parse_data():
    iniparser = PYP_Iniparser()
    with patch.object(iniparser, "_read", return_value=True):
        iniparser._lines = [
            "key1 = value1",
            "key2 = value2",
            "key3 = value3",
            "key1/value1",
            "random line",
            "other line",
            "key4=values=with=many=equal=signs",
            "pi=  3.14",
            "int = 10",
            "bool =false",
            "10=20 10",
        ]
        result = iniparser.parse("dummy_filename.ini")

    assert result is True
    assert iniparser.data == {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "values=with=many=equal=signs",
        "pi": "3.14",
        "int": "10",
        "bool": "false",
    }


def test_parse_data_strict():
    iniparser = PYP_Iniparser()
    with patch.object(iniparser, "_read", return_value=True):
        iniparser._lines = [
            "key1 = value1",
            "key2 = value2",
            "key3 = value3",
            "key1/value1",
            "random line",
            "other line",
            " ignored line=",
            "key4=values=with=many=equal=signs",
            "pi=  3.14",
            "int = 10",
            "bool =false",
            "10=20 10",
            "!some=value will be ignored",
        ]
        result = iniparser.parse("dummy_filename.ini", True)

    assert result is True
    assert iniparser.data == {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "values=with=many=equal=signs",
        "pi": 3.14,
        "int": 10,
        "bool": False,
    }
