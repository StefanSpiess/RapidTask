import pytest #necessary for pytest-mock even if not used explicitly
from modules.baseclass.BaseClass import BaseClass

def test_initialization_with_kwargs():
    obj = BaseClass(attr1="value1", attr2=42)
    assert obj.get_attribute("attr1") == "value1"
    assert obj.get_attribute("attr2") == 42

def test_get_attribute_existing():
    obj = BaseClass(attr1="value1")
    assert obj.get_attribute("attr1") == "value1"

def test_get_attribute_non_existing():
    obj = BaseClass()
    assert obj.get_attribute("non_existing") is None

def test_set_attribute():
    obj = BaseClass()
    obj.set_attribute("new_attr", "new_value")
    assert obj.get_attribute("new_attr") == "new_value"

def test_has_attribute_existing():
    obj = BaseClass(attr1="value1")
    assert obj.has_attribute("attr1") is True

def test_has_attribute_non_existing():
    obj = BaseClass()
    assert obj.has_attribute("non_existing") is False