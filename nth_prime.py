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

def nth_prime(n):
    
    primes = [2]
    curNum = 2

    while len(primes) < n:

        curNum += 1
        if is_prime(curNum): primes.append(curNum)

    return primes[-1] # Runtime O( n sqrt(n) ) Memory O(n?)

if __name__ == "__main__":
        
    while True:
        userInput = int(input('> '))
        print(nth_prime(userInput))