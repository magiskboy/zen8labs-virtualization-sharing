import time

size_mb = 512

data = bytearray(b'A' * size_mb * 1024 * 1024)

print("Allocated", size_mb, "MB")

time.sleep(10)
