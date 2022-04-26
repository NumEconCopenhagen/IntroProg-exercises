print('BFGS with analytical gradient:')

evals = 0
result = optimize.minimize(f_python,x0,jac=f_jac,method='BFGS',callback=collect,options={'disp':True})
contour()