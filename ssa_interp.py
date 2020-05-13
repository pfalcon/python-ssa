__all__ = ("__label__", "__phi__")


_last_bblock = None


def __label__(lab):
    global _last_bblock
    _last_bblock = lab


def __phi__(choices):
    global _last_bblock
    return choices[_last_bblock]
