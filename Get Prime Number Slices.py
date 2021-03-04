# Ultra fast isPrime algorithm
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

#Super Fast Algorithm version 3
def ultraFastAlgorithm():
    # Selects the interval, number of slices.
    interval = 10000
    numberOfSlices = 100
    numberOfPrimes = 0
    primeNumberList = []
    # Get the number of primes in each slice
    for oneSlice in range(0,numberOfSlices):
        startValue = oneSlice*interval+1
        endValue = interval*(oneSlice+1)
        numberOfPrimes = 0
        if startValue == 1:
            startValue = 2
            for everyNumber in range(startValue,endValue):
                if isUltraPrime(everyNumber):
                    numberOfPrimes += 1
                    pass
            print("(" + str(startValue) + "," + str(numberOfPrimes) + ")")
        else:
            for everyNumber in range(startValue,endValue):
                if isUltraPrime(everyNumber) == True:
                    numberOfPrimes += 1
                    pass
            #Prints number of percent of primes of end number
            print("(" + str(startValue) + "," + str(numberOfPrimes) + ")")        

ultraFastAlgorithm()
