print('Nelder-Mead:')
evals = 0
result = optimize.minimize(f_python,x0,method='Nelder-Mead',callback=collect,options={'disp':True})
contour()