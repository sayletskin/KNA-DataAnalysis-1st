import pandas as pd
import os

# 12_metro_compressor.csv
path = os.path.join("data", "12_metro_compressor.csv")

df = pd.read_csv(path,encoding='utf-8')

# 200행7열—인덱스3번행오일온도가NaN
# NaN -> 숫자 아님 (대표적 사례: 0으로 나눔)
print(df.head(4))
print(df.shape) # (200, 7)

