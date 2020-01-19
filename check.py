from itertools import cycle

l = [1, 2, 3, 4, 5, 6, 7]
step  = 3
def to_pop(l, step):
    if len(l) > 1:
        lcyc = cycle(l)
        for i in range(step):
            to_pop = next(lcyc)
            print(to_pop)
            l.remove(to_pop)
            return to_pop(l, step)
    else:
        print(l)
