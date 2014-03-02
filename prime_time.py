#Text of challenge: "Have the function PrimeTime(num) take the num parameter
#being passed and return the string true if the parameter is a prime number,
#otherwise return the string false. The range will be between 1 and 2^16."


def PrimeTime(num):
    
    numrange = range(num)
    
    del numrange[0:2]
    
    for i in numrange:
        if num % i == 0:
            return False
    return True


print PrimeTime(int(raw_input()))
