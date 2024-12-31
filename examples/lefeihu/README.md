# README

## Docker 方式

### build

```mermaid
docker build -t dreambooth:latest .
```

### run
```mermaid
docker run 
    -v /cfs/.cache/huggingface/hub:/cfs/.cache/huggingface/hub 
    --runtime=nvidia dreambooth:latest 
    python helloworld2.py
```

## Conda 方式
### 安装python库

```ipynb
#@title Install the required libs

!pip install -U -qq git+https://github.com/huggingface/diffusers.git
!pip install -qq accelerate tensorboard transformers ftfy gradio
!pip install -qq "ipywidgets>=7,<8"
!pip install -qq bitsandbytes
```

```jupyter
#@title [Optional] Install xformers for faster and memory efficient training

!pip install -U --pre triton
!pip install -U xformers --index-url https://download.pytorch.org/whl/cu121
```

```mermaid
pip install sentencepiece
```