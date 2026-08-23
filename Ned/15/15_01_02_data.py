import pandas as pd

# -999와 999라는 값이 있다면 NaN으로 처리하기 -> na_values=[-999, 999]
df = pd.read_csv('data/15_01_사출성형_공정.csv', encoding='utf-8', na_values=[-999, 999])
print(df.shape) # (250, 22)
df.info()
print(df.describe())

print(df.isna().sum())
print(df.notna().sum())

# 각 컬럼별 NaN 갯수를 낸 Serise 대상으로 다시 합산을 시키면? -> 전체 NaN 갯수
print(df.isna().sum().sum()) # 475
