from random import randrange

number = randrange(1, 9)

print("Wanna feel like a magician?\nI'll pick a number between 1 and 9, and you have to guess it. You have 3 tries. Good luck!")

while True:
    guess = int(input("Enter your guess: "))
    
    if type(guess) != int:
        print("That's not how you play the game. Try again.")
        continue
    
    elif guess == number:
        print("You guessed it! The number was " + str(number) + ".")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
        continue
    else:
        print("Your guess is too high. Try again.")
        continue