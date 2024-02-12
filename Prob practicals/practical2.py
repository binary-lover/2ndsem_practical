import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multinomial

# Set seed for reproducibility
np.random.seed(42)

# Generate random Multinomial distribution data
num_samples = 1000
probabilities = [0.2, 0.3, 0.5]  # Adjust the probabilities as needed
data = np.random.multinomial(1, probabilities, size=num_samples)

# Plotting the Multinomial distribution
plt.figure(figsize=(8, 6))
plt.bar(range(len(probabilities)), np.sum(data, axis=0) / num_samples, color='blue', alpha=0.7, label='Sampled Distribution')
plt.plot(range(len(probabilities)), probabilities, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=8, label='True Distribution')
plt.xlabel('Categories')
plt.ylabel('Probabilities')
plt.title('Multinomial Distribution')
plt.xticks(range(len(probabilities)))
plt.legend()
plt.show()

# Fitting the Multinomial distribution
fit_params = multinomial.fit(data, n=1)
fit_probabilities = fit_params[0]

# Display fitted probabilities
print("Fitted Probabilities:", fit_probabilities)
