class Solution:
    def reverseWords(self, s):
        list_from_words = s.split(' ')
        reversed_list = [n[::-1] for n in list_from_words]
        return ' '.join(reversed_list)


