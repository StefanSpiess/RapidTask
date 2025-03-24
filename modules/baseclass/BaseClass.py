"""Base class for all classes in the project."""

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