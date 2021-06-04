a=int(input("enter the first age"))
b=int(input("enter the second age"))
c=int(input("enter the third"))
if a> b and a >c:
    print("oldest is",'a')
elif b > a and b> c:
    print("oldest is",'b')
elif c >a and c >b:
    print("oldest is",'c')
else:
    print("all is equal")
