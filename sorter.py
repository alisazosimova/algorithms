import random

a = [10, 9, 7, 1, 4, 2, 6, 5, 3, 8]

b = random.sample(range(100), 20)


def min_max(num1, num2):
    if num1 < num2:
        return num1, num2
    elif num1 > num2:
        return num2, num1
    elif num1 == num2:
        return num2, num1


def compare_result(func):
    def inner(sorted_list):
        result = sorted_list
        second_run = func(sorted_list)
        if result != second_run:
            return inner(second_run)
        elif result == second_run:
            return second_run
    return inner


@compare_result
def looping(shuffled_list):
    num_list = list(shuffled_list)
    length = len(num_list)-1
    for index in range(0, length):
        num1 = num_list[index]
        num2 = num_list[index+1]
        min_num, max_num = min_max(num1, num2)
        print(min_num, max_num)
        num_list[index] = min_num
        num_list[index + 1] = max_num
    return num_list

print(looping(b))
#import ipdb; ipdb.set_trace()