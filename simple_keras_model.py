import numpy as np
import json

# Create a simple model representation using just NumPy
# This is a simplified representation of a dense layer with weights and biases

# Model parameters
input_size = 5
hidden_size = 10
output_size = 1

# Initialize weights and biases
np.random.seed(42)  # For reproducibility
W1 = np.random.randn(input_size, hidden_size) * 0.1
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.1
b2 = np.zeros((1, output_size))

# Model structure
model = {
    "layer1": {
        "weights": W1.tolist(),
        "biases": b1.tolist(),
        "activation": "relu"
    },
    "layer2": {
        "weights": W2.tolist(),
        "biases": b2.tolist(),
        "activation": "sigmoid"
    }
}

# Save model to JSON file
with open('simple_model.json', 'w') as f:
    json.dump(model, f)

print("Simple model created and saved to simple_model.json")
print(f"Model structure:")
print(f"  Input size: {input_size}")
print(f"  Hidden layer: {hidden_size} units with ReLU activation")
print(f"  Output layer: {output_size} unit with Sigmoid activation")