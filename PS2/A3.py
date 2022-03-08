# a. import
import ipywidgets as widgets
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# b. plotting figure


def fitting_normal(X, mu_guess, sigma_guess):

    # i. normal distribution from guess
    F = norm(loc=mu_guess, scale=sigma_guess)

    # ii. x-values
    x_low = F.ppf(0.001)  # x value where cdf is 0.001
    x_high = F.ppf(0.999)  # x value where cdf is 0.999
    x = np.linspace(x_low, x_high, 100)

    # iii. figure
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, F.pdf(x), lw=2)
    ax.hist(X, bins=100, density=True, histtype='stepfilled')
    ax.set_ylim([0, 0.5])
    ax.set_xlim([-6, 6])


# c. parameters
mu_true = 2
sigma_true = 1
mu_guess = 1
sigma_guess = 2

# d. figure
X = np.random.normal(loc=mu_true, scale=sigma_true, size=10**6)
#fitting_normal(X,mu_guess,sigma_guess)

widgets.interact(fitting_normal,
                 X=widgets.fixed(X),
                 mu_guess=widgets.FloatSlider(
                     description="$\mu$", min=0.1, max=5, step=0.05, value=1),
                 sigma_guess=widgets.FloatSlider(
                     description="$\sigma$", min=0.1, max=5, step=0.05, value=1)
)
