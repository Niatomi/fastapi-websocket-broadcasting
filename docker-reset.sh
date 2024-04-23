#!/bin/bash

# Removed all the containers
docker rm -vf $(docker ps -aq)
# Removed all the images
docker rmi -f $(docker images -aq)
docker system prune --all --force
