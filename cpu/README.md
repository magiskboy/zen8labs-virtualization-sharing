Execution plan


Step 1: Start VM1
Step 2: On VM1, run: sysbench cpu --time=20 --threads=4 and observe
Step 3: Start remaining VMs and run stress-ng --cpu 4 to pressure CPUs
Step 4: On VM1, run again: sysbench cpu --time=20 --threads=4 and observe

