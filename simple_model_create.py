import tensorflow as tf
from tensorflow import keras
import numpy as np

# Create a simple linear regression model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Print model summary
model.summary()

# Save the untrained model
model.save('untrained_linear_regression_model.h5')

print("Simple TensorFlow linear regression model created and saved successfully!")