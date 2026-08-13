# 실습5. info로 데이터 건강검진
import pandas as pd
import os

path_csv = os.path.join("data", "12_metro_compressor.csv")

# 12_metro_digital.csv 파일을 열어 DF 생성
df = pd.read_csv(path_csv, encoding="utf-8")

# DF의 info() 호출 출력
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   측정시각    200 non-null    str    
#  1   압축압력    200 non-null    float64
#  2   배출압력    200 non-null    float64
#  3   저장압력    200 non-null    float64
#  4   오일온도    199 non-null    float64
#  5   모터전류    200 non-null    float64
#  6   가동상태    200 non-null    str    
# dtypes: float64(5), str(2)
# memory usage: 11.1 KB
# None