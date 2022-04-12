LU,piv = linalg.lu_factor(A) # only done once
xb = linalg.lu_solve((LU,piv),b) # much faster than regular solve
xc = linalg.lu_solve((LU,piv),c)
xd = linalg.lu_solve((LU,piv),d)
print('b:',xb)
print('c:',xc)
print('d:',xd)