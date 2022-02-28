# a. contraint function (negative if violated)
constraints = ({'type': 'ineq', 'fun': lambda x:  I-expenditures(x,p)})
bounds = [(0,I/p_now) for p_now in p]

# b. call optimizer
initial_guess = (I/p)/6 # some guess, should be feasible
res = optimize.minimize(
    lambda x: -utility_function(x,alpha),initial_guess,
    method='SLSQP',bounds=bounds,constraints=constraints)

print(res.message) # check that the solver has terminated correctly

# c. print result
print_solution(res.x,alpha,I,p)