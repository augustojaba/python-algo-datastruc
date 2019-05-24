

def isPalindrome(string):
    i = 0
    j = len(string) -1

    while i <= j:
        if string[i] != string[j]:
            return False;
        else:
            i += 1
            j -= 1

    return True

def isPalindrome2(string):
    return string == ''.join(reversed(string))


def isPalindromeNumber(number):
    sign = number < 0

    if sign:
        number *= -1

    return str(number) == ''.join(reversed(str(number)))


print(isPalindrome('aaaaa'))
print(isPalindrome2('abba'))
print(isPalindrome2('abbabba'))
print(isPalindrome2('abbabbbba'))
print(isPalindromeNumber(454))
print(isPalindromeNumber(-454))
print(isPalindromeNumber(453))
print(isPalindromeNumber(0))


