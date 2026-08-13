# 실습 4 참고

import numpy as np

# 왠만하면 2차원 배열을 만들어주세요
apt_games = np.array([
  [3,6,9],
  [4,8,10]
])

print(apt_games)

# ndim으로 차원
print(apt_games.ndim) # 2

# shape으로 형태
print(apt_games.shape) # (2, 3)

# size로 전체 개수
print(apt_games.size) # 6