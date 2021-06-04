num=int(input("enter the number"))
if num%3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
elif num%3 and 5==0:
    print("fizz-buzz")
elif num%3 and 5!=0:
    print("buzz-fizz")
else:
    print("non divisible")