import random
theComputerNumber = random.randint(1,1000000)
gameOver = False
lowGuessRange = 1
highGuessRange = 1000000
numberOfGuesses = 0

#This is the game loop
while not gameOver:
    playerGuess = input ("Please enter your guess: ")
    print (playerGuess)
    # gameOver = True
    # if guess is in range
    # if guess > computer
    # if guess < computer
    # if guess = computer
    # updating low and high ranges
    # updating and testing if number of guesses exceeded
