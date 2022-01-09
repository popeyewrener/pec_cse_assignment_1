def q1():
    #program to find average of 3 numbers!!

    num1=float(input("Enter 1st number: "))
    num2=float(input("Enter 2nd number: "))
    num3=float(input("Enter 3rd number: "))

    avg=((num1+num2+num3)/3)

    print("The average of", num1, num2,num3, "is", avg)


def q2():
    #program to compute income tax

    #assigning constants first


    inc=float(input("Enter your gross income in dollars: "))
    dep=int(input("Enter total dependents: "))

    inc_tax=(inc-10000-(dep*3000))


    final_tax=inc_tax*0.2
    final_tax=round(final_tax,2)

    if final_tax<0:
        final_tax=0

    else:
        final_tax=final_tax


    print("Your income tax is: ", final_tax)   


def q3():
    sid=input("Enter SID: ")
    name=input("Enter name: ")

    gender=input("Enter Gender(M,F,U for unknown)")

    course=input("Enter course name: ")
    cgpa=float(input("Enter CGPA"))

    student=[sid,name,gender,course,cgpa]

    print(student)

def q4():
    mlist=[]
    for i in range (5):
        mark=float(input("Enter mark of Student:" ))
        mlist.append(mark)
        



    mlist.sort()

    print(mlist)



def q5a():
    color=['red','Green', "White",'Black', 'Pink', 'Yellow']
    color.pop(3)
    print(color)


def q5b():
    color=['red','Green', "White",'Black', 'Pink', 'Yellow']
    color[color.index("Black")]="Purple"; color[color.index("Pink")]="Purple"
    print(color)


def inputchoice():
    print("Enter Question number you want to explore: (Valid inputs are '1,2,3,4,5a,5b')")
    choice=input("Enter your choice here: ")
    if choice == "1":
        q1()
        inpchoice()
        

    elif choice == "2":
        q2()
        inpchoice()

    elif choice == "3":
        q3()
        inpchoice()

    elif choice == '4':
        q4()
        inpchoice()
    elif choice == "5a":
        q5a()
        inpchoice()

    elif choice == "5b":
        q5b()
        inpchoice()

    else:
        print("Invalid input",choice)
        print("Taking you to choice again!!")
        inputchoice()    

def inpchoice():
    ichoice= input("Do you want to try something else or quit ('Y' to try 'N' to quit)")
    if ichoice.upper() == "Y":
        inputchoice()
    elif ichoice.upper() == "N":
        print("CLOSED PROGRAM") 
    else:
        print("Invalid choice",ichoice)
        print("asking you again!!") 
        inpchoice()      


inputchoice()





