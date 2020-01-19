class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        else:
            s_len = len(s)
            print(f's_len = {s_len}')
            for i in range(0, s_len, 2):
                print(i)

# A   a
# l s
# i

# # try range(start, stop, step)
# for num in range(0, 10, 2):
#     for i in range(num):
#         print (num, end=" ") #print number
#     # new line after each row to display pattern correctly
#     print()

