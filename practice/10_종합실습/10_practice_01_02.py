# 실습2. 균등간격배열만들기

import numpy as np

# 단계
# · 시작값·끝값·개수를 정해 np.linspace로 구간을 균등 분할
idv_eleven = np.linspace(0, 100, 11)

# · 만들어진 배열과 각 값의 간격 확인
# · 결과 배열 출력
print(idv_eleven)
# [  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]