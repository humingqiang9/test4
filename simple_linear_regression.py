"""
Simple Linear Regression with TensorFlow/Keras
This script demonstrates how to build and train a simple linear regression model
using TensorFlow/Keras and save the trained model.
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np

# Generate synthetic data for linear regression
# y = 2*x + 1 + noise
np.random.seed(42)
X = np.random.randn(100, 1).astype(np.float32)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1).astype(np.float32)

# Create a simple sequential model
model = keras.Sequential([
    keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model with optimizer, loss function and metrics
model.compile(
    optimizer='sgd',  # Stochastic Gradient Descent
    loss='mean_squared_error',
    metrics=['mean_absolute_error']
)

# Display model architecture
print("Model Architecture:")
model.summary()

# Train the model
print("\nTraining the linear regression model...")
history = model.fit(X, y, epochs=100, verbose=0)

# Evaluate the model
print("Model trained!")
loss, mae = model.evaluate(X, y, verbose=0)
print(f"Final loss (MSE): {loss:.6f}")
print(f"Mean Absolute Error: {mae:.6f}")

# Show learned parameters
weights, bias = model.layers[0].get_weights()
print(f"Learned weight: {weights[0][0]:.4f} (Expected: 2.0)")
print(f"Learned bias: {bias[0]:.4f} (Expected: 1.0)")

# Save the model
model.save('linear_regression_model.h5')
print("\nModel saved as 'linear_regression_model.h5'")

# Demonstrate loading the model
print("\nLoading the model...")
loaded_model = keras.models.load_model('linear_regression_model.h5')
loaded_weights, loaded_bias = loaded_model.layers[0].get_weights()
print(f"Loaded weight: {loaded_weights[0][0]:.4f}")
print(f"Loaded bias: {loaded_bias[0]:.4f}")

print("\nScript completed successfully!")