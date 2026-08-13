# source .venv/Scripts/activate
import numpy as np

# 파이썬의 리스트로부터 Numpy 배열 만들기
temp = np.array([78.5, 69.8, 73.7])

print(temp) # [78.5 69.8 73.7] 항목사이에 콤마 없음

# 배열의 항목들마다 +5씩 더하려면
# 리스트였다면 10_01_01_list.py처럼
# for문으로 돌려서 항목마다 직접 처리해줬어야함
# Numpy라면 간단하게
print(temp + 5) # [83.5 74.8 78.7]

# 소숫점 이하가 없는 숫자 타입들로 가득한 배열
print(np.array([1,2,3])) # [1 2 3]

# 소숫점 이하가 없는 숫자 타입들로 가득한 배열
print(np.array([1.1,2.2,3.3])) # [1.1 2.2 3.3]

# 소숫점 있는거 없는거 믹스
print(np.array([1.1, 1, 2, 2.2]))
# [1.1 1.  2.  2.2]