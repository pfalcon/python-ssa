from ssa_interp import __label__, __phi__, __undef__


__label__("l0")
# All vars should be initialized
x0 = x1 = __undef__

a0 = 0

if a0:
    __label__("l1")
    x0 = 1
else:
    __label__("l2")
    x1 = 2

__label__("l3")
x2 = __phi__({"l1": x0, "l2": x1})
print(x2)
