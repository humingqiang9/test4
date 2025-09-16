import tensorflow as tf
from tensorflow import keras

# Create a simple Keras model with one dense layer
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(5,)),  # Dense layer with 10 units
    keras.layers.Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Display model summary
model.summary()

# Save the model architecture to a JSON file
model_json = model.to_json()
with open("model_architecture.json", "w") as json_file:
    json_file.write(model_json)

print("Model created and saved successfully!")
