bill=int(input("enter the unit of electricity bill"))
if bill<=100:
    print("no charge")
elif bill>100 and bill<=200:
    print("total bill amount",100*5)
elif bill>200:
    print("total bill amount is",200*10)
else:
    print("sorry! you are facing electriccity issue")