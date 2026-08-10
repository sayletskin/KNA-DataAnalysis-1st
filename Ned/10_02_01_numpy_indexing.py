# 1차원 인덱싱 - 번호로 값 꺼내기

# 배열의 인덱스 번호는 파이썬 리스트처럼 0부터 시작

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp) # [70 72 71 95 73]

# 첫번째 
print(temp[0]) # 70

# 뒤에서 첫 번째
print(temp[-1]) # 73

