import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
X = np.random.randn(100, 1)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)

# Add bias term (intercept)
X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance

# Calculate optimal parameters using Normal Equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Print parameters
print(f"Intercept: {theta_best[0][0]:.4f}")
print(f"Slope: {theta_best[1][0]:.4f}")

# Make predictions
X_new = np.array([[-2], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_best)

# Plot results
plt.scatter(X, y, label='Data')
plt.plot(X_new, y_predict, "r-", label='Prediction')
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# Save parameters to file
np.savetxt('linear_regression_params.txt', theta_best)
print("Model parameters saved to 'linear_regression_params.txt'")