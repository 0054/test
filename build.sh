#!/bin/bash

docker rmi flask_app || true
docker build -t flask_app /tmp/build
