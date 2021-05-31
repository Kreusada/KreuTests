from .badattr import BadAttr

# Skipping `__version__` and `version_info` attrs
# using `_version_` as an unsupported type, and 
# `version` as supported.

_version_ = BadAttr
version = "1.0.0"