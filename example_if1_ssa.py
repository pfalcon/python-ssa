from ssa_interp import __label__, __phi__


__label__("l0")
# All vars should be initialized
x0 = x1 = None

a0 = 0

if a0:
    __label__("l1")
    x0 = 1
else:
    __label__("l2")
    x1 = 2

# Crucial point - __phi__'s really should be first "instructions" of
# the basic block, even before a label.
x2 = __phi__({"l1": x0, "l2": x1})
__label__("l3")
print(x2)
