# 실습2. with open으로 파일에 쓰기
# 1) with open으로 파일을 쓰기 모드 w, utf-8로 열기
with open("hello.txt", "w", encoding="utf-8") as f:
  # 2) write로 내용을 쓰기
  f.write("안녕하세요\n")
  f.write("반갑습니다\t아님말고\n")
  # 3) with 블록이 끝나면 파일이 자동으로 닫힘

# 닫힘
# 4) r 모드로 다시 열어 쓴 내용을 확인
with open("hello.txt", "r", encoding="utf-8") as f:
  read_f = f.read()
  print(read_f)
# 안녕하세요
# 반갑습니다      아님말고