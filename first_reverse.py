#Text of challenge: "Have the function FirstReverse(str) take the str parameter
#being passed and return the string in reversed order."


def FirstReverse(str):
    str.reverse()
    revd = ''.join(str)
    return revd


print FirstReverse(list(raw_input()))
