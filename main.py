import os
import datetime
import webbrowser

command = {}
work = {}
print("::::: ::  ::  :::::::   :::::::   1")
print(":: :: ::  ::  ::   ::   ::        ")
print("::::: ::  ::  ::   ::   :::::::   ")
print("::      ::    ::   ::        ::        ")
print("::      ::    :::::::   :::::::       ")
print("                             PySoft Tech.")
print("^_^")
hour = int(datetime.datetime.now().hour)
if hour >= 4 and hour <= 9:
    print("Good Morning!")
    print("Extras: i")
elif hour >= 10 and hour <= 12:
    print("Good Noon!")
    print("Extras: i")
elif hour >= 13 and hour <= 16:
    print("Good Afternoon!")
    print("Extras: i")
elif hour >= 17 and hour <= 20:
    print("Good Evening!")
    print("Extras: i")
elif hour >= 21 and hour <= 24:
    print("Hello!")
    print("Extras: i")
else:
    print("Hello!")
    print("Extras: i")


def OS():
    def close():
        print("^_^")
        print("Hope you enjoyed the session...")
        print("Bye!")

    def notClose():
        print("¤ PyOS didn't shut down!")

    while True:
        print("        ")
        print("_________________________________________")
        print("              ")
        a = input("                 |")

        if a == 'quit()':
            print("Shut down?")
            while True:
                b = input("》")
                if b != "":
                    break
            if b == 'ok':
                close()
                break
            elif b == 'no':
                notClose()
            else:
                print("¤ Invalid confirmation command!")

        elif a == 'search':
            print("")
            q = input("¤ Search for: ")
            webbrowser.open("www.google.com?search=" + q)
        elif a == 'dir':
            path = "/"
            dir_list = os.listdir(path)
            print(dir_list)

        elif a == 'note':
            print("  ")
            print(":::::::::::::")
            print("::::|==|:::::")
            print(":: -------- :")
            print(":: -------- :")
            print(":: ------<====¤")
            print(":::::::::::::")
            print("      ")
            stringToSave = input("¤ Note here something: ")
            fileName = input("¤ Enter the file name: ")
            d = stringToSave
            k = fileName
            command[k] = d
            fileName2 = fileName + ".txt"
            f = open(fileName2, 'w')
            f.write(stringToSave)
            f.close()

        elif a == 'cal':
            print("    ")
            print("::::::::::::::::::::::::::::::::")
            print(":[                      ]:::::::")
            print("::::::::::::::::::::::::::::::::")
            print("::[1]::[2]::[3]::[4]::[5]::[C]::")
            print("::[6]::[7]::[8]::[9]::[0]::[.]::")
            print("::::::::::::::::::::::::::::::::")
            while True:
                print("                                             ")
                print("^_^")
                print("¤ Welcome to Calculator!")
                print("¤ Divide = /, Multipy = *, Add = +, Subtract = -, To exit = end")
                op = input("¤ Enter the operation: ")

                if op == '+':
                    num1 = input("¤ Enter the first number: ")
                    num2 = input("¤ Enter the second number: ")
                    num3 = float(num1) + float(num2)
                    print("=", num3)

                elif op == '/':
                    type = input("¤ Enter the type of answer (Decimal = d, Remainder type = r):  ")
                    if type == 'd':
                        num1 = input("¤ Enter the dividend: ")
                        if num1 == 'end':
                            break
                        else:
                            num2 = input("¤ Enter the divisor: ")
                        num3 = float(num1) / float(num2)
                        print("=", num3)
                    elif type == 'end':
                        break
                    elif type == 'r':
                        num1 = input("Enter the dividend: ")
                        if num1 == 'end':
                            break
                        else:
                            num2 = input("Enter the divisor: ")
                        num3 = float(num1) // float(num2)
                        num4 = float(num1) % float(num2)
                        print("¤ Quotient: ", num3)
                        print("¤ Remainder: ", num4)
                    else:
                        print("Calculation out of range!")
                elif op == '*':
                    num1 = input("Enter the first number: ")
                    if num1 == 'end':
                        break
                    else:
                        num2 = input("Enter the second number: ")
                    num3 = float(num1) * float(num2)
                    print("=", num3)
                elif op == '+':
                    num1 = input("Enter the first number: ")
                    if num1 == 'end':
                        break
                    else:
                        num2 = input("Enter the second number: ")
                    num3 = float(num1) + float(num2)
                    print("=", num3)
                elif op == '-':
                    num1 = input("Enter the first number: ")
                    if num1 == 'end':
                        break
                    else:
                        num2 = input("Enter the second number: ")
                    num3 = float(num1) - float(num2)
                    print("=", num3)
                elif op == 'end':
                    break
                else:
                    print("Enter valid operator!")

        elif a == 'cmd':
            print("    ")
            print("::::::::::::::::")
            print("::[C:/>   ]:::::")
            print("::::::::::::::::")
            while True:
                print("                                  .")
                print("PyOS 1.0.0.1")
                print("Command Prompt.>>>")
                b = input("》")
                if b == 'close':
                    break
                elif b == 'copyrights()':
                    print("-PyOS Community Ver. 1.0.0.1")
                    print(
                        "-Any copy of this product in any modern o r traditional way of storage and retriev al system without first written permissi on from the company will be considered i nvalid and an illegal offense as per the 'Copyrights Section and Act, 1975' at a  ny cost")
                    print("-Publisher and Developer: PySoft Tech. Pv t. Ltd.")
                    print("-Visit: about@pysoft.com")
                    print("-Or: www.pysoft.com/about")
                elif b == 'reset()':
                    k = 'r'
                    d = 'reset()'
                    command[k] = d
                elif b == 'about()':
                    print("-PyOS Community Ver. 1.0.0.1")
                    print("-By Sahil Gupta")
                    print("-Linux based Unix-like Operating System.  Powered by Python ")
                    print("-By PySoft Tech. Pvt. Ltd.")
                    print("-For Premium, Workgroup and other version s. Log in to www.pysoft.com/sales")
                elif b == 'end()':
                    break
                else:
                    print("Please Wait...")
                    print("(-_-)")
                    print("Bad or Invalid command!")

        elif a == 'open':
            try:
                k = input("¤ Enter file name: ")
                file = "\\" + k
                os.startfile(r"C:\Users\Admin\PyCharmProjects\PyOS"+ file)
            except Exception as e:
                print(e)
        elif a == 'time':
            hour = int(datetime.datetime.now().hour)
            if hour > 12:
                hour2 = hour - 12
                minute = str(datetime.datetime.now().minute)
                time = str(hour2) + ":" + minute + " PM"
                print("         ")
                print(":::::::::::::::")
                print("::[", time, "]::")
                print(":::::::::::::::")

                print("¤ Note: For updating time retype command  'time'")
            elif hour == 0:
                minute = str(datetime.datetime.now().minute)
                time = "12" + ":" + minute + " AM"
                print("          ")
                print(":::::::::::::::")
                print("::[", time, "]::")
                print(":::::::::::::::")

                print("¤ Note: For updating time retype command  'time'")
            elif hour == 12:
                minute = str(datetime.datetime.now().minute)
                time = str(hour) + ":" + minute + " PM"
                print("           ")
                print(":::::::::::::::")
                print("::[", time, "]::")
                print(":::::::::::::::")
                print("Hello!")
                print("¤ Note: For updating time retype command  'time'")
            else:
                minute = str(datetime.datetime.now().minute)
                time = str(hour) + ":" + minute + " AM"
                print("              ")
                print(":::::::::::::::")
                print("::[", time, "]:")
                print(":::::::::::::::")
                print("¤ Note: For updating time retype command  'time'")
        elif a == 'i':
            print("   ")
            print(
                "- We know that this Operating System is n  ot like Windows, MacOS or any other dom  inant OS. It's just a cmd. line app dev  eloped by tye newly formed company of j  ust two employees. But don't worry we j  ust need some support and funds to grow  better and we are pretty much sure that  you will defintely see PySoft Tech. bec  oming a tech giant like Apple, Google o  r Microsoft! Please don't forget to don  ate us at www.pysoft.com/donate. Thank   you ^_^")
            print("    ")
            print("--- By Sahil Gupta")
            print("--- CEO & Founder of PySoft Tech. Pvt. Lt    d.")
        elif a == 'dir':
            if command != "":
                print("¤ Your files: ")
                print(command)
            else:
                print("¤ You don't have any files!")
        elif a == "quit":
            print("¤ Wrong command for shut down!")
            print("¤ Type 'quit()'")
        elif a == 'yes' or a == 'no':
            print("¤ No use of confirmation commands, yes or  no!")
        else:
            print("¤ No such programs found!")


print("Inspired by MS-DOS and Altair Basic.")
print("|To Open instruction panel: ins")
print("|Or: To skip = press any key")
print("=========================================")
c = input("》")
if c == 'ins':
    print("|To close any program: end")
    print("|Notepad : note")
    print("|Command Prompt. : cmd")
    print("|To close a program : end")
    print("|Yes or acceptance : ok")
    print("|No or cancel : no")
    print("|Time : time")
    print("|To see files : dir")
    print("|To set reminders : set")
    print("|Calculator : cal")
    print("|To open text files of note : open")
    print("|To shut down : quit()")
    print("|Extras: i")
    OS()
else:
    OS()
