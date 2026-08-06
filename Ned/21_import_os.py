# data폴더 안 sample.txt를 다루는 방법
import os
sample = os.path.join("data", "sample.txt")

# 실습 1. open으로 파일 읽기
# 1) open으로 파일을 읽기모드 r, utf-8로 열기
with open(sample, "r", encoding="utf-8") as t:
  line = t.read()
  print(line)
# 읽기 모드
# Good bye world
# 안녕히가세요