echo test

docker build -t test:latest .
#docker run --runtime=nvidia dreambooth:latest nvidia-smi
#docker run --runtime=nvidia dreambooth:latest python helloworld2.py
docker run -v /cfs/.cache/huggingface/hub:/cfs/.cache/huggingface/hub test