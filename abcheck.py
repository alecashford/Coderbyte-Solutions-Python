def ABCheck(str):

    for i in range((len(str) - 4)):
        
        if str[i] == "a" and str[i + 4] == "b":
            return True
        elif str[i] == "b" and str[i + 4] == "a":
            return True
        else:
            i += 1
    return False

print ABCheck(raw_input())
