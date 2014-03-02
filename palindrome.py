#Text of challenge: "Have the function Palindrome(str) take the str parameter being
#passed and return the string true if the parameter is a palindrome, (the string is
#the same forward as it is backward) otherwise return the string false. For example:
#"racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string."

def Palindrome(str): 

    length = (len(str) - 1)
    
    for i in range(length):
        if str[i] != str[length - i]:
            return False
    return True

print Palindrome(raw_input())
