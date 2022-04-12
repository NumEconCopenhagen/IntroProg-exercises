def linear_search(L,x):
    
    # a. prep
    i = 0
    N = len(L)
    found = False

    # b. main
    while i < N-1 and not found:
        if x >= L[i] and x < L[i+1]: # comparison
            found = True
        else:
            i += 1 # increment

    # c. return
    return i
