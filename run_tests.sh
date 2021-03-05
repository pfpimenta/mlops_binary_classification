#!/bin/bash
# bash script to run the tests on the API

# build docker container
sh docker_build.sh

# run tests
pytest tests/

# remove docker container
docker rm -f mlops_bin_classifier
