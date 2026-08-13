# ==================================================

import pandas as pd
import os

path = os.path.join("data", "12_metro_compressor.csv")

df = pd.read_csv(path, usecols=['측정시각', '오일온도'])
# df을 생성하면 가장 먼저 shape
print(df.shape) # (200, 2)
# 사실 usecols 하기 전에 해야하는 거 head
print(df.head(3))
# head에서 나온 첫 행을 usecols에 골라 넣기

# ==================================================

# import pandas as pd
# 1. 데이터 읽기 및 크기, 열 목록 확인
df = pd.read_csv("data/12_metro_compressor.csv")
print("데이터 크기 (shape):", df.shape) # (200, 7)
# 2. 상위 3개 행 미리보기
print(df.head(3))
# 3. 종합 검진 (info) 실행
df.info()
# 4. 수치형 열 통계 요약
print(df.describe())

# =================================================

