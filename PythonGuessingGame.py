import random
computerNumber = random.randint(1,1000000)
gameOver = False
lowGuessRange = 1
highGuessRange = 1000000
numberOfGuesses = 20


#This is the game loop
while gameOver != True:
    
    playerGuess = int(input("Please enter your guess between " + str(lowGuessRange) + " and " + str(highGuessRange) + ":" ))
    if(playerGuess < computerNumber)
        print("The guess is too low")
    numberOfGuesses -= 1
    print("Guesses remaining: " + str(numberOfGuesses))
    
    
            
    #print (
    #gameOver = True
    #if guess is in range
    #if guess > computerNumber
    #if guess < computerNumber
    #if guess = computerNumber
    #updating low and high ranges
    # updating and testing if number of guesses exceeds guess limit which is 20
    
    
