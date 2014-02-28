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
