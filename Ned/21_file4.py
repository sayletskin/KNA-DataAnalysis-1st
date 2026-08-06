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
  reader = csv.reader(f) 
  print(reader) 
# DictReader가 아닌 그냥 reader를 사용하면
# 보통 csv파일의 첫줄인 헤더줄도 읽어버린다
# reader에게 첫줄은 건너뛰라고 말하는 방법이 필요하다
# next(reader)는 한줄 건너뛰고 reader가 반응하게 한다
  header = next(reader)

  for row in reader:
    print(row[0], row[3]) # 각 행(row)마다 list로 출력됨
    # 1번째 4번째 출력하는데 뭔지 모르고 출력됨 그래서

print("=" * 25)

with open(csv_path, "r", encoding="utf-8") as f:
  # DictReader는 첫줄은 컬럼 이름으로 판단하고
  # 각 row를 해당 컬럼이름들을 key로 하는 딕셔너리로 만듦
  reader = csv.DictReader(f)

  for row in reader:
    # 딕셔너리여서 key값을 넣으면 value가 출력
    print(row["설비ID"], row["진동Y"])


