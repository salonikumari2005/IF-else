side1=int(input("enter the first side"))
side2=int(input("enter the second side"))
side3=int(input("enter the third side"))
if side1==side2 or side2==side3 or side3==side1:
    print("isoceles triangle")
else:
    print("scalen triangle")