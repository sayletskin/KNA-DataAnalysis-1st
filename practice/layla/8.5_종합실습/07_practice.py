# 실습 1. import 세 방식으로 모듈 가져오기
# 1) import -> 모듈명.기능() 사용
import math
result = math.sqrt(16)
print(result) # 4.0

# 2) from 모듈 import 사용
from math import sqrt
result = sqrt(16)
print(result) # 4.0

# 3) import 모듈 as 별칭 으로 사용
import math as mt
result = mt.sqrt(16)
print(result) # 4.0

# 4) 세 방식 출력 같은지 확인
# 같음



# 실습2. 표준 라이브러리로 센서값 만들기
# 1) random 모듈을 import
# 3) math 모듈을 import
import random
import math

# 2) randint로 무작위 센서값을 만들어 출력
rand_sens = random.randint(1, 10)
print(rand_sens)

# 3) math 모듈로 그 값을 가공(제곱근)
sqrt_sens = round(math.sqrt(rand_sens),5)
print(sqrt_sens) 

# 4) 다시 실행시 값이 달라지는지 확인
# 달라짐



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

print("=" * 20)

# 실습4. os로 파일 존재 확인하기
# 1) os를 import
import os

# 2) path.join 으로 폴더와 파일 이름을 이어 경로를 만들기
path = os.path.join("data", "08_press.csv")

# 3) path.exists로 그 경로가 있는지 참·거짓 확인
is_exists = os.path.exists(path)
print(is_exists) # True

# 4) if로 있으거나 없으면 다른 메세지 출력
if is_exists:
  print("파일 있음!")
else:
  print("파일 없음!")
# 파일 있음!


# 실습5. datatime으로 점검 기록 남기기
# 1) os와 datatime을 import
import os, datetime

# 2) listdir로 폴더 파일 수를 구하기
data_folder_count = len(os.listdir("data"))
print(data_folder_count) # 6

# 3) datetime.now로 현재 시각을 담기
now = datetime.datetime.now()
print(now)

# 4) f-string으로 파일 수와 시각을 한 문장으로 출력
print(f"data폴더 파일 수 : {data_folder_count}개\n"
      f"점검 시각 {now}")


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