#!/bin/bash
# bash script to build and run the classifier
docker build -t mlops_bin_classifier . && docker run -d -p 9200:9200 mlops_bin_classifier
