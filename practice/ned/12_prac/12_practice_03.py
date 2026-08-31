# 실습3. 구조 파악 3종 도구

import pandas as pd
import os

path = os.path.join("data", "12_metro_digital.csv")

df = pd.read_csv(path, encoding="utf-8")

# .shape출력
print(df.shape) # (120, 4)

# .columns 출력 df.columns.tolist()출력
print(df.columns)
# Index(['측정시각', '압축기', '타워', '저압스위치'], dtype='str')
print(df.columns.tolist()) # ['측정시각', '압축기', '타워', '저압스위치']

# .dtype 출력
print(df.dtypes)
# 측정시각       str
# 압축기      int64
# 타워       int64
# 저압스위치    int64
# dtype: object