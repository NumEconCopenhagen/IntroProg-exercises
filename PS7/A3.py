_f1 = sm.lambdify((x1,x2),f1)
_f2 = sm.lambdify((x1,x2),f2)
_f11 = sm.lambdify((x1,x2),f11)
_f12 = sm.lambdify((x1,x2),f12)
_f21 = sm.lambdify((x1,x2),f21)
_f22 = sm.lambdify((x1,x2),f22)

def f_jac(x):
    return np.array([_f1(x[0],x[1]),_f2(x[0],x[1])])

def f_hess(x):
    row1 = [_f11(x[0],x[1]),_f12(x[0],x[1])]
    row2 = [_f21(x[0],x[1]),_f22(x[0],x[1])]
    return np.array([row1,row2])
