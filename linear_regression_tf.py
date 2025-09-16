import tensorflow as tf
import numpy as np

# Generate some sample data
np.random.seed(42)
X = np.random.randn(100, 1).astype(np.float32)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1).astype(np.float32)

# Create a TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices((X, y))
dataset = dataset.shuffle(buffer_size=100).batch(32)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(
    optimizer='sgd',
    loss='mean_squared_error',
    metrics=['mean_absolute_error']
)

# Train the model
history = model.fit(dataset, epochs=100, verbose=0)

# Print final loss
print(f"Final loss: {history.history['loss'][-1]}")

# Save the model
model.save('linear_regression_model.h5')
print("Model saved as 'linear_regression_model.h5'")