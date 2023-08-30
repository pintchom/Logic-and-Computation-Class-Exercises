

def is_prime(n):
    primes = [2]
    curNum = 2
    while curNum < n:
        curNum += 1
        add = True 
        for prime in primes:
            if int((curNum/prime)) == curNum/prime: #if int(curNum/Num) == float(curNum/NUum)
                add = False
                break
        if add: primes.append(curNum)
    if primes[-1] == n: return True 
    return False


if __name__ == "__main__":
    print("\n> Enter -1 to quit <")
    while True:
        userInput = int(input('> '))
        if userInput == -1: break
        print(is_prime(userInput))

