#conditional test in the while statement
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished. "

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("  You get in free!")
        elif age < 13:
            print("  Your ticket is $10.")
        else:
            print("  Your ticket is $15.")

#Use a conditional test in the while statement to stop the loop
active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        active=False
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        active=False
    elif int(age)>12:
        print("Ticket is $15")
        active=False

#Use an active variable to control how long the loop runs
count=0
while count<10:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        count+=1
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        count+=1
    elif int(age)>12:
        print("Ticket is $15")
        count+=1

#Use a break statement to exit the loop when the user enters a 'quit' value.
active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        active=False
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        active=False
    elif int(age)>12:
        print("Ticket is $15")
        active=False
    elif age=='quit':
        break