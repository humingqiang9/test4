import tensorflow as tf
import numpy as np

# Generate some sample data for linear regression
# y = 2*x + 1 + noise
np.random.seed(42)
x_data = np.random.randn(100).astype(np.float32)
y_data = 2 * x_data + 1 + 0.1 * np.random.randn(100).astype(np.float32)

# Create TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices((x_data, y_data))
dataset = dataset.batch(10)

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

# Display model summary
print("Model Summary:")
model.summary()

# Train the model
print("\nTraining the model...")
history = model.fit(dataset, epochs=100, verbose=0)

# Evaluate the model
print("\nModel trained!")
print(f"Final loss: {history.history['loss'][-1]}")

# Make a prediction
sample_x = tf.constant([[1.0]])
prediction = model.predict(sample_x)
print(f"\nPrediction for x=1.0: {prediction[0][0]}")

# Save the model
model.save('linear_regression_model.h5')
print("\nModel saved as 'linear_regression_model.h5'")