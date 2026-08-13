# 실습5. 경로·옵션오류고치기

import pandas as pd

try:
  df = pd.read_csv("아무거나.csv") # FileNotFoundError
  print(df.shape)
except FileNotFoundError :
  print("FileNotFoundError 발생")