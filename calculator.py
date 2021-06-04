operand1=int(input("enter the first number"))
operand2=int(input("enter the second number"))
operation=input("enter the operation")
if operation=="+":
    print(operand1+operand2,"addition")
elif operation=="-":
    print(operand1-operand2,"subtraction")
elif operation=="*":
    print(operand1*operand2,"multipiy")
elif operation=="%":
    print(operand1%operand2,"modulus")
elif operation=="/":
    print(operand1/operand2,"division")
elif operation=="//":
    print(operand1//operand2,"floor division")
else:
    print("xyz")