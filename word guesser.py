import random


def main():
    ans = input("start guessing: ")
    for i in range(0, 3):
        failed = 0
        for char in b:
            if char in ans:
                print(char, end="")
            else:
                print('_', end='')
                failed += 1
        if failed == 0:
            print("you win!")
            print(f"the word is: {b}")
            return True
        else:
            print(f"You are almost there. Try again")
            print(f"turns left = {3-i}")
            ans = input("start guessing: ")

    print("You lose!")
    return False


file = open("/home/shaurav/programms/python/words.txt", "r")
x = []
for a in file:
    x.append(a)
b = random.choice(x)

if __name__ == '__main__':
    main()
