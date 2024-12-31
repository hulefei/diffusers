echo start docker...

docker build -t dreambooth:latest .

#docker run --runtime=nvidia dreambooth:latest nvidia-smi
docker run -v /cfs/.cache/huggingface/hub:/cfs/.cache/huggingface/hub --runtime=nvidia dreambooth:latest python helloworld2.py
