import torch

print("PyTorch Version:", torch.__version__)

# Create a tensor
x = torch.rand(3, 3)

print("My First Tensor:")
print(x)

# Check GPU availability
print("MPS Available:", torch.backends.mps.is_available())