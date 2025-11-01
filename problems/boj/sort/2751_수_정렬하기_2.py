"""
BOJ 2751 - 수 정렬하기 2

문제 요약
- 입력: 수의 개수 N, N개의 정수
- 출력: 오름차순 정렬된 결과
- 제한: N ≤ 10^6, 시간복잡도 O(N log N) 이하 필요

접근 아이디어
1. 단순 정렬로 O(N log N) 가능
2. 파이썬 내장 정렬 사용
"""

import sys

input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]

numbers.sort()
for i in range(n):
    print(numbers[i])