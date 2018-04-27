def reverse(word):
    n = len(word) - 1
    reverse = ''
    while n >= 0:
        reverse = reverse + word[n]
        n = n - 1
    return reverse

def is_palindrome(word):
    if word == reverse(word):
        return True
    return False
def test(case):
    print(case)

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
