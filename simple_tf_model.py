import tensorflow as tf
import numpy as np

# Create a simple linear regression model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Generate some sample data
X = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Train the model for just 1 epoch to verify it works
model.fit(X, y, epochs=1, verbose=0)

# Save the model
model.save('simple_linear_regression_model.h5')

print("Simple TensorFlow linear regression model created and saved successfully!")