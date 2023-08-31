def is_prime(n):

    if n < 2:
        return False
    curNum = 2

    while curNum ** 2 <= n: 
    # Realized that if a number is prime, it's factors will lie below the first factor squared to be greater than n 

        if n % curNum == 0: # if curnum is a factor, then n is def not prime 
            return False 
        curNum += 1

    return True # Runtime O( sqrt(n) ), Memory O(1) 

if __name__ == "__main__":
    while True:
        userInput = int(input('> '))
        print(is_prime(userInput))

# 20 for example
# First num to be greater than sqrt(20) is 5 
# In order for 20 to be not prime, 2 3 or 4 must be a factor
# 2 is a factor, 4 is a factor 

# 121 for example 
# first num to be GREATER than sqrt(121) is 12
# In order for 121 to be not prime, 2,3,4,5,6,7,8,9,10,11 must be a factor. 
# 11 is a factor 

# 17 for example
# first num to be greater than sqrt(17) is 5
# in order for 17 to be not prime 2,3,4 must be a factor 
# None are factors, 17 is prime and we only checked 3 numbers instead of 17