import pandas as pd


# 실습1. 주조데이터구조·분포살펴보기

# · read_csv로 데이터를 불러와 head로 앞부분 확인
df = pd.read_csv('data/16_diecasting.csv', encoding="utf-8")
print(df.head(3)) 
#    샷  실린더압력    주조압력  사이클타임  비스킷두께형체력  상태
# 0  1  214.0  1037.0   20.7   10.0  258.0   0
# 1  2  217.0  1052.0   20.7   11.0  257.0   0
# 2  3  214.0  1037.0   20.8   11.0  254.0   0

# · shape와 columns로 크기와 컬럼 이름 확인
print(df.shape, df.columns)
# (202, 7)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '상태'], dtype='str')

# · info로 자료형과 결측 여부 훑기
df.info()
# 0   샷       202 non-null    int64  
#  1   실린더압력   188 non-null    float64
#  2   주조압력    188 non-null    float64
#  3   사이클타임   188 non-null    float64
#  4   비스킷두께   188 non-null    float64
#  5   형체력     188 non-null    float64
#  6   상태      202 non-null    int64  