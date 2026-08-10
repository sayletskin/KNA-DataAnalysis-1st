# 실습1번 참고 코드

# 미국식 속도 (miles)를 우리가 쓰는 속도(km)로 변환시켜주는
# Numpy 배열 예제 코드

import numpy as np
miles = np.array([94.7, 104.5, 105.5])

# 속도(km/h)=threh(mph)*1.60934
print(miles * 1.60934)
# [152.404498 168.17603  169.78537 ]
