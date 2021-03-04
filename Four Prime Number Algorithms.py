import time


# Old algorthim (Version 1.0) 
def slowAlgorithm():
    #Gets start time
    startTime = time.process_time()
    #Sets the end number to check to
    endNumber = 10
    #Gets every number between 1 and end number and makes it prime default
    for aPossiblePrime in range(2,endNumber):
        possiblePrime = True
        #Gets every possible number between 2 and its current number
        for aFactor in range(2,aPossiblePrime):
            #If the option is prime it moves on or else makes it false
            if aPossiblePrime % aFactor > 0:
                pass
            elif aPossiblePrime % aFactor == 0:
                possiblePrime = False
        #It checks if it is still true from the beginning
        if possiblePrime == True:
            #Calculates how far the program has run
            percent = aPossiblePrime/endNumber*100
            print("{0:.0f}%".format(percent))
        else:
            pass
    #Calculates the final time it took to run
    print("Complete Checking")
    finalTime = time.process_time() - startTime
    print(finalTime)


# Prime function (version 2.0)
def isPrime(number):
    """This is a docstring, it's a one liner that's meant to summarize how a function works. Actually, it also automatically generates documentation if you use the correct programs to read docstring in the future. This is too long."""
    #Gets every number that could be a factor
    for candidateFactor in range(2,number):
        # This does not divide evenly and it is not a factor
        if number % candidateFactor > 0:
            pass
        #If it divdes evently then makes the function False
        elif number % candidateFactor == 0:
            return False
    return True

# Version 2.0 algorithm
def fastAlgorithm():
    # Records start time
    startTime = time.process_time()
    endNumber = 10

    # Finds all primes between 2 and the end number; calculates the percent of the program run
    for everyNumber in range(2,endNumber):
        if isPrime(everyNumber) == True:
            percent = everyNumber/endNumber*100
            print("{0:.0f}%".format(percent))
            pass
    #Calculates the time it took to run
    print("Completed Checking")
    finalTime = time.process_time() - startTime
    print(finalTime)



    
# Prime function (version 3.0)
def isUltraPrime(number):
    #Gets every number that could be a factor then gets sqrt because of repitiion then adds one because of how range works
    for candidateFactor in range(2,int(number**0.5 + 1)):
        # This does not divide evenly and it is not a factor
        if number % candidateFactor > 0:
            pass
        #If it divdes evently then makes the function False
        elif number % candidateFactor == 0:
            return False
    return True



#Super Fast Algorithm version 3.0
def ultraFastAlgorithm():
    # Records start time
    numberOfPrimes = 0 
    startTime = time.process_time()
    endNumber = 4500000
    # Finds all primes between 1 and the end number; calculates the percent of the program run
    for everyNumber in range(2,endNumber):
        if isUltraPrime(everyNumber) == True:
            percent = everyNumber/endNumber*100
            print("{0:.0f}%".format(percent))
            numberOfPrimes += 1
            pass
    #Calculates the time it took to run
    print("Completed Checking")
    finalTime = time.process_time() - startTime
    print(finalTime)
    print(numberOfPrimes)



# Prime function version 4.0
def isFourXPrime(number):
    #Gets every number that could be a factor then gets sqrt because of repitiion then adds one because of how range works
    for candidateFactor in range(2,int(number**0.5 + 1)):
        # This does not divide evenly and it is not a factor
        if number % candidateFactor > 0:
            pass
        #If it divdes evently then makes the function False
        elif number % candidateFactor == 0:
            return False
    return True

#Super Fast Algorithm version 4.0
def forthFastAlgorithm():
    # Records start time
    numberOfPrimes = 0 
    startTime = time.process_time()
    endNumber = 10000000
    # Finds all primes between 1 and the end number; calculates the percent of the program run
    for everyNumber in range(3,endNumber,2):
        if isFourXPrime(everyNumber) == True:
            percent = everyNumber/endNumber*100
            print("{0:.0f}%".format(percent))
            numberOfPrimes += 1
            pass
    #Calculates the time it took to run
    print("Completed Checking")
    finalTime = time.process_time() - startTime
    print(finalTime)
    print(numberOfPrimes)


# Command which algorithm to run
forthFastAlgorithm()


