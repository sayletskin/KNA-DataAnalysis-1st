
import pandas as pd

df = pd.read_csv("data/02-01_측정의_3요소_측정샘플.csv")

# print(df.columns.tolist())
# ['timestamp', 'MTR01_VIB_RMS_H', 'MTR01_CURRENT', 
# 'MTR01_TEMP', 'HYD01_PRESS_IN', 'FUR01_TEMP_Z1']

# 1. 시간 주기
df["timestamp"] = pd.to_datetime(df["timestamp"])
gaps = df["timestamp"].diff().value_counts()
print(gaps)

# 2. 각 column의 계산(최대값, 최소값, 평균, 표준편차 등)
cols = [
  'MTR01_VIB_RMS_H', 
  'MTR01_CURRENT', 
  'MTR01_TEMP', 
  'HYD01_PRESS_IN', 
  'FUR01_TEMP_Z1'
  ]

print(df[cols].agg(["min", "max", "mean", "std"]))

# 3. 각 column의 최소 차이값
changes = df[cols].diff().abs()
change_min = changes[changes>0].min()
print(change_min)
# MTR01_VIB_RMS_H    0.1
# MTR01_CURRENT      0.5
# MTR01_TEMP         0.5
# HYD01_PRESS_IN     1.0
# FUR01_TEMP_Z1      0.5