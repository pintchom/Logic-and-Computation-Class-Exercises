def nth_prime(n):
        
    primes = [2]
    curNum = 2

    while len(primes) < n:

        add = True
        curNum += 1

        for prime in primes:
            if curNum%prime == 0:
                add = False
                break

        if add: primes.append(curNum)

    return primes[-1]

if __name__ == "__main__":
        
    while True:
        userInput = int(input('> '))
        print(nth_prime(userInput))