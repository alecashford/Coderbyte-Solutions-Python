def CheckNums(num1,num2): 

  num1 = int(num1)
  num2 = int(num2)
  
  if num2 == num1:
    return "-1"
  else:
    return num2 > num1

  
print CheckNums(int(raw_input()), int(raw_input()))
