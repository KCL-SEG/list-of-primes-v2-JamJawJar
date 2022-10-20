"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def findNextPrime(firstPrimeNumber):
    foundPrime = False
    newPrime = firstPrimeNumber
    while not foundPrime:
        newPrime += 1
        for number in range(2, newPrime):
            if newPrime % number ==0:
                foundPrime = False
                break
            else:
                foundPrime = True

    return newPrime


def primes(number_of_primes):

    if(number_of_primes <= 0):
        raise ValueError

    list = []

    while(len(list) < number_of_primes):
        if len(list) == 0:
            list.append(2)
        else:
            list.append(findNextPrime(list[-1]));
    return list
