def sieve(n):
    """ sieve of Eratosthenes
    
    Return all primes between 2 and n.
    
    Args:
    
        n (integer): maximum number to consider
    
    """
    
    # a. step 1: create list of potential primes
    primes = list(range(2,n+1))
    
    # b. step 2: initialize i
    index = 0
    i = primes[index]
    
    # c. step 3-6
    while i < math.sqrt(n):
            
        # step 3: remove
        k = i
        while i <= n:
            i += k
            if i in primes:
                primes.remove(i)
             
        # step 4: next number
        index += 1
        
        # step 5: set i
        i = primes[index]
        
    return primes

print('primes from 2 to 100:',sieve(100))