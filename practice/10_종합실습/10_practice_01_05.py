# 실습 5. 자료형 확인과 변환하기

import numpy as np

data = np.array([123.54234, 6456.5467, 7897.678])

# dtype 현재 자료형 확인
print(data.dtype)

# astype으로 정수형으로 변환한 새 배열 출력
converted_data = data.astype(int)
print(converted_data) # [ 123 6456 7897]