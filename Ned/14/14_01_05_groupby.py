# groupb 코드

import pandas as pd

df = pd.read_csv('data/14_hydraulic.csv', encoding='utf-8')
df.info()

# '냉각기상태' 컬럼의 내용별로 그룹핑을 하자 -> 분할
print(df.groupby('냉각기상태')) 
# <pandas.api.typing.DataFrameGroupBy object at 0x000002155875D550>

# 분할된 DF마다 '온도'컬럼이 있으니까, '온도'의 평균을 구해보자.
print(df.groupby('냉각기상태')['온도'])
# <pandas.api.typing.SeriesGroupBy object at 0x0000014D29927ED0>

# 냉각기상태에 따른 그룹별 온도 평균
print(df.groupby('냉각기상태')['온도'].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89
# Name: 온도, dtype: float64

# 냉각기상태에 따른 그룹별 진동 평균
print(df.groupby('냉각기상태')['진동'].mean().round(2))
# 냉각기상태
# 고장    0.69
# 저하    0.61
# 정상    0.55
# Name: 진동, dtype: float64


# 냉각기상태에 따른 그룹별 온도 평균과 진동 평균
print(df.groupby('냉각기상태')[['온도', '진동']].mean().round(2))
#           온도    진동
# 냉각기상태             
# 고장     54.67  0.69
# 저하     45.46  0.61
# 정상     35.89  0.55

print(df.groupby(['냉각기상태', '운전부하'])['온도'].mean().round(2))
# 냉각기상태  운전부하
# 고장     고부하     55.51
#        저부하     54.05
# 저하     고부하     44.07
#        저부하     45.58
# 정상     고부하     35.89

print(df.groupby(['냉각기상태', '운전부하'])[['온도', '진동']].mean().round(2))
#                온도    진동
# 냉각기상태 운전부하             
# 고장    고부하   55.51  0.73
#       저부하   54.05  0.66
# 저하    고부하   44.07  0.62
#       저부하   45.58  0.61
# 정상    고부하   35.89  0.55
