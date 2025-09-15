"""
Simple Linear Regression Model Definition with TensorFlow/Keras
This script demonstrates how to define a simple linear regression model
using TensorFlow/Keras and save the model architecture.
"""

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

from tensorflow import keras

# Create a simple sequential model for linear regression
model = keras.Sequential([
    keras.layers.Dense(1, input_shape=(1,), name='linear_layer')
])

# Compile the model
model.compile(
    optimizer='sgd',
    loss='mean_squared_error'
)

# Display model architecture
print("Model Architecture:")
model.summary()

# Save the model architecture (without training)
model.save('linear_regression_model_untrained.h5')
print("\nUntrained model saved as 'linear_regression_model_untrained.h5'")

# Also save in the native Keras format
model.save('linear_regression_model_untrained.keras')
print("Untrained model saved in native Keras format as 'linear_regression_model_untrained.keras'")

print("\nScript completed successfully!")