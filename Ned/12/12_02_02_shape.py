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

# ===================================

# 실습4. 열 이름·자료형 점검
# import pandas as pd
# import os

path_csv = os.path.join("data", "12_metro_compressor.csv")
# 12_metro_compressor.csv 읽어 DF 담기
df = pd.read_csv(path_csv, encoding="utf-8")

# .columns 출력 df.columns.tolist()출력
print(df.columns)
# Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'], dtype='str')
print(df.columns.tolist())
# ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']

# DF의 dtypes 출력
print(df.dtypes)
# 측정시각        str
# 압축압력    float64
# 배출압력    float64
# 저장압력    float64
# 오일온도    float64
# 모터전류    float64
# 가동상태        str
# dtype: object

