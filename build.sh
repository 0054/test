#!/bin/bash

docker rm -f api || true
docker rmi flask_app || true
docker build -t flask_app /tmp/build
