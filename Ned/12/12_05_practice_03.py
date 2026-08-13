# 실습3. 한글·구분자깨짐옵션다루기

import pandas as pd
import os

path = os.path.join("data", "12_metro_compressor_semicolon.csv")

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열 , sep=";"이면 200행 7열

df = pd.read_csv(path, sep=';')
print(df.shape) # (200, 7)
print(df.head(4))