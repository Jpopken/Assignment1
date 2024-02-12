#Assignment 1
#Assignment1
#jonahkpopken@lewis.edu
#Software Engineering – CPSC44000 - LT1 week 2 assignment
#02/05/2024
#This program finds the

#constants that set the min/max rangers per the assignment instructions
MINIMUM_RANGE =10
MINIMUM_EXPONENT =2
MAXIMUM_EXPONENT=12

#gets the exponent from the user and verifies it is within the range requested
def getExponent(n):

    while True:
        try:
            n = int(input("Enter the exponent "))
            if MINIMUM_EXPONENT < n < MAXIMUM_EXPONENT:
                print("You entered:", n)
                return n
            else:
                print("Error: The value entered must be a natural number that is greater than 2 but less than 12")
        except ValueError:
            print("Error: Please enter a natural number that is greater than 2 but less than 12")

#gets the range from the user and verifies it is within the range requested
def getRange(k):
    while True:
        try:
            k = int(input("Enter the range "))
            if k < MINIMUM_RANGE:
                print("Error the range must be greater than 10")
            else:
                print("You entered " + str(k))
                return k
        except ValueError:
            print("ERROR: Please enter a natural number that is greater than 10")
#calculates the nearest miss
def findNearMiss(n,k):
    nearMiss = 0

    #finds the sum of i**n and j**n and assigns it to xy
    for i in range (10,k+1):
         for j in range(10,k+1):
            xy = i **n + j ** n
            #uses xy to calculate z
            z = int(xy ** (1/n))
            #Sets z to be less than xy
            while z ** n >= xy:
                    z-=1

            #calculates which is closer to xy, z**n or z+1**n
            if (xy - (z**n)) < ((z+1)**n-xy):
                tempMiss = z**n / xy
            elif (xy - (z**n)) > ((z+1)**n-xy):
                tempMiss = (z+1) ** n / xy
                #increment z by 1 since z+1 is the closer value
                z +=1
            #checks to see if the current tempMiss is less than the current closest miss, or if nearMiss is 0
            if (tempMiss < nearMiss) or (nearMiss == 0):
                nearMiss = tempMiss
                print("\nNew nearest miss found at the following values\nx: " + str(i) + "\ny: "
                      + str(j) + "\nz: " + str(z) + "\nnear miss: " + str(nearMiss*xy) +
                      "\nrelative miss: " + str(round(nearMiss * 100, 2)) + "%"  )
    print("Search Complete.")


if __name__ ==  "__main__":

    numN = getExponent(input)
    numK = getRange(input)
    findNearMiss(numN,numK)
    input("Press Enter to exit...")
