import random

def add_quest():
    global correct, wrong
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    trueans = num1 + num2
    qloop = True
    while qloopa:
        try:
            ans = int(input("What is " + str(num1) + " + " + str(num2) + "? "))
            if ans == trueans:
                correct += 1
                qloopa = False
            else:
                wrong += 1
        except ValueError:
            print("Please enter a valid number.")
            ans = int(input("What is " + str(num1) + " + " + str(num2) + "? "))
            wrong += 1

def sub_quest():
    global correct, wrong
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    while num1 > num2:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
    trueans = num2 - num1
    ans = int(input("What is " + str(num2) + " - " + str(num1) + "? "))
    if ans == trueans:
        correct += 1
    else:
        wrong += 1

def multi_quest():
    global correct, wrong
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    trueans = num1 * num2
    ans = int(input("What is " + str(num1) + " x " + str(num2) + "? "))
    if ans == trueans:
        correct += 1
    else:
        wrong += 1

def div_quest():
    global correct, wrong
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    while num1 > num2 or num2 % num1 != 0:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
    trueans = num2 // num1
    ans = int(input("What is " + str(num2) + " ÷ " + str(num1) + "? "))
    if ans == trueans:
        correct += 1
    else:
        wrong += 1

def arth_quiz(name):
    global correct, wrong
    correct = 0
    wrong = 0
    
    print("Hello " + name + "! Welcome to the arithmetic quiz.")
    
    addq = 0
    subq = 0
    multiq = 0
    divq = 0
    
    while addq + subq + multiq + divq < 12:
        current_quest = random.randint(1, 4)
        if current_quest == 1 and addq < 3:
            add_quest()
            addq += 1
        elif current_quest == 2 and subq < 3:
            sub_quest()
            subq += 1
        elif current_quest == 3 and multiq < 3:
            multi_quest()
            multiq += 1
        elif current_quest == 4 and divq < 3:
            div_quest()
            divq += 1
    
    print("The test is over! You got " + str(correct) + " correct and " + str(wrong) + " wrong.")

def ask_arith():
    name = input("Please type in your name: ")
    ans = input("Would you like to start the quiz? Y/N ")
    loop = True
    while loop:
        if ans == "Y":
            arth_quiz(name)
            ans = input("Would you like to start the quiz again? Y/N ")
        if ans == "N":
            loop = False
            print("OK, Goodbye!")
        else:
            print("Please try anwsering again")
            ans = input("Would you like to start the quiz again? Y/N ")

ask_arith()

