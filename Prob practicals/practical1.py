import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Set parameters for the Binomial distribution
n = 45  # Number of trials
p = 0.5  # Probability of success

# Generate data points for the distribution
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

# Plot the Binomial distribution
plt.bar(x, pmf, align='center', alpha=0.7, label='Binomial PMF')
plt.title('Binomial Distribution')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.legend()
plt.show()

