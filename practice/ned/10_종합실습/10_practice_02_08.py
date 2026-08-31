# 실습8. 필터링과 통계 결합하기

import numpy as np
import os

path = os.path.join("data", "10_mct_tool.csv")

# · 토크 배열 준비
torque = np.loadtxt(path, delimiter=',', skiprows=1, usecols=5, encoding='utf-8')

# · 불리언 인덱싱으로 기준을 넘는 값만 추출
high = torque[torque > 10]
print(high) # [ 21. 147. 146.  21.]

# · 추출한 값들의 평균과 개수 계산
print(round(high.mean(), 2)) # 83.75
print(high.size) # 4