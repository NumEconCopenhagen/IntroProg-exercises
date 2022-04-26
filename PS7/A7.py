print('Newton-CG with analytical gradient and hessian:')

evals = 0
result = optimize.minimize(f_python,x0,jac=f_jac,hess=f_hess,method='Newton-CG',callback=collect,options={'disp':True})
contour()