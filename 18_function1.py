# print 함수를 생각해봅시다
print("안녕하세요")
first_name = "SayLets"
last_name = "Kin"
print(first_name)
print(last_name)
print(first_name, last_name)
print(f"{first_name}{last_name}")
print("========================")
# 위와 같이 똑같은 print함수 호출할 때도 다양한 방법이 있음
# 그 원리를 알려면 '우리가 직접 함수를 만들 수 있어야함'

# error의 종류
# 1. 실행중에 오류 (Runtime Error) - 작동 중단됨
# 2. 논리적 오류 - 작동은 되는데, 결과적으로 문제가 있어 고쳐야 함
# 우리는 함수 이름에 걸맞는 동작만 잘 되도록 만들어야 함

# 1) 간단한 인사메세지 보여주기 함수 만들기
# ":"으로 끝나는 줄의 뜻은 "이 다음 줄부터 들여쓴 내용은 한 묶음"
# 그래서 들여쓰는 구나
def say_hello(): # 여기가 길어질 예정
  print("안녕하세요") # print 안됨

# 위에서 만든 함수는 호출해야만 실행
say_hello() # 안녕하세요

# 2) 함수 안에서 벌어지는 일들을 만들어봅시다
def show_number():
  my_number = 44
  print(f"my_number: {my_number}")

show_number() # 44
# 여기서도 my_number 값을 정해봅시다
my_number = 24 
# 위 줄의 my_number와 함수 안의 my_number는 별개
show_number() # 44

# 그래서 함수 안의 my_number 데이터가 영향을 끼치는 범위를
# 전문용어로 scope(스코프)라고 부른다
# 함수언어(show_number)가 변수(my_number)에 끼치는 스코프 (29~30번 줄)

# 함수는 호출되기 전에 만들어져야 함
# show_title() # NameError: name 'show_title' is not defined
def show_title():
  print("함수 배우기")

show_title()

# 함수가 호출되면 그 안의 코드는 매번 새롭게 시작된다

def show_counter():
    # count += count + 1 # 기존 count라는 존재는 모른다고 error
    count = 1
    print(count)
    # 이 함수가 종료되면 count를 포함한 이 함수 안의 데이터는 모두 사라짐

show_counter()
show_counter()

# 각 함수의 이름은 이름에 걸맞는 역할만 해줘야 한다
def show_students():
   print("학생1: 짱구")
   print("학생2: 철수")
   print("학생3: 훈이")

def show_teacher():
   print("선생님: 채성아")

show_students()
show_teacher()

def show_classroom():
    show_students()
    show_teacher()

show_classroom()

# 코드 중복과 함수화

print("압축기A 온도 확인 중")
print("결과를 기록합니다")
print("펌프 1 온도 확인 중")
print("결과를 기록합니다")

# 위와 같은 코드를 복붙하면 언젠가 실수로 사고 생길 수 있음

# 실습 2. 모범답안
def start_check():
   print("점검을 시작합니다")
   print("안전 장비를 확인하세요")
   print("기록을 준비하세요")

start_check() # 압축기A
start_check() # 펌프1

# 함수의 호출 결과 예측하기
def say_hi():
   print("안뇽")

say_hi()
say_hi() # 안뇽 2번