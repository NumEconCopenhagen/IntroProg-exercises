fopt = np.inf
xopt = np.nan
for i,x0 in enumerate(x0s):
    
    # a. optimize
    result = optimize.minimize(f_python,x0,method='BFGS')
    xs[i,:] = result.x
    fs[i] = result.fun
    
    # b. print first 20 or if better than seen yet
    if i < 20 or fs[i] < fopt: # plot 20 first or if improving
        if fs[i] < fopt:
            xopt = xs[i,:]
            fopt = fs[i]
        print(f'{i:4d}: x0 = ({x0[0]:6.2f},{x0[0]:6.2f})',end='')
        print(f' -> converged at ({xs[i][0]:6.2f},{xs[i][1]:6.2f}) with f = {fs[i]:.12f}')
        
# best solution
print(f'\nbest solution:\n x = ({xopt[0]:6.2f},{xopt[1]:6.2f}) -> f = {fopt:.12f}')