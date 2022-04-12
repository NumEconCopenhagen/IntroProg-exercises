for beta in betas:
    f = lambda k: (alpha*k**beta + (1-alpha))**(1/beta)
    obj_kss = lambda kss: kss - (s*f(kss) + (1-delta)*kss)/((1+g)*(1+n))
    result = optimize.root_scalar(obj_kss,bracket=[0.1,100],method='brentq')
    print(f'for beta = {beta:.3f} the steady state for k is',result.root) 