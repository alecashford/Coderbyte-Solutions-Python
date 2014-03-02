#Text of challenge: "Have the function RunLength(str) take the str parameter being passed and
#return a compressed version of the string using the Run-length encoding algorithm. This
#algorithm works by taking the occurrence of each repeating character and outputting that
#number along with a single character of the repeating sequence. For example: "wwwggopp"
#would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols."


def RunLength(line):
    
    counter = 1
    complist = ""
    length = (len(line) - 1)

    for i in range(length):
        if line[i] == line[i + 1]:
            counter += 1
        elif (line[i] != line[i + 1]):
            complist += str(counter)
            complist += (line[i])
            counter = 1
        elif i > (length):
            complist += str(counter)
            complist += (line[i])
    complist += str(counter)
    complist += (line[length])
    
    return complist

print RunLength(raw_input())
