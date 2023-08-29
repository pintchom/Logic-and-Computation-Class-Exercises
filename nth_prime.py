
def nth_prime(n):
    primes = [2]
    curNum = 2
    while len(primes) < n:
        curNum += 1
        prime = True
        for num in primes:
            if int((curNum/num)) == curNum/num:
                prime = False
                break 
        if prime:
            primes.append(curNum)
    return primes[-1]
        

        
if __name__ == "__main__":
    while True:
        userInput = int(input('> '))
        if userInput == 0:
            break
        print(nth_prime(userInput))