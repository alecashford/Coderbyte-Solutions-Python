def Palindrome(str): 

    length = (len(str) - 1)
    
    for i in range(length):
        if str[i] != str[length - i]:
            return False
    return True

print Palindrome(raw_input())
