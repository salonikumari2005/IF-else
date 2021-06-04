day=input("enter the day")
if day=="sunday"or "monday":
    print("i want to go outside")
    takepermission=input("enter the name from whom you take a permission")
    if takepermission=="disco":
        print("can i go to outside?")
        givepermission=input("take permission")
        if givepermission=="yes":
            print("you can go to outside")
            print("but don't travel long distance otherwise you will have to quarantine")
            quarantine=(input("enter the day of quarantine"))
            if quarantine=="7 days":
                print("it's good to safety")
                takepermission=input("enter the name from whom you take a permissiom after disco")
                if takepermission=="rose dii":
                    print("can i go to outside?")
                    givepermission=input("take permission")
                    if givepermission=="yes":
                        print("sure allow you")
                        precaution=input("enter the precaution")
                        if precaution=="mask,sanitizer and gloves":
                            print("i am ready to go outside")
                            place=input("enter the place where ever you go")
                            if place=="medical store":
                                print("you can go")
                            else:
                                print("you can't go")
                        else:  
                            print("i am not ready to go outside")
                    else:
                        print("not allow")
                else:
                    print("can i not go to  outside")
            else:
                print("it's not good for safety")
        else:
            print("you can  not go to outside")
    else:
        print("can i not go to outdside")
else:
    print("i don't want to go outside")


    