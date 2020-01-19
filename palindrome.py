def is_palindrome_1(word):
    list_from_word = list(word)
    if len(list_from_word) <= 1:
            return True
    else:
        if list_from_word[0] == list_from_word[-1]:
            return is_palindrome(list_from_word[1:-1])
        else:
            return False

def is_palindrome(word):
    list_from_word = [word.lower() for word in list(word)]
    number_of_letters = len(list_from_word) # 5
    if number_of_letters > 1:
        for i in range(int(number_of_letters/2)):
            if list_from_word[i] != list_from_word[number_of_letters - 1 - i]:
                return False
    return True
# Solution from Internet
def is_palindrome2(word):
    return word.lower() == word[::-1].lower()

