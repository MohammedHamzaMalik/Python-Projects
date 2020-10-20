import time  # Importing module time

# Welcoming the user

name = input("Hey welcome, wait a minute!, who are you?, what's your name? ")

print("Hello " + name + ", welcome to HANGMAN!, it's time to play.")

time.sleep(1)  # Giving some time to user to get ready for the game

print("Start guessing...")

time.sleep(1.5)

word = "aurora"  # Creating the word which is to be guessed by the user
# meaning of aurora : the dawn in the morning
user_guesses = " "

turns = 5

# Making a while loop and checking whether the number of turns are more than 0 or not
while turns > 0:
    fail_count = 0  # Initializing fail count to zero

    for char in word:  # Traversing through each character in the word
        if char in user_guesses:
            print(char)
        else:
            print("___")
            fail_count += 1  # Increasing the fail count

    if fail_count == 0:
        print("Heyya! You won the game! Congrats buddy 👍")
        break

    user_guess = input("Hey "+name+" guess a character : ")  # Taking guessed character from user

    user_guesses += user_guess  # Adding the guessed character to the guessed word

    if user_guess not in word:

        turns -= 1  # Decreasing the number of turns one by one

        print("Sorry buddy you'r wrong !")
        if turns > 0:
            print("You can guess for only " + str(turns) + " times")
        else:
            print("Buddy! you lost are your chances.")
        if turns == 0:
            print("Alas! you lose😭")
            
