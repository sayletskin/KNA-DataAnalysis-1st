# 실습 4. csv.reader로 csv읽기
# 1) csv 모듈을 import
import csv
import os
csv_path = os.path.join("data", "08_press.csv")

# 2) with open으로 csv를 읽기 모드 utf-8로 열기
with open(csv_path, "r", encoding="utf-8") as f:

  # 3) csv.reader로 reader 객체를 만들기
  csv_reader = csv.reader(f)

  # 4) for로 각 행(리스트)을 하나씩 꺼내 출력
  for csv_list in csv_reader:
    print(csv_list)