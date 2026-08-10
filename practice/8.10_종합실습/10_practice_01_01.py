# 실습1. 센서값 배열 만들기
import numpy as np

# 단계
# · 섭씨 측정값 리스트를 np.array로 배열 생성
temps_C = np.array([25, 29, 34, 39])

# · 배열에 곱셈과 덧셈을 묶음 연산으로 적용해 화씨로 변환
temps_F = temps_C * 1.8 + 32

# · 변환된 배열 출력
print(temps_F) # [ 77.   84.2  93.2 102.2]