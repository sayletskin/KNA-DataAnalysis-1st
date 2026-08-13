# 실습2. head·tail 행 개수 조절
# 숫자 인자를 바꿔가며 원하는 만큼 보는 감각 익히기

import pandas as pd
import os

path = os.path.join("data", "12_metro_digital.csv")

df = pd.read_csv(path, encoding="utf-8")

print(df.shape) # (120, 4)

# head(1), head(10), tail(7), head(500) 출력 비교
print(df.head(1)) # index 0 출력
print(df.head(10)) # index 0~9 출력
print(df.tail(7)) # index 113~119 출력
print(df.head(500)) # index 0~4, ..., 115~119 출력

