# 실습1. CSV 불러오기 워밍업

import pandas as pd
import os

path = os.path.join("data","12_metro_small.csv")

try:
  df = pd.read_csv(path, encoding='utf-8')
  print(df.shape) # (30, 7)
  print(df.size) # 210  
  print(df.head(2)) # 기본값5, 숫자만큼 행 추출
except:
  print(f"파일이 없습니다.{path}")

