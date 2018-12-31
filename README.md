## Udacity Machine Learning NanoDegree - Finding Donors Project

Original github material is [here](https://github.com/udacity/machine-learning/tree/master/projects/finding_donors)

This is the initial commit to setup the project structure. More coming soon!

### Continuous Integration

## Build Status

[![CircleCI](https://circleci.com/gh/jerowe/udacity-finding-donors/tree/master.svg?style=svg)](https://circleci.com/gh/jerowe/udacity-finding-donors/tree/master)

CI is at at [CircleCI](https://circleci.com/gh/jerowe/udacity-finding-donors)

## Bring up the local server

```
docker-compose up --build -d
```

```
curl -X POST \
    http://localhost:5000/health \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/json' \
    -d '{"hello": "world"}'
curl -X GET \
    http://localhost:5000\
    -H 'Cache-Control: no-cache'
```