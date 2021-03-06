__all__ = ("__label__", "__phi__", "__undef__")


class Undef:
    def __repr__(self):
        return "__undef__"


__undef__ = Undef()


_prelast_bblock = None
_last_bblock = None


def __label__(lab):
    global _prelast_bblock, _last_bblock
    _prelast_bblock = _last_bblock
    _last_bblock = lab


def __phi__(choices):
    global _prelast_bblock
    return choices[_prelast_bblock]
