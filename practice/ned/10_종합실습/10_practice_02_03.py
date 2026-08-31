# 실습3. 센서값 정규화하기

import numpy as np

# 회전수 측정 배열 준비
rpm = np.array([1552, 1407, 1496, 1443, 1422, 1860])

# 최솟값과 최댓값을 min, max로 확인
print(rpm.min())
print(rpm.max())

# 정규화 공식을 브로드캐스팅으로 적용해 변환
# 정규화 공식
# 정규화된X = (비교대상 - 최소값) / (최대값 - 최소값)
rpm_min = rpm.min()
rpm_max = rpm.max()
normalized = (rpm - rpm_min) / (rpm_max - rpm_min)
print(normalized) 
# [0.3200883  0.         0.19646799 0.0794702  0.03311258 1.        ]
print(np.round(normalized, 2))
# [0.32 0.   0.2  0.08 0.03 1.  ]