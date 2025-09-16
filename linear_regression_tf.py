import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
X = np.random.normal(0, 1, (1000, 1))
y = 2 * X + 1 + np.random.normal(0, 0.1, (1000, 1))

# Create TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

# Train the model
history = model.fit(X, y, epochs=100, verbose=0)

# Evaluate the model
loss = model.evaluate(X, y, verbose=0)
print(f"Final loss: {loss}")

# Plot the results
plt.scatter(X, y, alpha=0.5, label='Data')
plt.plot(X, model.predict(X), color='red', label='Prediction')
plt.legend()
plt.show()

# Save the model
model.save('linear_regression_model.h5')
print("Model saved as 'linear_regression_model.h5'")