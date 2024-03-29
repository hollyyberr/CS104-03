import random

numberofGuesses = 0
number = random.randint(1,1000000)
lowGuessRange = 1
highGuessRange = 1000000


name = input("Hello! What is your name? ")
print(name + ", I am thinking of a whole number between 1 and 1000000. Can you guess what it is?")

while numberofGuesses < 20:
    guess = input("Take a guess ")
    guess = int(guess)
    numberofGuesses = numberofGuesses + 1;
    guessesLeft = 20 - numberofGuesses;

    while guess > highGuessRange or guess < lowGuessRange:
        guess = int(input("The number is not in the range, please make a guess in between " + str(lowGuessRange) + " and " + str(highGuessRange) + ":"))
    if guess < number:
        guessesLeft=str(guessesLeft)
        lowGuessRange = guess
        print("Your guess is too low! You have " + guessesLeft + " guesses left")
        print("Enter a number between " + str(lowGuessRange) + " and " + str(highGuessRange))

    elif guess > number:
        guessesLeft=str(guessesLeft)
        highGuessRange = guess
        print("Your guess is too high! You have " + guessesLeft + " guesses left")
        print("Enter a number between " + str(lowGuessRange) + " and " + str(highGuessRange))
    
    if guess == number:
        break

if guess == number:
    numberofGuesses=str(numberofGuesses)
    print("Good job " +name+ "! You guessed the number in " + numberofGuesses + " tries! :)")

if guess != number:
    number=str(number)
    print("Sorry you've run out of guesses, "+name+ ". The number I was thinking of was " + number + ". :(")
