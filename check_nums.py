#Text of challenge: "have the function CheckNums(num1,num2) take both
#parameters being passed and return the string true if num2 is greater
#than num1, otherwise return the string false. If the parameter values
#are equal to each other then return the string -1."


def CheckNums(num1,num2): 

  num1 = int(num1)
  num2 = int(num2)
  
  if num2 == num1:
    return "-1"
  else:
    return num2 > num1

  
print CheckNums(int(raw_input()), int(raw_input()))
