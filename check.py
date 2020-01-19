# def duplicate_count(text):
#     text = text.lower()
#     array = list(text)
#     counter_list = 0
#     for item in array:
#         for item in text:
#             new = text.replace(item, '')
#             if (len(text) - len(new)) > 1:
#                 counter_list +=1
#                 text = new
#     return counter_list
#
# text = 'aabbccd'*10000
#
# print(duplicate_count(text))
from itertools import cycle

l = [1, 2, 3, 4, 5, 6, 7]
step  = 3
#next_c = next(lcyc)
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

print(to_pop(l, step))