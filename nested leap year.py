year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400:
            print("leap year")
        else:
            ("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
        