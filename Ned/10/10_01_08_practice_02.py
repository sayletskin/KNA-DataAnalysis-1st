# 실습2. 균등간격배열만들기
import numpy as np

# 30까지 6간격으로 배열 채워 만들기
# 0부터 6 증가시키면서 30보다 작은 값일 때 배열에 붙여나감
gab_six = np.arange(0, 30, 6)
print(gab_six) # [ 0  6 12 18 24]

# 0부터 30까지 6등분 나눠 배열 내용 채우기
idv_six = np.linspace(0, 30, 6)
print(idv_six) # [ 0.  6. 12. 18. 24. 30.]
