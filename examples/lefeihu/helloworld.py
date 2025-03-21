from diffusers import DiffusionPipeline
import os
import subprocess

import torch
import hf_cache

# hf_cache.cache()

# 自动下载模型到缓存目录（默认路径：~/.cache/huggingface/hub）
pipe = DiffusionPipeline.from_pretrained(
    "hulefei/cat-toy",
    torch_dtype=torch.float16,  # FP16 模式节省显存
    # revision="fp16"             # 加载优化后的权重版本
).to("cuda")

pipeline = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")
image = pipeline("An image of a squirrel in Picasso style").images[0]
image.save("astronaut_rides_horse.png")

#
# 查看cuda
# if torch.cuda.is_available():
#     print("CUDA 可用")
#     print("CUDA 版本:", torch.version.cuda)
# else:
#     print("CUDA 不可用")

# from diffusers import StableDiffusionPipeline
#
# pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
# # pipe = StableDiffusionPipeline.from_pretrained("hulefei/cat-toy", torch_dtype=torch.float16)
# pipe = pipe.to("cuda")
# prompt = "a <cat-toy> in mad max fury road"
# image = pipe(prompt).images[0]
#
# # 保存图像到本地文件
# output_path = "output_image.png"
# image.save(output_path)
# print(f"图像已保存到: {output_path}")

# from diffusers import StableDiffusionPipeline
#
# pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
# print(pipeline.config)
#



