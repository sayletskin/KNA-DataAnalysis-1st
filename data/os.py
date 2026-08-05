# 절대경로
# 예 : python C:\Users\sayletskin\바탕화면\sample\code.py

# C:\Users\sayletskin\바탕화면\sample 폴더에
# 터미널을 연 상태에서 code.py 코드를 실행하고 싶다면
# python code.py

# 위 code.py 언급부분은 사실 상대경로를 의미한다
# 그래서 절대경로로 지정해줘도 똑같이 실행될 것이다

# 현재 경로에 있는 해당 파이리란걸 더 강조하는 상대경로 지정으로 써도 된다
# python ./code.py 

# 상대경로
# 예 : python ..\sample\code.py
# 뭐가 다른거야

# 표준 라이브러리 os 모듈 활용

# 현재 작업 중인 폴더(디렉터리)의 위치
import os
current_working_directory = os.getcwd()
print(current_working_directory)
# C:\Users\PC2507\Desktop\KNA-DataAnalysis-1st

# 현재 작업 중인 폴더 안에 있는 파일 목록
file_list = os.listdir()
print(file_list)
for file_name in file_list:
  print(file_name)

print("=" * 20)

# 파일이 존재하는지 알아보기
# 운영체제마다(윈도/맥/리녹스)마다 경로를 나타내는 방법이 달라서
# 상황에 맞게 경로문자열을 만들어주는 os의 함수를 사용합시다
path = os.path.join("data", "08_press.csv")

# 실제로 경로 문자열을 따라서 찾아가면
# 해당 파일이 있는지 알아보자 : .exist Bool형
if os.path.exists(path):
  print(f"파일 있음: {path}")

print(os.path.exists(path))

