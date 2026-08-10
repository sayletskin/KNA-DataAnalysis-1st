import os
import csv

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
   writer = csv.writer(f) # 너는 라이트 전문가니?
   writer.writerow(["시각", "설비"])
   writer.writerow(['09:08', 'PUMP-01'])
# with open("hello.txt", "w", encoding="utf-8") as f:
#   f.write("안녕하세요\n")
#   f.write("반갑습니다\t아님말고\n")
# csv 파일은 csv 전문가에게 변수하나 걸치고 csv 함수를 씀