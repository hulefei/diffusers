echo prune docker...

echo prune container
docker container prune -f

echo prune image
docker image prune -f

echo ==========container==========
docker container ps -a

echo ==========images=============
docker images
