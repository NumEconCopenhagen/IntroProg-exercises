def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
for n in [1,2,3,4,5]:
    y = factorial(n)
    print(f'the factorial of {n} is {y}')
    assert(y == math.factorial(n))