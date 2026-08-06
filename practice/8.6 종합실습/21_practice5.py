# 실습 5. csv.wirter로 CSV쓰기
# 1) csv를 import
import csv
import os

path = os.path.join("data", "practice5.csv")

# 2) with open으로 w·utf-8·newline(?) 옵션으로 열기
with open(path, "w", encoding="utf-8", newline="") as f:
  # 3) csv.writer로 writer 객체를 만들기
  writer = csv.writer(f)
  # 4) writerow로 헤더와 각 데이터 행을 쓰기
  writer.writerow(["실습6자료", "str"])
  writer.writerow(["첫 번째 행", "89"])
  writer.writerow(["두 번째 행", "91"])
  writer.writerow(["세 번째 행", "88"])
  writer.writerow(["네 번째 행", "92"])
  