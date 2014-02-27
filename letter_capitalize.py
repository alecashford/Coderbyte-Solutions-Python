def LetterCapitalize(str):
    
    words = str.split(" ")
    
    caplist = []
    
    for word in words:
        word1 = word[0].capitalize()
        caplist.append(word1 + word[1:])
    
    capped = " ".join(caplist)
    return capped




print LetterCapitalize(raw_input())
