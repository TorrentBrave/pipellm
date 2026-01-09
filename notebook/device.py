import torch

# PyTorch 版本
print("Torch version:", torch.__version__)

# 是否是 CUDA 版本（带 GPU 支持）
print("CUDA available:", torch.cuda.is_available())

# 当前 CUDA 设备数量
print("Number of CUDA devices:", torch.cuda.device_count())

# 当前默认设备名称
if torch.cuda.is_available():
    print("Current CUDA device:", torch.cuda.get_device_name(torch.cuda.current_device()))

