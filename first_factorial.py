#Text of challenge: "Have the function FirstFactorial(num) take the num parameter being
#passed and return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)).
#For the test cases, the range will be between 1 and 18."


def FirstReverse(str):
    str.reverse()
    revd = ''.join(str)
    return revd


print FirstReverse(list(raw_input()))
