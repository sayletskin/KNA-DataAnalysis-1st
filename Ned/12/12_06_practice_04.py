# 실습4. 필요한열만골라불러오기

import pandas as pd
import os

path = os.path.join("data", "12_metro_compressor.csv")

df = pd.read_csv(path, usecols=['측정시각', '오일온도', '모터전류', '압축압력'])
print(df.shape) # (200, 4)
print(df.head(3))
# usecols 순서 상관x