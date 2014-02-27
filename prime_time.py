def PrimeTime(num):
    
    numrange = range(num)
    
    del numrange[0:2]
    
    for i in numrange:
        if num % i == 0:
            return False
    return True


print PrimeTime(int(raw_input()))
