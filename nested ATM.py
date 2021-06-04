print("you are welcome")
card_insert=input("insert your card")
if card_insert=="ATM CARD":
    print("accepted your card")
    language=input("choose your language")
    if language=="english":
        print("next")
        pin=int(input("enter your pin"))
        if pin==800006:
            print("good")
            password=int(input("enter the four digit password"))
            if password==1234:
                print("correct")
                account=input("enter the type of a/c")
                if account=="saving" or account=="current":
                    print("in process your service")
                    transaction=input("select your transaction")
                    if transaction=="cash withdrawal":
                        print("in process")
                        amount=int(input("enter the amount"))
                        total=int(input("enter the total amount"))
                        if amount<=10000:
                            print("in process your service")
                            print("transaction is successfully done")
                            print("collect your cash")
                            receipt=input("do you want receipt")
                            if receipt=="yes":
                                print("collect your receipt")
                                print("your remaining balance is",(total-amount))
                                print("thank you for transaction")
                    elif transaction=="pin change":
                        print("in process your service")
                        pin_change=input("do you want to change your pin")
                        new_pin=input("enter your new pin")
                        if pin_change=="yes":
                            print("your new pin is",new_pin)
                    elif transaction=="deposit":
                        print("select your bank")
                        bank=input("enter the bank name")
                        if bank=="SBI" or "ICICI":
                            print("ok")
                            mobile_num=int(input("enter the mobile number"))
                            if mobile_num==1234567890:
                                print("in processing your service")
                                account_num=int(input("enter the a/c number"))
                                if account_num==1234567890:
                                    print("in processing your service")
                                    confirm=input("are you confirm your deposit")
                                    if confirm=="yes":
                                        print("put your cash in machine")
                                        amount=int(input("enter your amount"))
                                        total=int(input("enter your total amount"))
                                        print("your total balance is",(total+amount))
                                    else:
                                        print("no")
                    elif transaction=="balance enquiry":
                        print("in processing your service")
                        print("pleas wait")
                        total=int(input("enter your total amount"))
                        print("your total balance is",(total))
                    else:
                        print("sorry! your service is unvailable")
                else:
                    print("link failed")
            else:
                print("wrong")
        else:
            print("bad")
    else:
        print("exit")
else:
    print("refused your card")
    













































