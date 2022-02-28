import itertools as it

N = 15 # number of points in each dimension
fac = np.linspace(0,1,N) # vector betweein 0 and 1
x_max = I/p # maximum x so E = I

x_best = np.empty(5)
u_best = -np.inf
for x in it.product(fac,fac,fac,fac,fac):
    x *= x_max
    E = expenditures(x,p)
    if E <= I:
        u_now = utility_function(x,alpha)
        if u_now > u_best:
            x_best = x
            u_best = u_now
          
print_solution(x_best,alpha,I,p)     