# 실습1. IQR과 이상치 경계 구하기
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")
# · 사이클타임의 25%·75% 값을 구해 IQR(Q3-Q1) 계산
q1 = df['사이클타임'].quantile(0.25)
q3 = df['사이클타임'].quantile(0.75)
iqr = q3 - q1
print(q1, q3, iqr) # 20.8 35.925 15.124999999999996

# · Q1에서 IQR의 1.5배를 빼 하한 계산
lower = round(q1 - 1.5 * iqr, 2)
print(lower) # -1.89

# · Q3에 IQR의 1.5배를 더해 상한 계산
upper = round(q3 - 1.5 * iqr, 2)
print(upper) # 13.24