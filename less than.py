classHeld=int(input("how many classes are class are held"))
classAttend=int(input("how many classes are attend by student"))
per=classAttend/classHeld*100
print("total percentage of this student is",per,"%") 
if per>75:
    print("this student is allowed to sit in exam")
else:
    print("this student is not allowed sit in exam")