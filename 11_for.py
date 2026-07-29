# 반복문은 동일한 작업을 특정 횟수만큼 반복해야할 때
# 코드를 길게 쓰지 않고 반복시킬 수 있음

# for(예약어) 변수 in range(횟수):
#   반복시킬 코드 (들여쓰기 한 칸 필수)
# 같은 코드를 복사 붙여넣기로 여러번 작성하는 대신
# "N번 실행하라"는 의미
# i 는 index의 약자로 자주씀

for i in range(3):
  print("안녕하세요") # range에 전달한 인자 3만큼 3번 반복
  # i를 쓰지 않아도 됨 -> 단, 목적이 "3번 반복"일 때

# 0부터 10까지의 숫자 자체가 필요하거나 출력할 때
for i in range(11):
  print(i)
  # i는 증가값을 지정하지 않는 이상 반복할 때마다 자동으로 +1이 적용됨

# 0부터 10까지 짝수만 필요할 때
for i in range(0, 11, 2): # range(시작, 끝, 증가값)
  print(i) # 반복할 때마다 i가 2씩 증가

# 실습 > 1부터 10까지 홀수만 출력
for i in range(1,11,2):
  print(i)

# 역순 출력
for 아이 in range(10, 0, -1): 
  print(아이)

# 10 부터 1까지 짝수만 역순 출력
for 아잉 in range(10,0,-2):
  print(아잉)

for i in range(0,10,-2):
  print(i)
# 동작 안함
# 시작값인 0에서 -2를 했을 때 끝 값이 포함되지 않아서 반복문 종료

# 실습
#N = int(input("자연수: ")) # N = 5 일 때
#for i in range(1, N+1, 1):
  print(i) # 1 2 3 4 5
#for i in range(2, N+1, 2):
  print(i) # 2 4 
#for i in range(N, 0, -1):
  print(i) # 5 4 3 2 1

# 실습. 3의 배수 출력하기
# 사용자에게 범위를 입력받아 3, 6, 9를 포함한 숫자인 경우 출력하기
# 예)
  # 사용자 입력값: 20
  # 출력값: 3, 6, 9, 12, 15, 18
# for문, if문, 나머지 연산자만 사용
# i % 3 == 0 을 이용

num = int(input("범위 입력(숫자): ")) # num = 24

for i in range(1,num+1):
  if i % 3 == 0:
    print(f"입력한 1~{num}사이 3의 배수 출력: {i}") # 3 6 9 12 15 18 21 24
  elif i % 5 == 0:
    print(f"입력한 1~{num}사이 3의 배수 출력: {i}") # 미출력 , 3의 배수가 아니면서 5의 배수는 없다

total = 0
for i in range(1, 6):
  total += i # += 재할당연산자 total = total + i
  print("합계:", total)

for i in range(1, 6):
  total2 = 0 # 반복을 돌 때마다 total2에 값이 0으로 할당
  total2 += i
  print("합계:", total2) # 가장 마지막 i인 5 출력

if 3 == 3: 
  hi = "안녕" # False면 할당 안됨ㅋㅋ
print(hi)
# Python에서는 if문 안의 변수도 어디서든 호출 가능한 변수로 선언됨
# 교훈 if문은 몰라도 for문 안에서는 변수를 할당하지 말자

# 1~15 사이의 4의 배수만 누적
total3 = 0
for i in range(1, 16):
  if i % 4 == 0:
    total3 += i
    print(total3) # 1~15까지의 4의 배수 합

# 개수 세기
count = 0
for i in range(1, 100):
  if i % 13 == 1:
    count += 1
    print(count) # 1~99 까지 수를 13 나눴을 때 나머지가 1인 수의 갯수 , 8

# 평균 구하기
total4, count2 = 0, 0
#for i in range