# 실습5. 조건별 개수와 비율 세기

import numpy as np

# 토크 배열 준비
torque = np.array([42.7, 65.7, 41.9, 46.4, 16.8, 15.3])

# 비교 조건으로 참·거짓 불리언 배열 생성
high = torque > 45
print(high) # [False  True False  True False False]
# print(torque[torque > 45]) # [65.7 46.4]

# 불리언 배열의 합(sum)으로 개수, 평균(mean)으로 비율 계산
print(high.sum()) # 2 
print(round(high.mean(), 2)) # 0.33