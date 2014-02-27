def FirstReverse(str):
    str.reverse()
    revd = ''.join(str)
    return revd


print FirstReverse(list(raw_input()))
