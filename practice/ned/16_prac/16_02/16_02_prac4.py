# 실습4. 이상치제거후크기비교
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

q1 = df['사이클타임'].quantile(0.25)
q3 = df['사이클타임'].quantile(0.75)
iqr = q3 - q1
lower = round(q1 - 1.5 * iqr, 2)
upper = round(q3 + 1.5 * iqr, 2)
mask = (df['사이클타임'] < lower) | (df['사이클타임'] > upper)

# · 조건을 뒤집어 정상 범위 행만 남기기
df_clean = df[~mask]

# · 원본과 제거 후의 행 수를 비교
print(len(df), len(df_clean)) # 202, 196

# · 제거 후 평균을 구해 변화 확인
print(df['사이클타임'].mean(), round(df_clean['사이클타임'].mean(), 2))
# 64.75 27.28