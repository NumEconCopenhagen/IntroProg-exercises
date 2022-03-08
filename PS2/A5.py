# a. parameters
N = 10000
mu = 0.5
sigma = 0.2
mu_low = 0.1
mu_high = 0.9
beta1 = 1.3
beta2 = 2.1
seed = 1986

# b. draws of random numbers
np.random.seed(seed)
alphas = np.random.normal(loc=mu, scale=sigma, size=N)
alphas = np.fmax(np.fmin(alphas, mu_high), mu_low)
e1 = np.random.exponential(beta1, size=N)
e2 = np.random.exponential(beta2, size=N)

# c. demand function


def demand_good_1_func(alpha, p1, p2, e1, e2):
    I = p1*e1+p2*e2
    return alpha*I/p1

# d. excess demand function


def excess_demand_good_1_func(alphas, p1, p2, e1, e2):

    # a. demand
    demand = np.sum(demand_good_1_func(alphas, p1, p2, e1, e2))

    # b. supply
    supply = np.sum(e1)

    # c. excess demand
    excess_demand = demand-supply

    return excess_demand

# e. find equilibrium function


def find_equilibrium(alphas, p1, p2, e1, e2, kappa=0.5, eps=1e-8, maxiter=500):

    t = 0
    while True:

        # a. step 1: excess demand
        Z1 = excess_demand_good_1_func(alphas, p1, p2, e1, e2)

        # b: step 2: stop?
        if np.abs(Z1) < eps or t >= maxiter:
            print(f'{t:3d}: p1 = {p1:12.8f} -> excess demand -> {Z1:14.8f}')
            break

        # c. step 3: update p1
        p1 = p1 + kappa*Z1/alphas.size

        # d. step 4: return
        if t < 5 or t % 25 == 0:
            print(f'{t:3d}: p1 = {p1:12.8f} -> excess demand -> {Z1:14.8f}')
        elif t == 5:
            print('   ...')

        t += 1

    return p1


# f. call find equilibrium function
p1 = 1.4
p2 = 1
kappa = 0.5
eps = 1e-8
p1 = find_equilibrium(alphas, p1, p2, e1, e2, kappa=kappa, eps=eps)
