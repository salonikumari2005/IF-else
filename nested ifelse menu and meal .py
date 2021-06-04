day=input("enter the day")
meal=input("enter the meal")
if day=="monday":
    if meal=="breakfast":
        print("poori sabji")
    elif meal=="lunch":
        print("sambhar rice")
    else:
        print("chiken rice")
elif day=="tuesday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("rajma chawal")
    else:
        print("roti sabji")
else:
    print("nothing")