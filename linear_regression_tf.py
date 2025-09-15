import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

import numpy as np

# Generate some sample data
np.random.seed(42)
X = np.random.randn(100, 1).astype(np.float32)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1).astype(np.float32)

# Create TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices((X, y))
dataset = dataset.shuffle(buffer_size=100).batch(32)

# Define model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile model
model.compile(
    optimizer='sgd',
    loss='mean_squared_error',
    metrics=['mean_absolute_error']
)

# Train model
print("Training the linear regression model...")
model.fit(dataset, epochs=100, verbose=0)

# Evaluate model
print("Model trained!")
print(f"Final loss: {model.evaluate(dataset, verbose=0)[0]}")

# Save model
model.save('linear_regression_model.h5')
print("Model saved as 'linear_regression_model.h5'")