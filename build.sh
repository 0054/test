#!/bin/bash

docker rm -f flask_app || true
docker build -t flask_app /tmp/build
