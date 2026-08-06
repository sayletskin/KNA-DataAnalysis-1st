# 실습 6. CSV 읽어 조건 저장하기
# 1) csv를 import
import csv
import os

prac5_path = os.path.join("data", "practice5.csv")
prac6_path = os.path.join("data", "practice6.csv")
lists = []

# 2) csv.reader로 읽고 첫 줄 헤더는 건너뛰기
with open(prac5_path, "r", encoding="utf-8") as f:
  csv_reader = csv.reader(f)
  header = next(csv_reader)

# 3) 값을 float로 변환해 기준 90초과 행만 리스트에 모으기
  for row in csv_reader:
    if float(row[1]) > 90:
      lists.append(row)

# 4) csv.writer로 모은 행들을 새 CSV에 저장
with open(prac6_path, "w", encoding="utf-8", newline="") as f:
  csv_writer = csv.writer(f)
  csv_writer.writerow(header)
  csv_writer.writerows(lists)
