#!/bin/bash

vagrant ssh vm1 -c 'python3 ./source/memory_workload.py' &
vagrant ssh vm2 -c 'python3 ./source/memory_workload.py' &

wait
