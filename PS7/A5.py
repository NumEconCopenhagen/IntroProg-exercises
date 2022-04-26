print('BFGS without analytical gradient:')

evals = 0
result = optimize.minimize(f_python,x0,method='BFGS',callback=collect,options={'disp':True})
contour()