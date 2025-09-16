import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.random.randn(100, 1).astype(np.float32)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1).astype(np.float32)

# Create TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
history = model.fit(X, y, epochs=10, verbose=0)

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Data')
plt.plot(X, model.predict(X), color='red', label='Prediction')
plt.legend()
plt.title('Linear Regression with TensorFlow')
plt.xlabel('X')
plt.ylabel('y')
plt.savefig('linear_regression_plot.png')

# Save the model
model.save('linear_regression_model.h5')

print("Model training completed and saved.")
print(f"Final loss: {history.history['loss'][-1]:.4f}")