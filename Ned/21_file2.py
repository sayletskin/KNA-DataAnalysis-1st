import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 코드 강제 종료시키기
if not os.path.exists(csv_path):
  print(f"{csv_path}에 파일 없습니다.")
  sys.exit(1) # 코드 강제 종료
# 비정상 종료시 보통 0이 아닌 값 전달

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
  # print(f.readlines()) # 이제 csv 전문가에게 맡깁시다
  reader = csv.reader(f) # <- 리더 전문가
  print(reader) # <_csv.reader object at 0x000001513B978A00>
  # 누가 암호로 만들어놧어 해독 전문가 불러
  for row in reader: # <- 전문가
    print(row) # 각 행(row)마다 list로 출력됨