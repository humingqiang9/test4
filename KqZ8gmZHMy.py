import torch
import torch.nn as nn
import torch.nn.functional as F

class BinaryClassificationNet(nn.Module):
    """
    A simple neural network for binary classification tasks.
    """
    def __init__(self, input_size, hidden_size1=64, hidden_size2=32):
        """
        Initialize the network layers.
        
        Args:
            input_size (int): Number of input features
            hidden_size1 (int): Number of neurons in the first hidden layer
            hidden_size2 (int): Number of neurons in the second hidden layer
        """
        super(BinaryClassificationNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.fc3 = nn.Linear(hidden_size2, 1)
        self.dropout = nn.Dropout(0.2)
        
    def forward(self, x):
        """
        Forward pass through the network.
        
        Args:
            x (Tensor): Input tensor of shape (batch_size, input_size)
            
        Returns:
            Tensor: Output tensor of shape (batch_size, 1) with sigmoid activation
        """
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        x = torch.sigmoid(x)
        return x

# Example usage:
# model = BinaryClassificationNet(input_size=10)
# input_data = torch.randn(32, 10)  # batch of 32 samples with 10 features each
# output = model(input_data)
# print(output.shape)  # Should be torch.Size([32, 1])