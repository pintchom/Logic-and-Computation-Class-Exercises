def is_prime(n):
    
    if n < 2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False 
    return True 
    

if __name__ == "__main__":

    while True:
        userInput = int(input('> '))
        print(is_prime(userInput))

