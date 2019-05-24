
def reverse_1(string):
    result = ''
    for i in range(1, len(string)+1):
        result = result + string[-i]

    return result

# Using Slice Syntax (https://stackoverflow.com/questions/509211/understanding-slice-notation)
def reverse_2(string):
    return string[::-1]

def reverse_3(string):
    result = ''
    for i in string:
        result = i + result

    return result

# Map reduce solution (https://stackoverflow.com/questions/2682012/how-to-call-same-method-for-a-list-of-objects)
# Trying to do reverse but just training the use of map
def reverse_4(string):
    return ''.join(map(lambda x: x.upper(), list(string)))

print(reverse_1("geeksforgeeks"))
print(reverse_2("geeksforgeeks2"))
print(reverse_3("geeksforgeeks3"))
print(reverse_4("geeksforgeeks4"))