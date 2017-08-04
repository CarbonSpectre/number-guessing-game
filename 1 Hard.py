import random, time

print("You will think of a number between 1 and 100, and I'll try to guess what it is!")
time.sleep(5)

correct = False

numberList = [1,100]

number = random.randint(1,100)
tries = 0

while correct == False:
    numberList.append(number)
    numberList.sort()
    time.sleep(2)
    tries += 1
    guess = str(input("\nIs your number "+str(number)+"? "))
    if guess in ["Yes","yes"]:
        print("Guessed correctly in", tries, "tries!")
        break
    elif guess in ["No","no"]:
        higherLower = str(input("Is your number higher or lower? "))
        if higherLower in ["Higher","higher"]:
            numberList.pop(0)
            number = random.randint((number+1),numberList[-1])
        elif higherLower in ["Lower","lower"]:
            numberList.pop(-1)
            number = random.randint(numberList[0],(number-1))
    
