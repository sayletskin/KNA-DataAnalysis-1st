# 실습8. drop_duplicates로중복제거
import pandas as pd

df = pd.read_csv("data/16_diecasting.csv", encoding="utf-8")


# · drop_duplicates로 완전 중복 행 제거
df_onlyone = df.drop_duplicates()

# · 제거 후 행 수와 남은 중복 개수 확인
print(len(df), len(df_onlyone)) # 202 200

# · subset으로 특정 컬럼만 기준 삼아 제거
df_onlyone_subset = df.drop_duplicates(subset="실린더압력")
print(len(df_onlyone_subset)) # 16


