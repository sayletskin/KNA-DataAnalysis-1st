# 실습 6. 특정 구간 추출 종합
# 열 선택·loc·iloc를 결합해 특정 구간을 추출하는 종합
import pandas as pd

df_shot = pd.read_csv('data/13_diecasting_shot.csv')

# · 여러 feature 열을 선택한 뒤 iloc로 앞 구간 추출
cols =['실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력']
print(df_shot[cols].iloc[0:10].shape) # (10, 5) , (0~9, cols갯수)

# · loc 라벨 범위로 두 열 구간 추출
cols2 = ['실린더압력','주조압력']
print(df_shot[cols2].loc[0:5].shape) # (11, 2) , (0~5, cols2갯수)

# · iloc 위치 범위로 앞쪽 열 구간 추출
# .iloc(50:60, 0:6)
print(df_shot.iloc[50:60, 0:6]) # (50~59행, 0~5열)