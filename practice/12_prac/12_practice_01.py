# 실습1. head·tail로 디지털 신호 살펴보기
# head와 tail로 데이터 첫인상과 결측치 확인

import pandas as pd
import os

path = os.path.join("data", "12_metro_digital.csv")

df = pd.read_csv(path, encoding="utf-8")

# df정상작동 확인용 shape
print(df.shape) # (120, 4)

# head와 tail로 NaN 찾기
print(df.head(10))
print(df.tail(10))