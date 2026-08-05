# 실습3. os로 폴더 목록 살펴보기
# 1) os 모듈을 import
import os

# 2) getcwd로 현재 작업 폴더를 학인
file_folder = os.getcwd()
print(file_folder)

# 3) listdir로 폴더 안 목록 변수에 담기
file_lists = os.listdir("data")

# 4) for로 목록을 하나씩 출력(하고 csv만 골라 출력)
for file_name in file_lists:
  print(file_name)

for file_name in file_lists:  
  if file_name.endswith("csv"):
    print(f"csv파일: {file_name}")