class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        else:
            s_len = len(s)
            print(f's_len = {s_len}')
            for i in range(0, s_len, 2):
                print(i)

