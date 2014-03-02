#Text of challenge: "Have the function LetterChanges(str) take the str parameter
#being passed and modify it using the following algorithm. Replace every letter
#in the string with the letter following it in the alphabet (ie. c becomes d, z
#becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and
#finally return this modified string."



vowels = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', 'a']

dic = {}
for i in range(0, 26):
    dic[alphabet[i]] = alphabet[i + 1]


def LetterChanges(str):
    
    text = ""    
    for i in str:
        if i in dic:
            i = dic[i]
        text = text + i
    
    text2 = ""
    for i in text:
        if i in vowels:
            i = vowels[i]
        text2 = text2 + i
        
    return text2
    
    
print LetterChanges((raw_input().lower()))
