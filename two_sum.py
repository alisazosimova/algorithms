
nums =   [10, 5, 2, 3, 7, 5]
target = 10

def from_internet_sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


def sum_pairs(nums, target):
    seen_elements = {}
    for num1 in nums:
        num2 = target - num1
        if num2 in seen_elements:
            return [num2, num1]
        else:
            seen_elements[num1] = 0


print(sum_pairs(nums, target))

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]
#
assert sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1
assert sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2
assert sum_pairs(l3, -7) == None, "No Match: %s should return None for sum = -7" % l3
assert sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4
assert sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5
assert sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6
assert sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7
assert sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8



#print(sum_pairs0(nums, target))

class Solution:
    def twoSum(self, nums, target):
        print(nums)
        dictionary = {number: index for index, number in enumerate(nums)}
        print(dictionary)
        for key in dictionary:
            print(key)
            key_2 = target - key
            print(key_2)
            if dictionary.get(key_2):
                return [dictionary[key],  dictionary[key_2]]


#nums = [2, 4, 5, 5]
# [4, 8, 7, 3, 15] should return [1, 7] for sum = 8
#First Match From Left REDUX!: [10, 5, 2, 3, 7, 5] should return [3, 7] for sum = 10


# I need to check with right number is farther from list end and choose that pair
def sum_pairs1(nums, target):
    pairs = []
    for n in nums:
        a = target - n
        n_index = nums.index(n)
        if a in nums[n_index+1:]:
            a_index = nums[n_index+1:].index(a) + nums.index(n) +1
            pairs.append([a_index, n_index])
    if pairs:
        pairs.sort()
        i_2, i_1 = pairs[0]
        return [nums[i_1], nums[i_2]]
