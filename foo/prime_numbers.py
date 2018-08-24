# detect mersenne prime numbers (test code only)
# Written by Vince, started 19/04/2018

# version 1.0       19/04/2018   Vincent     Initial program code
# version 1.1       01/06/2018   Vincent     Adding log to file system
#                                            Separate py into modules/package

# This py script only contains the prime number checking routine.

# import declarations

# function/block declarations

def IsPrime(prime):

    # check to determine whether the number itself is a prime number
    # automatically cut out all even number, except 2, as not prime numbers.
    # otherwise cycle through first half of all integers below the specified integer.

    # Can we use MATH functions?
    # Is multi-threading available?
    
    if prime == 2 or prime==3 or prime==5 or prime==7:
        return  True
    elif prime % 2 == 0:
        # the only even prime number is 2.
        # the modulus function is computationally expensive, can I reduce this further ???
        return False
    else:
        # number must be odd
        index = 3
        index_max = int((prime**0.5)+1)
        while index < index_max:
            if prime % index == 0:
                # if the number is divisible by another number other than itself and 1,
                # then it is not a prime number

                # if div by 2, then false, but if div by 6, then false.
                # why check 6 ?!?  Only check against prime numbers.
                
                return False
            index = index + 1
        return True

