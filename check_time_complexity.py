import math

def check_time_complexity(n, t=1, ops_per_sec=1e8):
    R = t * ops_per_sec
    print(f"N={n}, 제한={t}s, 연산가능≈{R:.1e}")
    print(f"O(N): {n <= R}")
    print(f"O(N log N): {n*math.log2(n) <= R}")
    print(f"O(N^2): {n**2 <= R}")
    print(f"O(2^N): {2**n <= R if n < 30 else False}")

check_time_complexity(100000, t=2)