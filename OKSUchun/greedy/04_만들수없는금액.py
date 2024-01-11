from itertools import combinations as c
import psutil
import time
import os

pid = os.getpid()


def solution():
    n = int(input())
    coin = list(map(int, input().split()))
    sum_list = []
    for i in range(1, n + 1):
        # nCr = list(c(coin, i))
        sum_list.extend(list(map(sum, list(c(coin, i)))))

    sum_list = sorted(list(set(sum_list)))

    for i in range(1, sum_list[-1] + 2):
        if i in sum_list:
            pass
        else:
            result = i
    print(result)


start_time = time.time()  # 측정 시작
process = psutil.Process(pid)
initial_memory = process.memory_info().rss
solution()
final_memory = process.memory_info().rss
memory_usage = final_memory - initial_memory

# Convert to megabytes (MB)
memory_usage_mb = memory_usage / (1024 * 1024)

print(f"Memory Usage of the Function: {memory_usage_mb} MB")
end_time = time.time()
print(f"time: {end_time-start_time} 초입니다.")
