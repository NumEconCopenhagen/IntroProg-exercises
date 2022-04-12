ss_func = sm.lambdify((s,g,n,delta,alpha),kss)

# Evaluate function
ss_func(0.2,0.02,0.01,0.1,1/3)