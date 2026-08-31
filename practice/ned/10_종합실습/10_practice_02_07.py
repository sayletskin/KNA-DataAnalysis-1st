# 실습7. 파일 데이터로 기초 통계 구하기

import numpy as np
import os

path = os.path.join("data", "10_mct_tool.csv")

# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm = np.loadtxt(path, delimiter=',', skiprows=1, usecols=4, encoding='utf-8')

# 불러온 배열의 평균과 표준편차 계산
print(round(rpm.mean(),1)) # 4212.6
print(round(rpm.std(),1)) # 1144.9

# 최솟값과 최댓값으로 값의 범위 확인
print(f"최댓값: {rpm.max()}, 최솟값: {rpm.min()}") # 최댓값: 4987.0, 최솟값: 58.0
print(f"값의 범위: {rpm.max() - rpm.min()}") # 값의 범위: 4929.0
