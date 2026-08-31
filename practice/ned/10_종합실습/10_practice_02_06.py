# 실습6. 센서별 기초 통계 구하기

import numpy as np

# 여러 설비의 회전수·토크 이차원 배열 준비
rpm_torque = np.array([
  [1552, 42.7],
  [1407, 65.7],
  [1496, 41.9],
  [1443, 46.4]
])

# axis를 열 방향으로 지정해 센서별 평균 계산
print(rpm_torque.mean(axis = 0)) # [1474.5     49.175]

# 센서별 표준편차 계산
print(np.round(rpm_torque.std(axis = 0), 2)) # [54.81  9.69]