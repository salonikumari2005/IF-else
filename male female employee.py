Age = int(input("Enter the age: "))
sex = input("Enter the sex: ")
if sex == "female":
    print("she will work only urban areas ")
elif sex == "male":
    if Age >=20 and Age<=40:
        print("he work anywhere")
    elif Age >=40 and Age<=60:
        print("he work only in urban area")
    else:
        print("error")
else:
    print("he can't able to do work")

