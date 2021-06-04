#facebook account
app=input("install your app")
if app=="facebook":
    print("open the facebook app")
    print("click on create new account")
    print("then click on next")
    print("now click on none of the above")
    firstname=input("enter your first name")
    lastname=input("enter your last name")
    if firstname=="saloni":
        if lastname=="kumari":
            print("next")
            birth_date=int(input("enter your birth date"))
            if birth_date==20_12_2004:
                print("next")
                gender=input("enter your gender")
                if gender=="female"or gender=="male":
                    print("next")
                    sign_up=input("select your sign up account")
                    if sign_up=="mobile number":
                        print("ok")
                        mobile_number=int(input("enter your mobile number"))
                        if mobile_number==1234567890:
                            print("your facebook is open")
                    elif sign_up=="email address":
                        print("ok")
                        email_address=input("enter your email address")
                        if email_address=="saloniroy9090@gmail.com":
                            print("next")
                            password=input("enter your password")
                            if password=="saloni34@":
                                print("next")
                                print("click on sign up")
                                print("creating your account")
                                save=input("do you want to save password")
                                if save=="yes" or save=="not now":
                                    print("ok")
                                    remember=input("are you want to remember your email address or password")
                                    if remember=="yes":
                                        print("show it")
                                        print("after that click on next")
                                        code=int(input("enter the code from your email"))
                                        if code==57137:
                                            print("confirm")
                                            profile_picture=input("add your profile picture so friends can find you")
                                            if profile_picture=="choose from gallery" or "take a photo":
                                                print("done")
                                                print("add your friends")
                                                print("save your login info")
                                                print("ok")
                                                print("congratulation! your facebook account is made successfully")
                                            else:
                                                print("something is went wrong")
                                        else:
                                            print("check it")
                                    else:
                                        print("please try again")
                                else:
                                    print("not ok")
                            else:
                                print("delete your account")
                        else:
                            print("exit")
                    else:
                        print("try again")
                else:
                    print("exit")
            else:
                print("go to hell")
        else:
            print("wrong name")
    else:
        print("wrong name")
else:
    print("dont create")


