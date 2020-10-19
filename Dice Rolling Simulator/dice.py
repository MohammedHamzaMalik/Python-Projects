import random

roll_the_dice = 'yes'

while roll_the_dice == 'yes':
    num = random.randint(1, 6)

    if num == 1:
        print("     "
              "\n  *  "
              "\n     ")
    if num == 2:
        print("*    "
              "\n     "
              "\n    *")
    if num == 3:
        print("*    "
              "\n  *  "
              "\n    *")
    if num == 4:
        print("*   *"
              "\n     "
              "\n*   *")
    if num == 5:
        print("*   *"
              "\n  *  "
              "\n*   *")
    if num == 6:
        print("*   *"
              "\n*   *"
              "\n*   *")

    roll_the_dice = input("Want to roll the dice again!, enter yes, if not then enter no : ")
    if roll_the_dice == 'No':
        print("Thanks for playing!"
              "\nSee you again soon 😀")
    print("\n")
