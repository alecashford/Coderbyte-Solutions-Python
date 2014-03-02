#Text of challenge: "Take the str parameter being passed and return the string true
#if the characters a and b are separated by exactly 3 places anywhere
#in the string at least once (ie. "lane borrowed" would result in true
#because there is exactly three characters between a and b). Otherwise
#return the string false."


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
