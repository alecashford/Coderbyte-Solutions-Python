punct = list( )

def AlphabetSoup(str):

    for line in str:
        if line in punct:
            str = str.replace(line, "")
    
    str.sort()
    
    str = "".join(str)
    
    return str
            
            
print AlphabetSoup(list(raw_input()))
