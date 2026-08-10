# 실습 1. import 세 방식으로 모듈 가져오기
# 1) import -> 모듈명.기능() 사용
import math
result = math.sqrt(16)
print(result) # 4.0

# 2) from 모듈 import 사용
from math import sqrt
result = sqrt(16)
print(result) # 4.0

# 3) import 모듈 as 별칭 으로 사용
import math as mt
result = mt.sqrt(16)
print(result) # 4.0

# 4) 세 방식 출력 같은지 확인
# 같음