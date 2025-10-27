<div align="center">
    <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Black+Han+Sans&size=40&duration=2500&pause=1000&center=true&vCenter=true&width=435&lines=Problem+solving" alt="Typing SVG" /></a>
</div>

<br>

# ⏱ 시간 복잡도 계산 방법

알고리즘 문제를 풀 때는 주어진 시간 제한 안에 프로그램이 동작할 수 있는지를 판단해야 합니다.  
이를 위해 입력 크기(N)와 시간 제한(T)을 기준으로 얼마나 큰 시간 복잡도까지 가능한지 계산합니다.

## 1️⃣ 초당 처리 가능한 연산량

보통 온라인 저지 기준으로는 다음과 같이 가정합니다:

| 언어 | 1초당 가능한 연산 횟수 |
|------|------------------|
| C / C++ / Java | 약 `10^8` 번 |
| Python | 약 `10^7` 번 |

즉, 시간 제한이 T초라면 대략

```r
허용 연산량 R = (초당 연산량) × T
```

으로 계산할 수 있습니다.

## 2️⃣ 입력 크기에 따른 적정 시간 복잡도

아래 표는 약 1~2초 제한 기준에서 대략적으로 가능한 복잡도를 정리한 것입니다.

| 입력 크기 (N) | 가능한 시간 복잡도 | 예시 알고리즘 |
|----------------|----------------|----------------|
| `N ≤ 10^7` | `O(N)` | 단순 순회, 누적합, 해시 |
| `N ≤ 10^5` | `O(N log N)` | 정렬, 우선순위 큐, 이분 탐색 |
| `N ≤ 2×10^3` | `O(N²)` | 중첩 루프, 2차원 DP |
| `N ≤ 100` | `O(N³)` | 플로이드–워셜, 3중 루프 |
| `N ≤ 20` | `O(2^N)` | 완전 탐색, 백트래킹 |
| `N ≤ 10` | `O(N!)` | 순열 탐색 |

⚠️ Python은 느리기 때문에 여유 있게 잡는 게 좋습니다.  
예: N=10⁵라면 O(N log N)은 가능하지만 O(N²)은 불가능합니다.

## 3️⃣ 예시 계산

```mathematica
예: N = 100,000, 시간 제한 = 2초, 언어 = C++

→ 초당 연산량 = 10^8
→ 허용 연산량 R = 2 × 10^8
→ N log N = 100,000 × 17 ≈ 1.7×10^6 < R → ✅ 가능
→ N² = 10^10 > R → ❌ 불가능
```

따라서 이 문제에서는 O(N log N) 이하의 알고리즘을 선택해야 합니다.

## 4️⃣ 정리 요약

```markdown
1. 언어별 초당 연산량 기준을 정한다.
2. 시간 제한 T초를 곱해 허용 연산량 R을 계산한다.
3. 입력 크기 N에 대해 f(N) ≤ R 인 시간복잡도를 선택한다.
```

## 5️⃣ 참고 공식 (빠른 계산용)

```python
# 허용 가능한 시간복잡도 계산기 (Python)
import math

def check_time_complexity(n, t=1, ops_per_sec=1e8):
    R = t * ops_per_sec
    print(f"N={n}, 제한={t}s, 연산가능≈{R:.1e}")
    print(f"O(N): {n <= R}")
    print(f"O(N log N): {n*math.log2(n) <= R}")
    print(f"O(N^2): {n**2 <= R}")
    print(f"O(2^N): {2**n <= R if n < 30 else 'too large'}")

check_time_complexity(100000, t=2)
```