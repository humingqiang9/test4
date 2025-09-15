"""
TensorFlow Linear Regression Model - Complete Example
This script demonstrates how to:
1. Define a simple linear regression model
2. Save the model
3. Load the model
4. Use the model for predictions
"""

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

from tensorflow import keras
import numpy as np

def create_and_save_model():
    """Create a simple linear regression model and save it."""
    print("Creating linear regression model...")
    
    # Create model
    model = keras.Sequential([
        keras.layers.Dense(1, input_shape=(1,), name='linear_layer')
    ])
    
    # Compile model
    model.compile(optimizer='sgd', loss='mean_squared_error')
    
    # Display model architecture
    print("Model Architecture:")
    model.summary()
    
    # Save model in both formats
    model.save('linear_regression_model.h5')
    model.save('linear_regression_model.keras')
    
    print("\nModel saved in two formats:")
    print("- HDF5 format: 'linear_regression_model.h5'")
    print("- Native Keras format: 'linear_regression_model.keras'")
    
    return model

def load_and_use_model():
    """Load the saved model and demonstrate its usage."""
    print("\n" + "="*50)
    print("Loading and using the saved model...")
    
    # Load model from HDF5 format
    print("\nLoading model from HDF5 format...")
    loaded_model_h5 = keras.models.load_model('linear_regression_model.h5')
    
    # Load model from Keras format
    print("Loading model from Keras format...")
    loaded_model_keras = keras.models.load_model('linear_regression_model.keras')
    
    # Demonstrate predictions with both models
    print("\nMaking predictions with loaded models...")
    test_input = np.array([[1.0], [2.0], [3.0]], dtype=np.float32)
    
    predictions_h5 = loaded_model_h5.predict(test_input, verbose=0)
    predictions_keras = loaded_model_keras.predict(test_input, verbose=0)
    
    print(f"Input values: {test_input.flatten()}")
    print(f"Predictions (HDF5 model): {predictions_h5.flatten()}")
    print(f"Predictions (Keras model): {predictions_keras.flatten()}")
    
    # Show model weights
    print("\nModel weights from HDF5 model:")
    weights, bias = loaded_model_h5.layers[0].get_weights()
    print(f"Weight: {weights[0][0]:.4f}")
    print(f"Bias: {bias[0]:.4f}")

def main():
    """Main function to run the complete example."""
    print("TensorFlow Linear Regression Model Example")
    print("="*50)
    
    # Create and save model
    model = create_and_save_model()
    
    # Load and use model
    load_and_use_model()
    
    print("\n" + "="*50)
    print("Example completed successfully!")

if __name__ == "__main__":
    main()