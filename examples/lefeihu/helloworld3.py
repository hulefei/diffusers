import os

import torch
print(torch.cuda.is_available())  # 如果返回 False，表示没有 GPU 支持
print(torch.version.cuda)         # 检查 PyTorch 编译时使用的 CUDA 版本

print(os.environ.get('HF_HOME'))