# 실습3. 측정시간축배열만들기

import numpy as np

# 단계
# · 시작값·끝값·간격을 정해 np.arange로 시점 배열 생성
# · 간격을 바꿔가며 시점 개수 변화 관찰
# · 시간축 배열 출력

two_min = np.arange(0, 60 * 2, 15)

print(two_min) 
# [  0  15  30  45  60  75  90 105]
