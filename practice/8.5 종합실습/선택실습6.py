# 실습 6. 폴더에서 csv파일만 골라내기
# 1) os를 import하고 listdir로 폴더 목록 구하기
import os

data_lists = os.listdir("data")

# 2) for-if로 .csv로 끝나는 이름만 빈 리스트에 모으기
csv_file = []

for file_name in data_lists:
  if file_name.endswith("csv"):
    csv_file.append(file_name)

# 3) 모은 csv마다 path.join으로 전체 경로 만들기(?)
csv_paths = []

for cvs_name in csv_file:
    cvs_path = os.path.join("data", cvs_name)
    csv_paths.append(cvs_path)

print(csv_paths)

# 4) 골라낸 csv 목록 출력
print(csv_file)  