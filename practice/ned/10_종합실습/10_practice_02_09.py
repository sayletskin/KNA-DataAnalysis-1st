# 실습9. NumPy 기초 종합 분석

import os
import numpy as np

path = os.path.join("data", "10_mct_tool.csv")

# · np.loadtxt로 회전수와 토크 두 열을 불러오기
data = np.loadtxt(path, delimiter=',', skiprows=1, usecols=(4,5), encoding='utf-8')
# print(data)

# · shape과 dtype으로 구조 확인
print(data.shape) # (40, 2)
print(data.dtype) # float64

# · 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rpm = data[:, 0]
anomaly = rpm[rpm < 2000]
# print(anomaly) # [  58. 1216. 1217. 1241.]
print(anomaly.size) # 4
print(round(anomaly.mean(), 2)) # 933.0
