from ssa_interp import __label__, __phi__, __undef__


# Declare all vars appearing in __phi__, as all their params are evaluated
# (unlike abstract model, where only actual execution path is considered).
a2 = __undef__

__label__("l0")
a0 = 0

while True:
    __label__("l1")
    a1 = __phi__({"l0": a0, "l1": a2})
    if not (a1 < 5):
        # This really should be a bblock too.
        break
    # This really should be a bblock too.
    print(a1)
    a2 = a1 + 1
