def TimeConvert(num): 

    hours = (num / 60)
    min = (num % 60)
    return "%d:%d" % (hours, min)

print TimeConvert(int(raw_input()))
