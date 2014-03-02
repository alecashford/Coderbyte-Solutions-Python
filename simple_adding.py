#Text of challenge: "Have the function SimpleAdding(num) add up all the
#numbers from 1 to num. For the test cases, the parameter num will be
#any number from 1 to 1000."


def SimpleAdding(num):
    a = range((num + 1))
    total = sum(a)    
    return total

print SimpleAdding(int(raw_input()))
