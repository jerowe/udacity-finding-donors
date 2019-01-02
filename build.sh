#!/usr/bin/env bash

set -x -e
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

