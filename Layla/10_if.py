# 조건문 - if
# 항상 실행되지 않고 조건에 따라서 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True 와 False로 결과가 나와야 함

# if 조건식:
#   실행할 코드 (한 칸 들여쓰기(tap))

# if문의 :(콜론)은 그 다음 올 코드가 if문 조건식의 결과가 True일 때만 실행하라는 의미
# 들여쓰기 한 코드는 if문의 조건식 결과가 True일 때 실행
# 즉, 여기서부터 이 조건에 속한다라는 신호
# 조건에 속하는 코드는 모두 들여쓰기가 적용되어있어야 함

temp = 85

if temp > 80: # 만약 temp라는 변수에 담긴 값이 80보다 크다면?
  print("temp 변수의 값이 80보다 크다!!!")
  print("🚨 점검 요망 🚨")
print("이건 상시 코드")

temp = 50

if temp > 80:
  print("temp 변수의 값이 80보다 크다!!!")
  print("🚨 점검 요망 🚨")
print("이건 상시 코드")
# 50이 80보다 큰 지 비교하고 False라는 결과를 확인하면 들여쓰기 한 코드는 실행X

# temp 변수의 값이 80보다 크다면 "경고" 출력
# temp 변수의 값이 80 이하라면 "정상" 출력
# 위 두 가지를 모두 하고싶은 경우

temp = 90

# 1안
if temp > 80:
  print("경고")
if temp <= 80:
  print("정상")
# 번거로움, 식상함, 논쟁의 여지가 있음, if문을 2개씀

# 2안 > else 사용
if temp > 80: # if문 True 일 때 실행
  print("경고")
else: # if문 False 일 때 실행
  print("정상")
# if문의 코드블럭과 else문의 코드블럭은 절대 동시에 실행되지 않음
# 둘 중 하나만 실행
# 1개의 분기로 코드를 실행해야할 때 사용

# if문 실습
# 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성하기
# 성인 > "성인입니다.", 미성년자 > "미성년자입니다." 출력
age = int(input("나이: "))
if age >= 19:
  print("성인입니다.")
else:
  print("미성년자입니다.")

# 숫자 맞추기 게임(?)
num = int(input("숫자맞추기: "))
if num == 50:
  print("정답")
else:
  print("오답")
print("게임종료")

# 예시
# 정답을 50으로 지정
# 사용자에게 입력값 받기
# 정답과 동일하면 맞다고 출력 아니면 틀렸다 출력

answer = 50
user_answer = int(input("정답입력: "))

if answer == user_answer:
  print("정답")
else:
  print("오답")
print("게임종료")

# 신호등 색을 입력받아서
# "초록색"이라면 "건너세용" 출력
# "빨간색"이라면 "기다리세용" 출력
# 입력값이 초록색이나 빨간색이어야만 정상동작 하도록
# 이상한 값 입력시 "다시 입력하세요" 출력

# or 사용 + if문 중첩
color = input("신호등 색깔(빨간색or초록색): ")
if color == "초록색" or color == "빨간색": # color가 "초록색"이거나 "빨간색" 일 때 실행
  if color == "초록색":
    print("건너세요") # 중첩 if문은 들여쓰기 주의
  else: # 'if color == "빨간색":'이랑 같음
    print("기다리세요")
#  print("이건 언제 실행될까?") # 사용자 입력값이 초록색 이거나 빨간색일 때 무조건 출력
else:
  print("다시 입력하세요")

# and 연산자 + 중첩

# 사람 체온 판단
# 정상 체온 범위: 36.2~36.9

user_a = float(input("체온을 입력해주세요: "))
if user_a >= 36.2 or user_a <= 36.9:
  print("당신은 정상체온입니다.")
else:
  if user_a < 36.2:
    print("당신은 저체온 입니다.")
  else:
    print("당신은 열이 나고 있습니다.")
print("체온 판단 종료")

if user_a < 36.2 or user_a > 36.9:
  if user_a < 36.2:
    print("저체온")
  else:
    print("고열")
else:
  print("정상체온")
print("체온 판단 종료22")
# 위의 체온 판단 if문 안에서 열나는지 저체온인지 판단하도록 수정
# if문 중첩 자체는 무한히 가능 하지만 권장X

# elif
# else와 if만으로 분기하기에는 불편하고, if 중첩이 너무 많아져서 생김

# 미열 고온 구분하기
if user_a <= 36.2:
  print("당신은 저체온입니다.")
elif user_a >= 36.9 and user_a < 37.8:
  print("당신은 미열입니다. 주의하세요.")
elif user_a >= 37.8:
  print("당신은 고열입니다. 병원에 방문하세요.")
else:
  print("당신은 정상체온입니다.")
print("체온 확인 완료333")
# elif > if문에서 False일 때 else 와 if 를 합쳐서 그 외의 경우를 if로 이어나갈 수 있다.

# elif의 순서

score = 100
# if score >= 50:
#   print("미흡")
# elif score >= 70:
#   print("보통")
# elif score >= 90:
#   print("우수")
# else:
#   print("비상!!!")
# 100이기 때문에 우수가 출력되야하지만 코드의 순서가 적합하지 않아서 "미흡"이 출력

if score >= 90:
  print("우수")
elif score >= 70:
  print("보통")
elif score >= 50:
  print("미흡")
else:
  print("비상!!!")
# 까다로운 조건을 위에 넓은 조건을 밑에

# not 연산자

if not ( 3 == 5 ):
  print("출력됨")
# 3 == 5 는 False 이고 not 때문에 True가 되어서 프린트 출력됨

# if문은 줄바꿈 하지 않아도 :을 기준으로 동작 자체는 가능
# 그러나 줄바꿈해서 가독성을 높이는 걸 권장
# 탭은 아직 위의 코드가 끝나지 않았고 한 줄이라는 것을 명시
if score >= 90: print("우수") # 작동됨

# 실습
temp = float(input("온도 입력: "))
if temp >= 80:
  print("위험")
elif temp >= 60:
  print("주의")
else:
  print("정상")

# 실습
my_id , my_pw = "king", "123"
user_id = input("아이디: ")
user_pw = input("비밀번호: ")
if my_id == user_id and user_pw == my_pw:
  print("로그인 성공")
else:
  print("로그인 실패")

# 실습
temp = float(input("온도: "))
vip = float(input("진동: "))
cur = float(input("전류: "))
if temp > 80 or vip > 4.0:
  print("위험:즉시 정지")
elif cur > 60 and temp > 70:
  print("주의:부하 점검")
elif vip > 2.5:
  print("진동 관찰")
else:
  print("정상") # 78, 3.2, 52 > "진동 관찰"