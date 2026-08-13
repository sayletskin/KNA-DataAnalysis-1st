# 시작:끝으로 구간 잘라내기

import numpy as np

temp = np.array([70, 72, 71, 95, 73])
print(temp) # [70 72 71 95 73]

# 두 번째 부터 네 번째 까지 [1:4]
print(temp[1:4]) # [72 71 95]

# 간격을 지정해 뽑아내기
print(temp[::2]) # [70 71 73]