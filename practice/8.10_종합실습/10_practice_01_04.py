import numpy as np

# 왠만하면 2차원 배열을 만들어주세요
gugudan = np.array([
  [3,6,9,12,15],
  [4,8,12,16,20],
  [5,10,15,20,25],
])

print(gugudan)

# ndim으로 차원
print(gugudan.ndim) # 2

# shape으로 형태
print(gugudan.shape) # (3, 5)

# size로 전체 개수
print(gugudan.size) # 15