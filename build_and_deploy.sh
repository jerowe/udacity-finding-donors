#!/usr/bin/env bash

set -x -e
## This script relies on having already logged into docker with 'docker login'
## Building is a 2 step process
## Run an initial docker-compose build
## Build the angular interface
## And then rebuild the nginx interface

mkdir -p finding-donors-web-app/nginx/html/
mkdir -p finding-donors-web-app/nginx/html/t

docker-compose build --force-rm

# Build the front end angular interface
cd finding-donors-web-app
rm -rf nginx/html/*
docker run -it -v $(pwd):/app:z finding-donors_angular6-build ng build --prod  --output-hashing none --configuration=production --output-path ./nginx/html
cd ..

docker-compose build --force-rm

### Tag the docker images
docker tag finding-donors_udacity-finding-donors-server quay.io/jerowe/udacity-finding-donors-server:latest
docker tag finding-donors_udacity-finding-donors-client quay.io/jerowe/udacity-finding-donors-client:latest

# Docker login
#echo ${QUAY_API_TOKEN} | docker login quay.io -u jerowe  --password-stdin
docker login quay.io -u jerowe  -p ${QUAY_API_TOKEN}

# Push to quay
docker push quay.io/jerowe/udacity-finding-donors-server:latest
docker push quay.io/jerowe/udacity-finding-donors-client:latest
