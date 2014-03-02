#Text of challenge: "Have the function LetterCapitalize(str) take the
#str parameter being passed and capitalize the first letter of each
#word. Words will be separated by only one space."


def LetterCapitalize(str):
    
    words = str.split(" ")
    
    caplist = []
    
    for word in words:
        word1 = word[0].capitalize()
        caplist.append(word1 + word[1:])
    
    capped = " ".join(caplist)
    return capped




print LetterCapitalize(raw_input())
