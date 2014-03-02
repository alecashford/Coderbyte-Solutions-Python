#Have the function TimeConvert(num) take the num parameter being passed
#and return the number of hours and minutes the parameter converts to
#(ie. if num = 63 then the output should be 1:3). Separate the number
#of hours and minutes with a colon."


def TimeConvert(num): 

    hours = (num / 60)
    min = (num % 60)
    return "%d:%d" % (hours, min)

print TimeConvert(int(raw_input()))
