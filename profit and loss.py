sp=int(input("enter the selling price"))
cp=int(input("enter the cost price"))
if sp>cp:
    print(sp-cp,"profit")
elif cp-sp:
    print(cp-sp,"loss")
else:
    print("invalid")