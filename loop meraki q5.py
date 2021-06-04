
# student_number=int(input("enter the number")
# expenditure=int(input("enter the number"))
# budget=student_number*expenditure
# if budget<=50000:
#     print("under")
# else:
#     print("high")

num=int(input("enter the number"))
x=(num%10)
y=(num//10)%10
z=(num//100)
new_num=(x*100)+(y*10)+(z*1)
if num>10:
    print(new_num)
else:
    print("invalid number")

 