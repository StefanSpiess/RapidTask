"""
BaseClass
---------

A generic base class designed to provide fundamental methods for managing attributes dynamically. 
This class allows for flexible initialization and manipulation of attributes, making it suitable 
for use as a foundational class in various projects.

Attributes:
    None explicitly defined. Attributes can be dynamically added during initialization or runtime.

Methods:
    __init__(**kwargs):
        Initializes the object with attributes provided as keyword arguments. Each key-value pair 
        in `kwargs` is set as an attribute of the object.

    get_attribute(attr_name):
        Retrieves the value of the specified attribute. If the attribute does not exist, 
        it returns `None`.

    set_attribute(attr_name, value):
        Sets the value of the specified attribute. If the attribute does not exist, it will 
        be created dynamically.

    has_attribute(attr_name):
        Checks whether the object has a specific attribute. Returns `True` if the attribute 
        exists, otherwise `False`.
"""

class BaseClass:
    """Generic base class providing fundamental methods such as getters and setters."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_attribute(self, attr_name):
        """Get the value of an attribute if it exists, else return None."""
        return getattr(self, attr_name, None)

    def set_attribute(self, attr_name, value):
        """Set the value of an attribute."""
        setattr(self, attr_name, value)

    def has_attribute(self, attr_name):
        """Check if the object has a specific attribute."""
        return hasattr(self, attr_name)