price=int(input("enter the price"))
quantity=int(input("enter the quantity"))
amt=price*quantity
if amt>1000:
    print("10% discount applicable")
    discount=amt*10/100
    amt=amt-discount
    print("amount payable:",amt)
else:
    print("no discount")

