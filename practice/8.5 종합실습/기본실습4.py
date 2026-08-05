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