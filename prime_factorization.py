
def prime_factorization(n):

    factors = [] # save factors while moving 
    curNum = 2
    while curNum ** 2 <= n: # minimum factor is 2, and maximum factor is sqrt(N) 

        while n%curNum==0: # while instead of if since it could be the same factor many times
            factors.append(curNum)
            n = int(n/curNum)
        curNum += 1

    if n != 1: factors.append(n) # appending the last prime number if left. 1 means n was divided down as far down as possible

    return factors
    
if __name__ ==  "__main__":
    while True:
        userInput = int(input('> '))
        print(prime_factorization(userInput))