# 2차원 인덱싱

import numpy as np

data = np.array([
  [70, 2.1],
  [72, 2.3]
])

print(data)
# [[70.   2.1]
#  [72.   2.3]]
print(data.dtype) # float64

# 1) 기존 리스트 처럼 특정 위치 집어내기
print(data[0][1]) # 2.1

# 2) 대부분 numpy의 배열은 수학공식 같은 식으로 위치를 지칭한다
# 0행(row) 1열(calumn)
print(data[0, 1]) # 2.1
