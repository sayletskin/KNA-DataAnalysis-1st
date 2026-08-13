# 실습4. 이상 센서값 필터링하기

import numpy as np

# 회전수와 토크 배열 준비
rpm = np.array([1552, 1407, 1496, 1443, 1822, 1860])
torque = np.array([42.7, 65.7, 41.9, 46.4, 16.8, 15.3])

# 비교 연산으로 회전수가 기준을 넘는 조건 생성 -> 1800 이상
print(rpm[rpm > 1800]) # [1822 1860]


# 다중 조건으로 회전수 과다 또는( OR, | ) 토크 과소 위험 시점 필터링
# rpm[0] 데이터와 torque[0] 데이터는 같은 시기의 상황을 다룸
print((rpm > 1800) | (torque < 20))
# [False False False False  True  True]