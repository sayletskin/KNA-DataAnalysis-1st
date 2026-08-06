# 기본 내장함수인 open()으로 sample.txt 파일 열기
# 읽기모드(r)로 utf-8 형식을 변환을 거쳐 읽기로 한다
# 가져온 정보(파인 접근 열쇠(참조값))를 f에 담는다
f = open("sample.txt", "r", encoding="utf-8")

print(type(f).__name__)


f.close() # 열었다면 언젠가는 꼭 닫아줍시다

# 만약 신경써서 파일 닫기(close) 해주기 귀찮다면
# with open ... as 문법을 쓰는 것도 좋다
with open("sample.txt", "r", encoding="utf-8") as f:
  # 앞으로 이렇게 들여쓰기 된 코드가 끝나면
  # 파일 접근을 닫습니다(close)

  # 텍스트파일 파일 한줄씩 문자열을 만들기
  lines = f.readlines()
  print(lines)

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

# 실습 3. a 모드로 기록 이어붙이기
# 1) with open으로 파일을 추가 모드 a로 열기
with open("hello.txt", "a", encoding="utf-8") as f:
  # 2) write로 새 기록 문장을 쓰기
  f.write("사실 반갑죠?\n")
  f.write("아니라고요? 에반데\n")
# 3) w 모드와 달리 기존 내용이 보존됨을 확인
# '4)'에서 기존 내용이 보존됨을 확인
# 4) r 모드로 열어 전체가 쌓였는지 확인
with open("hello.txt", "r", encoding="utf-8") as f:
  read_f = f.read()
  print(read_f)
# 안녕하세요
# 반갑습니다      아님말고
# 사실 반갑죠?
# 아니라고요? 에반데