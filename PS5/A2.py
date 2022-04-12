def swap(L,i,j):
    temp = L[i] # save value at i
    L[i] = L[j] # overwrite value at i with value at j
    L[j] = temp # write original value at i to value at j
    
def bubble_sort(L):   
    for k in range(len(L)-1,0,-1):
        for i in range(k):
            if L[i] < L[i+1]:
                swap(L,i,i+1)
                
