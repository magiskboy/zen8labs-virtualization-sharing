#!/bin/bash

URL=$1

echo "VM2 - vCPUs = 4"
vagrant ssh vm2 -c "wrk -c 2 -t 2 --timeout 60 -d 60s ${URL}"

echo "VM1 - vCPUs = 2"
vagrant ssh vm1 -c "wrk -c 2 -t 2 --timeout 60 -d 60s ${URL}"

