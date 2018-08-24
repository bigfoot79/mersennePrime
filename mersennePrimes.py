# detect mersenne prime numbers (test code only)
# Written by Vince, started 19/04/2018

# version 1.0       19/04/2018   Vincent     Initial program code
# version 1.1       01/06/2018   Vincent     Adding log to file system
#                                            Separate py into modules/package
# version 1.2       01/06/2018   Vincent     Using "generators" to store MP.
# version 1.2       24/08/2018   Vincent     Migrated to GitHub

# mersenne prime numbers are where (2**prime - 1) is also a prime number
# https://en.wikipedia.org/wiki/Mersenne_prime
# https://www.mersenne.org/primes/ (describes all known mersenne primes)
# largest known prime number is (2**77232917 - 1) is also a mersenne prime

# import declarations
import foo.log_file
import foo.prime_numbers

# function/block declarations
def mersenne_detector():

    foo.log_file.log_file_create()      # Create a new log file
    
    count = long(2)                     # allow higher whole numbers to be applied
    while count <= 4423:                  # (2^^4423 - 1)

        prime = long(count)

        # If this number a prime number, then continue otherwise move onto next number
        if foo.prime_numbers.IsPrime(prime) == True :
        
            mersenne_prime = (2**prime - 1)

            if foo.prime_numbers.IsPrime(mersenne_prime) == True :

                str_message = "%12d, %60d, MP candidate is a PRIME, MP has been identified!" % (prime,mersenne_prime)
                foo.log_file.log_file_append(str_message)
                yield prime
            else:
                str_message = "%12d, %60d, MP candidate is NOT a PRIME, MP not found" % (prime,mersenne_prime)
                foo.log_file.log_file_append(str_message)

        count = long(count + 1)
    
def main():

    # The mersenne detector uses the yield function which releases control back to the for loop after finding another mersenne prime.
    
    for prime in mersenne_detector():
        mersenne_prime = (2**prime - 1)
        print("Mersenne prime [prime: %5d]: %30d" % (prime,mersenne_prime))
        
    
if __name__ == '__main__':

    main()
    print("Program complete")



