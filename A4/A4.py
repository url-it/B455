import numpy as np

# Given values
mu = np.array([[2], [3]])
Sigma = np.array([[1, 0.5], [0.5, 2]])
W = np.array([[1], [2]])

# Calculate the mean and covariance in the new space
mu_new = np.dot(W.T, mu)
Sigma_new = np.dot(np.dot(W.T, Sigma), W)

print("mu_new = ", mu_new)
print("Sigma_new = ", Sigma_new)