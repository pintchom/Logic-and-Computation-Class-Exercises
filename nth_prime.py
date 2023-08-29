
def nth_prime(n):
    primes = [2] #Minimum prime numbers to check for is 1 and 2 will always be the first prime number
    curNum = 2 #Starting the next from here
    while len(primes) < n:
        curNum += 1
        prime = True # determines whether added to primes output 
        for num in primes:
            if int((curNum/num)) == curNum/num: #if int(curNum/Num) == float(curNum/NUum)
                prime = False
                break # if this ever works, definitely not a prime number
        if prime:
            primes.append(curNum)
    return primes[-1]
        

        
if __name__ == "__main__":
    while True:
        userInput = int(input('> '))
        if userInput == 0: #program stops when 0 inputted or program stopped
            break
        print(nth_prime(userInput))