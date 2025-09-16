import torch
import torch.nn as nn
import torch.nn.functional as F

class PyTorchBinaryClassifier(nn.Module):
    """
    A PyTorch neural network model for binary classification.
    This implementation uses a different architecture with batch normalization.
    """
    def __init__(self, input_dim, hidden_dims, dropout_rate=0.3):
        """
        Initialize the binary classifier.
        
        Args:
            input_dim (int): Number of input features
            hidden_dims (list): List of hidden layer sizes
            dropout_rate (float): Dropout rate for regularization
        """
        super(PyTorchBinaryClassifier, self).__init__()
        
        # Create layers dynamically based on hidden_dims
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, hidden_dim))
            layers.append(nn.BatchNorm1d(hidden_dim))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout_rate))
            prev_dim = hidden_dim
            
        # Output layer
        layers.append(nn.Linear(prev_dim, 1))
        layers.append(nn.Sigmoid())
        
        # Combine all layers into a sequential model
        self.network = nn.Sequential(*layers)
        
    def forward(self, x):
        """
        Forward pass through the network.
        
        Args:
            x (Tensor): Input tensor of shape (batch_size, input_dim)
            
        Returns:
            Tensor: Output tensor of shape (batch_size, 1)
        """
        return self.network(x)

# Example usage
if __name__ == "__main__":
    # Define model parameters
    input_dimension = 20
    hidden_layers = [128, 64, 32]
    
    # Create model instance
    model = PyTorchBinaryClassifier(input_dimension, hidden_layers)
    
    # Create sample data
    batch_size = 16
    sample_data = torch.randn(batch_size, input_dimension)
    
    # Forward pass
    predictions = model(sample_data)
    
    # Print model information
    print(f"Model architecture:\n{model}")
    print(f"\nInput shape: {sample_data.shape}")
    print(f"Output shape: {predictions.shape}")
    print(f"Sample predictions: {predictions.flatten()[:5]}...")