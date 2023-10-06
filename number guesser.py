import random
x = random.randint(0, 10)
def game():
    for i in range(0, 3):
        a = int(input(
            "enter the number you guessed: "
        ))
        if a == x:
            return True
        else:
            print("try again")
            if a > x:
                print("the number you guessed is greater.")
            else:
                print("the number is less.")
                
if game() == True:
    print("you guessed the correct number!")
else:
    print(f"you guessed the incorrect number three times. the correct number is {x}")


