# a. define objective function
def unconstrained_objective(x,alpha,I,p):
    
    penalty = 0
    E = expenditures(x,p)
    if E >= I:
        ratio = I/E
        x *= ratio # now p*x = I
        penalty = 1000*(E-I)**2
    
    u = utility_function(x,alpha)
    return -u + penalty 
    # note: 
    #  "-u" because we are minimizing
    #  "+ penalty" because the minimizer 
    #   will then avoid the E > I

# b. call optimizer
initial_guess = (I/p)/6
res = optimize.minimize(
    unconstrained_objective,initial_guess,
    method='Nelder-Mead',args=(alpha,I,p),options={'maxiter':5000},tol=1e-10)

print(res.message)

# c. print result
print_solution(res.x,alpha,I,p)   