# a. parameter choices
sigma = 3.14
omega = 2
N = 10000
np.random.seed(1986)

# b. draw random numbers
x = np.random.normal(loc=0, scale=sigma, size=N)

# c. transformation function


def g(x, omega):
    y = x.copy()
    y[x < -omega] = -omega
    y[x > omega] = omega
    return y


# d. mean and variance
mean = np.mean(g(x, omega))
var = np.var(g(x-mean, omega))
print(f'mean = {mean:.5f}, var = {var:.5f}')
