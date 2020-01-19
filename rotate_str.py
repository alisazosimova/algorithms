class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        len_a = len(A)
        a_hash = 0
        b_hash = 0
        alphabet = 256
        h = 1
        if len_a == len(B):
            for i in range(len_a):  # getting hashes
                a_hash =  alphabet *  a_hash + ord(A[i])
                b_hash =  alphabet * b_hash + ord(B[i])
                print(f'a_hash = {a_hash}\nb_hash = {b_hash}')
                if a_hash != b_hash:
                    a_hash = (alphabet * (a_hash - ord(A[i]) * h) + ord(A[len_a-1]))
                else:
                    return True

A = 'abcde'
B = 'bcdea'

#  A = 'abcde', B = 'abced'

a = Solution()
print(a.rotateString(A, B))