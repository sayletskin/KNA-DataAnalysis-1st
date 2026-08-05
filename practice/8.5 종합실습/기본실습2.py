# 실습2. 표준 라이브러리로 센서값 만들기
# 1) random 모듈을 import
# 3) math 모듈을 import
import random
import math

# 2) randint로 무작위 센서값을 만들어 출력
rand_sens = random.randint(1, 10)
print(rand_sens)

# 3) math 모듈로 그 값을 가공(제곱근)
sqrt_sens = round(math.sqrt(rand_sens),5)
print(sqrt_sens) 

# 4) 다시 실행시 값이 달라지는지 확인
# 달라짐