#Text of challenge: "Have the function AlphabetSoup(str) take the str
#string parameter being passed and return the string with the letters
#in alphabetical order (ie. hello becomes ehllo). Assume numbers and
#punctuation symbols will not be included in the string."



punct = list( )

def AlphabetSoup(str):

    for line in str:
        if line in punct:
            str = str.replace(line, "")
    
    str.sort()
    
    str = "".join(str)
    
    return str
            
            
print AlphabetSoup(list(raw_input()))
