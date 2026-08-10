# 실습 1. open으로 파일 읽기
# 1) open으로 파일을 읽기모드 r, utf-8로 열기
t = open("sample.txt", "r", encoding="utf-8")
print(type(t).__name__) # TextIOWrapper

# 2) read로 전체를 한 문자열로 읽어 출력
line = t.read()
print(line)

t.close()

# 3) readlines로 줄 리스트로 읽어 출력
t = open("sample.txt", "r", encoding="utf-8")
lines = t.readlines()
print(lines)

t.close()

# 4) 두 방식의 결과 차이
# read를 썼을 때
# Hello world
# 안녕하세요
# 반갑습니다
# readlines를 썼을 때
# ['Hello world\n', '안녕하세요\n', '반갑습니다']

# read는 문서 전체를 그대로 옮겨 출력했고,
# readlines는 문서 전체를 옮겼지만 \n을 이용해서 한 줄로
# 이루어진 리스트를 출력했다