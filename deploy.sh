#!/usr/bin/env bash
set -x -e

### Tag the docker images
docker tag finding-donors_udacity-finding-donors-server quay.io/jerowe/udacity-finding-donors-server:latest
docker tag finding-donors_udacity-finding-donors-client quay.io/jerowe/udacity-finding-donors-client:latest

docker tag finding-donors_udacity-finding-donors-server quay.io/jerowe/udacity-finding-donors-server:1.1
docker tag finding-donors_udacity-finding-donors-client quay.io/jerowe/udacity-finding-donors-client:1.1


# Docker login
#echo ${QUAY_API_TOKEN} | docker login quay.io -u jerowe  --password-stdin
docker login quay.io -u jerowe  -p ${QUAY_API_TOKEN}

# Push to quay
docker push quay.io/jerowe/udacity-finding-donors-server:latest
docker push quay.io/jerowe/udacity-finding-donors-client:latest

# Push versioned to quay
docker push quay.io/jerowe/udacity-finding-donors-server:1.1
docker push quay.io/jerowe/udacity-finding-donors-client:1.1
