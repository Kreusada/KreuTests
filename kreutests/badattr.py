class BadAttr(type):
    """A class used to represent an unsupported
    type which will be provided to the parser and
    will therefore trigger a rare exception.
    """

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f"<class '{self.__class__.__name__}'>"

    @property
    def __str__(self):
        return self.__repr__