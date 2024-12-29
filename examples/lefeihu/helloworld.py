# from diffusers import DiffusionPipeline
import os
import subprocess

import torch
#
# pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
# pipeline.to("cuda")
# pipeline("An image of a squirrel in Picasso style").images[0]

# 查看cuda
# if torch.cuda.is_available():
#     print("CUDA 可用")
#     print("CUDA 版本:", torch.version.cuda)
# else:
#     print("CUDA 不可用")

from diffusers import StableDiffusionPipeline

# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a <cat-toy> in mad max fury road"
image = pipe(prompt).images[0]

# 保存图像到本地文件
output_path = "output_image.png"
image.save(output_path)
print(f"图像已保存到: {output_path}")

# from diffusers import StableDiffusionPipeline
#
# pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
# print(pipeline.config)
#
# import os
# print(os.environ.get("HF_HOME", "none"))



