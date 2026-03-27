#!/bin/bash

N="1000"
N_TASK="128"

echo "VM1: vCPUs = 2"
vagrant ssh vm1 -c "python3 ./source/cpu_workload.py 4 ${N} ${N_TASK}"

echo ===========

echo "VM1: vCPUs = 4"
vagrant ssh vm2 -c "python3 ./source/cpu_workload.py 4 ${N} ${N_TASK}"
