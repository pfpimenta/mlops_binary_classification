#!/bin/bash
# bash script to build and run the classifier
docker rm -f mlops_bin_classifier
docker build -t mlops_bin_classifier .
docker run -d --name mlops_bin_classifier -p 9200:9200 mlops_bin_classifier 
