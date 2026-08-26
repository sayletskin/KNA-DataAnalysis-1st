import pandas as pd
import os

path_WD = os.path.join("data", "16_welding.csv")
wf = pd.read_csv(path_WD, encoding="utf-8")
# wf.info()
#  0   용접전압    162 non-null    int64
#  1   용접전류    162 non-null    int64
#  2   통전전압    162 non-null    int64
#  3   통전전류    162 non-null    int64
#  4   가압력     162 non-null    int64
#  5   판정      162 non-null    int64

# 실습10. 다른현장(용접) 이상치·중복종합정제
q1, q3 = wf['용접전류'].quantile(0.25), wf['용접전류'].quantile(0.75)
iqr = q3 - q1
lo, op = q1 - iqr * 1.5, q3 + iqr * 1.5
m = ((wf['용접전류'] < lo) | (wf['용접전류'] > op))

# · 용접 통전전류의 IQR 경계로 이상치 개수·비율 확인
print(m.sum()) # 20
print(round(m.mean() * 100, 1)) # 12.3

# · clip으로 이상치를 보정하고 중복을 제거·정리
wf['용접전류'] = wf['용접전류'].clip(lo, op)
wf = wf.drop_duplicates().reset_index(drop=True)
print(len(wf)) # 158
# 용접전류 이상치 보정 -> 중복 행 제거 및 인덱스 정렬

# · 정제한 데이터를 파일로 저장
# wf.to_csv()

# 예상 결과
# 용접 통전전류 이상치 24건(14.8%), 보정·중복 제거 후 저장