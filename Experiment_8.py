"""Example will be the ATM machine
As we know ATM machine performs multiple operations and those are:
1.Account Information
2.PIN Change
3.Balance Inquiry
4.Withdrawal
5. Deposit
Now, What you need to do, You need to create a class of ATM and methods/functions is nothing but your operations that means your code will have 5 methods
One More important note, as you know if you enter wrong pin for three time it get block , that means you need to write a program in this way if I give wrong pin three times, Your account should get blocked. If you have any doubts, drop a comment or just text me on whats-app.
Do the same post your link in comment section

Now, How you will store data/Account information
store it in terms of dictionary or file as per your convenience.
1.If You are using dictionary:
key will be your name
value will be your - Acc. No, Mobile No., PIN
e.g. D={"ABC":5212485411,123454562,4545, "DEF":4559845253,1234567895,8989}

2.If you are using files include following:
Name:
Account No.
Mobile NO.
Address:
PIN
"""
class ATM:
    u1={"accno":5448254482,"mobno":9999999999,"pin":5421,"add":"Bhosari","balance":40000}
    u2={"accno":5448254483,"mobno":9999999998,"pin":5422,"add":"Chinchvad","balance":50000}
    u3={"accno":5448254484,"mobno":9999999997,"pin":5423,"add":"Moshi","balance":60000}
    u4={"accno":5448254485,"mobno":9999999996,"pin":5424,"add":"Pimpri","balance":40000}
    u5={"accno":5448254486,"mobno":9999999995,"pin":5425,"add":"Chakan","balance":90000}
    def Balance_inq(self):
        u1={"accno":5448254482,"mobno":9999999999,"pin":5421,"add":"Bhosari","balance":40000}
        u2={"accno":5448254483,"mobno":9999999998,"pin":5422,"add":"Chinchvad","balance":50000}
        u3={"accno":5448254484,"mobno":9999999997,"pin":5423,"add":"Moshi","balance":60000}
        u4={"accno":5448254485,"mobno":9999999996,"pin":5424,"add":"Pimpri","balance":40000}
        u5={"accno":5448254486,"mobno":9999999995,"pin":5425,"add":"Chakan","balance":90000}
        n=input("Enter your name:")
        a=int(input("Enter your account no"))
        if n=="u1":
            for i in range(0,3):
                p=int(input("Enter your pin"))
                if p==u1["pin"]:
                    print("Balance :",u1["balance"])
                    break
                else:
                    print("Wrong info entered!")
                    print("this was your",i+1,"turn out of 3 tries!")
                    print("After 3rd try your account will be blocked!")
                    if i==2:
                        print("Your account is blocked!")
        elif n=="u2":
            for i in range(0,3):
                p=int(input("Enter your pin"))
                if p==u2["pin"]:
                    print("Balance :",u2["balance"])
                    break
                else:
                    print("Wrong info entered!")
                    print("this was your",i+1,"turn out of 3 tries!")
                    print("After 3rd try your account will be blocked!")
                    if i==2:
                        print("Your account is blocked!")
        elif n=="u3":
            for i in range(0,3):
                p=int(input("Enter your pin"))
                if p==u3["pin"]:
                    print("Balance :",u3["balance"])
                    break
                else:
                    print("Wrong info entered!")
                    print("this was your",i+1,"turn out of 3 tries!")
                    print("After 3rd try your account will be blocked!")
                    if i==2:
                        print("Your account is blocked!")
        elif n=="u4":
            for i in range(0,3):
                p=int(input("Enter your pin"))
                if p==u4["pin"]:
                    print("Balance :",u4["balance"])
                    break
                else:
                    print("Wrong info entered!")
                    print("this was your",i+1,"turn out of 3 tries!")
                    print("After 3rd try your account will be blocked!")
                    if i==2:
                        print("Your account is blocked!")
        elif n=="u5":
            for i in range(0,3):
                p=int(input("Enter your pin"))
                if p==u5["pin"]:
                    print("Balance :",u5["balance"])
                    break
                else:
                    print("Wrong info entered!")
                    print("this was your",i+1,"turn out of 3 tries!")
                    print("After 3rd try your account will be blocked!")
                    if i==2:
                        print("Your account is blocked!")
    def deposit(self):
        u1={"accno":5448254482,"mobno":9999999999,"pin":5421,"add":"Bhosari","balance":40000}
        u2={"accno":5448254483,"mobno":9999999998,"pin":5422,"add":"Chinchvad","balance":50000}
        u3={"accno":5448254484,"mobno":9999999997,"pin":5423,"add":"Moshi","balance":60000}
        u4={"accno":5448254485,"mobno":9999999996,"pin":5424,"add":"Pimpri","balance":40000}
        u5={"accno":5448254486,"mobno":9999999995,"pin":5425,"add":"Chakan","balance":90000}
        x=input("name ")
        y=int(input("acc"))
        z=int(input("pin"))
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        for s in range(0,3):
            if x=="u1":
                try:
                    if z==u1["pin"] and y==u1["accno"]:
                        w=int(input("Enter the amount :"))
                        u1["balance"]=u1["balance"]+w
                        print(u1)
                        break
                except:
                    c1+=1
                    print("wrong pin!")
                    if c1==3:
                        print("Your account is blocked!")
            elif x=="u2":
                try:
                    if z==u2["pin"] and y==u2["accno"]:
                        w=int(input("Enter the amount :"))

                        u2["balance"]=u2["balance"]+w
                        print(u2)
                        break
                except:
                    c2+=1
                    print("wrong pin!")
                    if c2==3:
                        print("Your account is blocked!")
            elif x=="u3":
                try:
                    if z==u3["pin"] and y==u3["accno"]:
                        w=int(input("Enter the amount :"))

                        u3["balance"]=u3["balance"]+w
                        print(u3)
                        break
                except:
                    c3+=1
                    print("wrong pin!")
                    if c3==3:
                        print("Your account is blocked!")
            elif x=="u4":
                try:
                    if z==u4["pin"] and y==u4["accno"]:
                        w=int(input("Enter the amount :"))

                        u4["balance"]=u4["balance"]+w
                        print(u4)
                        break
                except:
                    c4+=1
                    print("wrong pin!")
                    if c4==3:
                        print("Your account is blocked!")
            elif x=="u5":
                try:
                    if z==u5["pin"] and y==u5["accno"]:
                        w=int(input("Enter the amount :"))

                        u5["balance"]=u5["balance"]+w
                        print(u5)
                        break
                except:
                    print("wrong pin!")
            else:
                c5+=1
                print("wrong pin!")
                if c5==3:
                    print("Your account is blocked!")
    def withdrawal(self):
        u1={"accno":5448254482,"mobno":9999999999,"pin":5421,"add":"Bhosari","balance":40000}
        u2={"accno":5448254483,"mobno":9999999998,"pin":5422,"add":"Chinchvad","balance":50000}
        u3={"accno":5448254484,"mobno":9999999997,"pin":5423,"add":"Moshi","balance":60000}
        u4={"accno":5448254485,"mobno":9999999996,"pin":5424,"add":"Pimpri","balance":40000}
        u5={"accno":5448254486,"mobno":9999999995,"pin":5425,"add":"Chakan","balance":90000}
        x=input("name ")
        y=int(input("acc"))
        z=int(input("pin"))
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        for s in range(0,3):
            if x=="u1":
                try:
                    if z==u1["pin"] and y==u1["accno"]:
                        w=int(input("Enter the amount :"))
                        if w<=u1["balance"]:
                            u1["balance"]=u1["balance"]-w
                            print(u1)
                        else:
                            print("You dont have enough balance!")
                        break
                except:
                    c1+=1
                    print("wrong pin!")
                    if c1==3:
                        print("Your account is blocked!")
            elif x=="u2":
                try:
                    if z==u2["pin"] and y==u2["accno"]:
                        w=int(input("Enter the amount :"))
                        if w<=u2["balance"]:
                            u2["balance"]=u2["balance"]-w
                            print(u2)
                        else:
                            print("You dont have enough balance!")
                        break
                except:
                    c2+=1
                    print("wrong pin!")
                    if c2==3:
                        print("Your account is blocked!")
            elif x=="u3":
                try:
                    if z==u3["pin"] and y==u3["accno"]:
                        w=(input("Enter the amount :"))
                        if w<=u3["balance"]:
                            u3["balance"]=u3["balance"]-w
                            print(u3)
                        else:
                            print("You dont have enough balance!")
                        break
                    else:
                        print("wrong info")
                except:
                    c3+=1
                    print("wrong pin!")
                    if c3==3:
                        print("Your account is blocked!")
            elif x=="u4":
                try:
                    if z==u4["pin"] and y==u4["accno"]:
                        w=int(input("Enter the amount :"))
                        if w<=u4["balance"]:
                            u4["balance"]=u4["balance"]-w
                            print(u4)
                        else:
                            print("You dont have enough balance!")
                    else:
                        print("wrong info")
                        break
                except:
                    c4+=1
                    print("wrong pin!")
                    if c4==3:
                        print("Your account is blocked!")
            elif x=="u5":
                try:
                    if z==u5["pin"] and y==u5["accno"]:
                        w=int(input("Enter the amount :"))
                        if w<=u5["balance"]:
                            u5["balance"]=u5["balance"]-w
                            print(u5)
                        else:
                            print("You dont have enough balance!")
                        break

                except:
                    c5+=1
                    print("wrong pin!")
                    if c5==3:
                        print("Your account is blocked!")
            else:
                print("wrong info!")
    def Acc_Info(self):
        u1={"accno":5448254482,"mobno":9999999999,"pin":5421,"add":"Bhosari","balance":40000}
        u2={"accno":5448254483,"mobno":9999999998,"pin":5422,"add":"Chinchvad","balance":50000}
        u3={"accno":5448254484,"mobno":9999999997,"pin":5423,"add":"Moshi","balance":60000}
        u4={"accno":5448254485,"mobno":9999999996,"pin":5424,"add":"Pimpri","balance":40000}
        u5={"accno":5448254486,"mobno":9999999995,"pin":5425,"add":"Chakan","balance":90000}
        a=input("Enter your name: ")
        p=int(input("Enter your account no :"))
        if a=="u1" and p==u1["accno"]:
            print("Name : ","u1")
            print("Account no: ",u1["accno"])
            print("Mobile number: ",u1["mobno"])
            print("Address: ",u1["add"])
        elif a=="u2" and p==u2["accno"]:
            print("Name : ","u2")
            print("Account no: ",u2["accno"])
            print("Mobile number: ",u2["mobno"])
            print("Address: ",u2["add"])
        elif a=="u3" and p==u3["accno"]:
            print("Name : ","u3")
            print("Account no: ",u3["accno"])
            print("Mobile number: ",u3["mobno"])
            print("Address: ",u3["add"])
        elif a=="u4" and p==u4["accno"]:
            print("Name : ","u4")
            print("Account no: ",u4["accno"])
            print("Mobile number: ",u4["mobno"])
            print("Address: ",u4["add"])
        elif a=="u5" and p==u5["accno"]:
            print("Name : ","u5")
            print("Account no: ",u5["accno"])
            print("Mobile number: ",u5["mobno"])
            print("Address: ",u5["add"])
        else:
            print("Wrong info entered!")
    def Pin_change(self):
        u1={"accno":5448254482,"mobno":9999999999,"pin":5421,"add":"Bhosari","balance":40000}
        u2={"accno":5448254483,"mobno":9999999998,"pin":5422,"add":"Chinchvad","balance":50000}
        u3={"accno":5448254484,"mobno":9999999997,"pin":5423,"add":"Moshi","balance":60000}
        u4={"accno":5448254485,"mobno":9999999996,"pin":5424,"add":"Pimpri","balance":40000}
        u5={"accno":5448254486,"mobno":9999999995,"pin":5425,"add":"Chakan","balance":90000}
        n=input("Enter your name ")
        p=int(input("Enter your pin "))
        for s in range(0,3):
            if n=="u1":
                try:
                    if p==u1["pin"]:
                        print("Please enter your new pin")
                        newpin=input()
                        u1["pin"]=newpin
                        print("You have succesfully changed your pin!")
                        print(u1)
                        break
                except:
                    print("wrong pin!")
            elif n=="u2":
                try:
                    if p==u2["pin"]:
                        print("Please enter your new pin")
                        newpin=input()
                        u2["pin"]=newpin
                        print("You have succesfully changed your pin!")
                        print(u2)
                        break
                except:
                    print("wrong pin!")
            elif n=="u3":
                try:
                    if p==u3["pin"]:
                        print("Please enter your new pin")
                        newpin=input()
                        u3["pin"]=newpin
                        print("You have succesfully changed your pin!")
                        print(u3)
                        break
                except:
                    print("wrong pin!")
            elif n=="u4":
                try:
                    if p==u4["pin"]:
                        print("Please enter your new pin")
                        newpin=input()
                        u4["pin"]=newpin
                        print("You have succesfully changed your pin!")
                        print(u4)
                        break
                except:
                    print("wrong pin!")
            elif n=="u5":
                try:
                    if p==u5["pin"]:
                        print("Please enter your new pin")
                        newpin=input()
                        u5["pin"]=newpin
                        print("You have succesfully changed your pin!")
                        print(u5)
                        break
                except:
                    print("wrong pin!")
            else:
                print("Wrong username!")

print("Services available:")
print("To display account information enter 1")
print("To change pin enter 2")
print("To deposit enter 3")
print("To withdraw enter 4")
print("For balance enquiry 5")
s=int(input("please enter a number as per the service required :"))

ob=ATM()
if s==1:
    ob.Acc_Info()
elif s==2:
    ob.Pin_change()
elif s==3:
    ob.deposit()
elif s==4:
    ob.withdrawal()
elif s==5:
    ob.Balance_inq()
else:
    print("Sorry,service unavailable!")
