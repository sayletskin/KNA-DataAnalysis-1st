# [실습 1] finally로 파일 안전하게 닫기
import os

path = os.path.join("data", "sample.txt")

# 1) try블록에서 파일을 열어 처리
try:
  sample = open(path, "r", encoding="utf-8")
  print(sample.readlines())
# 2) 처리 도중 오류가 날 수 있음을 가정
except:
  print("오류 발생")
# 3) finally블록에 close를 넣어 오류 여부와 상관없이 닫기
finally:
  sample.close()
  print("파일 종료")
# 4) 일부로 오류를 내도 finally가 실행되는지 확인
# print(sample.read())에 오타를 내서 오류 발생시 finally 작동