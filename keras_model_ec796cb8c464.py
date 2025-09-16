import tensorflow as tf
from tensorflow import keras

# Create a Keras model with exactly one dense layer
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(10,))  # Single dense layer with 32 units
])

# Compile the model
model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])

# Display model summary
model.summary()

# Save the model in SavedModel format
model.save('single_dense_layer_model')

# Also save in HDF5 format
model.save('single_dense_layer_model.h5')

print("Model with one dense layer created and saved successfully!")
