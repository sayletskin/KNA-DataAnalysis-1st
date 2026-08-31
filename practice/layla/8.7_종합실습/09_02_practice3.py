# [실습3] 여러 파일 묶어 처리하기
# 다음과 같은 식의 리스트를 만들어 반복문으로 처리하자
# for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됩니다

# file_names = ["블라.csv", "블라블.csv", "블라블라.csv"]
import os

# 1) 여러 파일 이름을 반복
file_names = ["08_press.csv", "sample.txt", "영크크.csv",
               "09_ict_inspection.csv", "영크크.txt"]

seccess_file = 0

# 2) try에서 파일을 열어 처리
for file_name in file_names:
  try:
    file_path = os.path.join("data", file_name)
    file = open(file_path, "r", encoding="utf-8")
    seccess_file += 1
    print(file.readlines())
  except FileNotFoundError:
    continue

print(f"{seccess_file}개 처리 완료")