# 실습 8. 압축기와 디지털 신호 구조 비교
# data/12_metro_compressor.csv 
# data/12_metro_digital.csv
# shape, info, describe

import pandas as pd
import os

path_compres = os.path.join("data", "12_metro_compressor.csv") 
path_digital = os.path.join("data", "12_metro_digital.csv")

df_compres = pd.read_csv(path_compres)
print(df_compres.shape) # (200, 7)
df_compres.info()
print(df_compres.describe())
# ata columns (total 7 columns):
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
#              압축압력        배출압력        저장압력        오일온도        모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000


df_digital = pd.read_csv(path_digital)
print(df_digital.shape) # (120, 4)
df_digital.info()
print(df_compres.describe())
# <class 'pandas.DataFrame'>
# RangeIndex: 120 entries, 0 to 119
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    120 non-null    str  
#  1   압축기     120 non-null    int64
#  2   타워      120 non-null    int64
#  3   저압스위치   120 non-null    int64
# dtypes: int64(3), str(1)
# memory usage: 3.9 KB
#              압축압력        배출압력        저장압력        오일온도  모터전류
# count  200.000000  200.000000  200.000000  199.000000  200.000000
# mean     9.172200   -0.016950    9.171400   63.181910    2.060850
# std      0.583699    0.047173    0.582497    6.249822    2.196505
# min      8.130000   -0.030000    8.130000   50.100000    0.030000
# 25%      8.700000   -0.020000    8.697500   58.100000    0.040000
# 50%      9.175000   -0.020000    9.175000   62.900000    0.040000
# 75%      9.665000   -0.020000    9.655000   68.100000    3.812500
# max     10.220000    0.600000   10.220000   75.000000    6.190000