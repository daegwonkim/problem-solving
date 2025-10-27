# 정렬(Sorting) 패턴

## 1️⃣ 개념 요약
정렬은 데이터를 **일정한 기준으로 재배치**해서 문제의 복잡도를 낮추는 대표적인 전처리 기법이다.  
정렬을 통해 '순서'가 생기면 **탐색, 비교, 최적화 문제**가 단순해진다.  

즉, 정렬은 “답을 구하는 과정”이 아니라 “문제를 단순한 형태로 바꾸는 전처리 과정”이다.  
정렬하고 나면 항상 새로운 접근법이 보일 것이다.

---

## 2️⃣ 대표 알고리즘 요약

| 알고리즘 | 시간복잡도 | 특징 | 사용 예시 |
|-----------|--------------|------|------------|
| 선택 정렬 | O(N²) | 단순하지만 느림 | 개념 연습용 |
| 퀵 정렬 | O(N log N) | 평균적으로 빠름, 분할정복 기반 | 일반적인 대용량 데이터 |
| 병합 정렬 | O(N log N) | 안정적, 추가 메모리 필요 | 안정 정렬 필요한 경우 |
| 카운팅 정렬 | O(N + K) | 정수 범위 작을 때 매우 빠름 | 점수 정렬, 나이순 정렬 |
| 내장 정렬 | 언어마다 다름 | 최적화된 하이브리드 방식 | 실무/코테 대부분 사용 가능 |

---

## 3️⃣ 언제 정렬을 써야 하는가?

| 상황 | 정렬이 필요한 이유 |
|------|--------------------|
| 두 배열의 원소를 비교해야 할 때 | 정렬 후 투 포인터로 O(N) 가능 |
| “가장 큰 값”, “가장 작은 값” 구할 때 | 정렬 후 인덱스로 바로 접근 |
| 범위 합, 누적값 계산 시 | 정렬로 순서 보장 |
| 특정 기준(예: 점수, 나이 등)으로 우선순위 정할 때 | 커스텀 키 정렬로 해결 |

---

## 4️⃣ 자주 쓰이는 코드 패턴

### ① 기본 정렬
```python
arr = sorted(arr)  # 오름차순
arr = sorted(arr, reverse=True)  # 내림차순
```

### ② 튜플 기준 정렬
```python
people = [(25, "Tom"), (20, "Jane"), (25, "Alex")]
people.sort(key=lambda x: (x[0], x[1]))  # 나이 → 이름 순
```

### ③ 객체(클래스) 정렬
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    score: int

students = [Student("A", 90), Student("B", 80)]
students.sort(key=lambda s: s.score, reverse=True)
```

### ④ 정렬 + 탐색 조합 (Binary Search)
정렬 후 이진 탐색으로 값 존재 여부 판단.
```python
arr = sorted(arr)
# bisect 모듈 활용
import bisect
exists = bisect.bisect_left(arr, target) < len(arr) and arr[bisect.bisect_left(arr, target)] == target
```

### ⑤ 정렬 + 투 포인터 조합
“두 수의 합”처럼 정렬된 상태에서 양 끝 포인터를 이동.
```python
arr.sort()
l, r = 0, len(arr) - 1
while l < r:
    s = arr[l] + arr[r]
    if s == target:
        print(l, r)
        break
    elif s < target:
        l += 1
    else:
        r -= 1
```