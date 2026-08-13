# 실습 6. 배열 모양 바꾸기

import numpy as np

# 목표
# 한 줄 배열을 값 개수에 맞는 표 모양으로 변환

# 단계
# · 연속 정수 배열을 arange로 생성
numbers = np.arange(6)
print(numbers) # [0 1 2 3 4 5]

# · 값 개수에 맞는 행·열을 정해 reshape로 형태 변환
converted_numbers = numbers.reshape(2,3)

# · 바뀐 배열 출력
print(converted_numbers)
# [[0 1 2]
#  [3 4 5]]