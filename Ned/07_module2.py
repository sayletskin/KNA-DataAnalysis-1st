# math 표준 라이브러리
import math

print(math.sqrt(9)) # 3.0
print(math.ceil(4.2)) # 5
print(2 ** 3) # 8
# math에서 sqrt, ceil 두개만 사용한다면 이렇게 써도 됨
from math import sqrt, ceil

# 위에서 가져온 math 함수들 사용 예제입니다
print(sqrt(9))
print(ceil(4.2))

print("=" * 20)

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10)) # 1~10사이 정수 무작위
print(random.choice(["정상", "경고", "위험"])) # 셋 중 무작위

print("=" * 20)

# 표준 라이브러리의 datetime 모듈
import datetime

now = datetime.datetime.now()
print(now) # 2026-08-05 11:20:25.253227

print("=" * 20)

# 모듈 도움말 보기 : 참고만 하고 웹에서 구글링하기
# dir(math)
# help(math.sqrt)
