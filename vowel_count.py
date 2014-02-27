vowels = ["a", "e", "i", "o", "u"]

vowellist = []

def VowelCount(str):

    for i in str:
        if i in vowels:
            vowellist.append(i)
    
    vowelnum = len(vowellist)
    
    return vowelnum


print VowelCount(raw_input())
