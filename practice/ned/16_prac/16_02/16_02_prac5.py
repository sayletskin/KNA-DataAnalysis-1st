# 실습 5. 경계값 보정 clipping
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")

q1 = df['사이클타임'].quantile(0.25)
q3 = df['사이클타임'].quantile(0.75)
iqr = q3 - q1
lower = round(q1 - 1.5 * iqr, 2)
upper = round(q3 + 1.5 * iqr, 2)

# · clip으로 하한보다 작은 값은 하한으로 올리기
# · 상한보다 큰 값은 상한으로 내리기
df_cliped = df['사이클타임'].clip(lower=lower, upper=upper)

# · 보정 후 최솟값·최댓값·평균 확인
print(round(df_cliped.min(), 2), round(df_cliped.max(), 2))   # 20.6 58.61
print(round(df_cliped.mean(), 2)) # 28.28
