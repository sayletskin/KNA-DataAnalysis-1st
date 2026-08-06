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