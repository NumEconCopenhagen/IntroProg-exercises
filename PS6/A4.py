import numecon_linalg
Y = np.column_stack((F,e))
numecon_linalg.gauss_jordan(Y)
print('solution',Y[:,-1])
assert np.allclose(F@Y[:,-1],e)