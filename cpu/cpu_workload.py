import sys
import multiprocessing as mp
import time
import numpy as np


def matmul_pure(N):
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
    return A @ B

    # C = [[0.0]*N for _ in range(N)]

    # for i in range(N):
    #     for j in range(N):
    #         s = 0.0
    #         for k in range(N):
    #             s += A[i][k] * B[k][j]
    #         C[i][j] = s

    # return C[0][0]


if __name__ == "__main__":
    cpus = int(sys.argv[1])
    N = int(sys.argv[2])
    n_task = int(sys.argv[3])

    print(f'CPUs: {cpus} | N: {N} | n_task: {n_task}')

    with mp.Pool(processes=cpus) as pool:
        start = time.time()
        pool.map(matmul_pure, [N]*n_task)
        print(f"In {time.time()-start} seconds")
