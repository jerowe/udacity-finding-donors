## Udacity Machine Learning NanoDegree - Finding Donors Project

Original github material is [here](https://github.com/udacity/machine-learning/tree/master/projects/finding_donors)

Site deployed to AWS is [here](http://jerowe-udacity-finding-donors.us-east-2.elasticbeanstalk.com/#/home)

Python notebook is [here](https://github.com/jerowe/udacity-finding-donors/blob/master/finding_donors_flask_app/materials/finding_donors.ipynb)
Python notebook exported as html is [here](https://github.com/jerowe/udacity-finding-donors/blob/master/finding-donors-flask-app/nginx/finding_donors.html)
And [here](https://github.com/jerowe/udacity-finding-donors/blob/master/report.html)

Python notebook exported to html is [here](http://jerowe-udacity-finding-donors.us-east-2.elasticbeanstalk.com/finding_donors.html)

## Blog Post

If you're interested in how I configured the different web services to deploy with AWS, check out my [blog post here](https://dabble-of-devops.com/deploy-a-full-stack-web-application-with-docker-and-traefik/).

### Continuous Integration

## Build Status

[![CircleCI](https://circleci.com/gh/jerowe/udacity-finding-donors/tree/master.svg?style=svg)](https://circleci.com/gh/jerowe/udacity-finding-donors/tree/master)

CI is at at [CircleCI](https://circleci.com/gh/jerowe/udacity-finding-donors)

## Bring up the local server

```
docker-compose up --build -d
```

### Health Endpoints

There are two health methods up. They don't actually do anything besides verify the server is hunky dory.

```
curl -X POST \
    http://localhost/server/health \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/json' \
    -d '{"hello": "world"}'
```

```
curl -X GET \
    http://localhost/server \
    -H 'Cache-Control: no-cache'
```

### Data Endpoints

```
curl -X GET \
    http://localhost/server/read-data \
    -H 'Cache-Control: no-cache'
```
