# 수학 관련 모듈을 불러옵니다
import math

# 해당 모듈이름.함수() 식으로 호출
print(0)
print(math.sqrt(25)) # 5.0, 25의 제곱근

# 수학 관련된 모듈에서 sqrt 기능만 불러옵니다
from math import sqrt
print(sqrt(25)) # math를 호출할 필요 없음

# math 라는 모듈 이름 다 쓰기 귀찮아서 줄이기
# as : 가져온 모듈의 별칭(축약) - 권장
import math as mt

# 별칭으로 가져온 모듈 이름을 언급해봅시다
result = mt.sqrt(25)
print(result) # 5.0 , 가능

# datetime 모듈을 가져옵니다 (축약해서)
import datetime as dt

# datetime의 .now()는 현재 지역 날짜와 시간을 반환
now = dt.datetime.now()
print(now) # 2026-08-05 11:20:25.253227