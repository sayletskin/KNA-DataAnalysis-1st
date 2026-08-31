# 실습6. 처리 전후 통계 비교
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

q1 = df['실린더압력'].quantile(0.25)
q3 = df['실린더압력'].quantile(0.75)
iqr = q3 - q1
lower = round(q1 - 1.5 * iqr, 2)
upper = round(q3 + 1.5 * iqr, 2)
mask = (df['실린더압력'] < lower) | (df['실린더압력'] > upper)

# · 실린더압력 이상치 경계와 조건을 만들기
# · 제거·보정·중앙값 채움 세 방식을 각각 적용
df_filled = df['실린더압력'].mask(mask).fillna(df['실린더압력'].mask(mask).median())

print(round(df['실린더압력'].mean(), 2)) # 234.31
print(round(df[~mask]['실린더압력'].mean(), 2)) # 238.39
print(round(df['실린더압력'].clip(lower = lower, upper = upper).mean(), 2)) # 235.31
print(round(df_filled.mean(), 2)) # 238.05

# · 처리 전 평균과 세 방식의 평균을 나란히 비교
