# 실습 1. 데이터 불러오기와 구조 확인하기

import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')

# shape 확인
print(df.shape) # (30, 7)

# columns의 열 이름 출력 확인
print(df.columns)
# Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')

# 실제 CSV파일 열어보고 shape, columns 그대로 나온건지 비교

# -----------------------------------------------------------------------------
# 실습 2. 열 선택하기

# data/13_diecasting_small.csv 파일 열기
import pandas as pd

df = pd.read_csv('data/13_diecasting_small.csv')

# · 대괄호 한 겹으로 단일 열을 Series로 선택
# : '형체력' 컬럼 하나만 빼오기
df_series = df["형체력"]

# · 대괄호 두 겹으로 복수 열을 DataFrame으로 선택
# : '형체력', '실린더압력' 두개를 선택하기
df_dataframe = df[['형체력', '실린더압력']]

# · 선택한 열에 mean으로 평균 계산
# df['형체력'].mean() -> round로 소숙점 이하 1자리까지만 나오게 조정해주세요
print(round(df_series.mean(),1)) # 267.8

# -----------------------------------------------------------------------------
# 실습 3. 공정 센서 열 골라내기

# · 주조 로그 파일 불러오기
# data/13_diecasting_shot.csv 파일 열기
import pandas as pd

df = pd.read_csv('data/13_diecasting_shot.csv')

# · 한 센서 열을 Series로 선택
# '형체력' 선택
df_series = df['형체력']

# · 여러 feature 열을 DataFrame으로 선택해 형태 확인
# df[['형체력', '실린더압력', '주조압력']].shape 출력
df_dataframe = df[['형체력', '실린더압력', '주조압력']]
print(df_dataframe.shape) # (200, 3)