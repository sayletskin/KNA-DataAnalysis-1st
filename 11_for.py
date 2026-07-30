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
for i in range(1, 60):
  if i % 15 == 0:
    count2 += 1
    total4 += i
    print(total4, count2)
    print(total4 / count2)

print("=== 구분선 ===")

# enumerate (낱낱이 세다) < 리스트 필요 
temps = [33, 23, 45, 32, 28]

for t in enumerate(temps):
  print(t) # (인덱스, 요소값) < 객관적으로 쓰기 불편함 따라서 
# 범위를 지정하지 않아도 enumerate()에 전달한 리스트의 모든 요소 순화
# 문제는 형식이 (인덱스, 요소값)로 출력
# enumerate를 사용할 때는 변수를 2개 전달

for idx, t in enumerate(temps): # 내가 저 위에 total4, count2 = 0, 0 복합 할당한거 처럼 idx, t = (인덱스), (요소값) 으로 복합 할당 / 순서 중요
  print(f"idx: {idx}, t: {t}") # idx: (인덱스), t : (요소값) < 이건 쓰기 편한가?

# for, idx, t in enumerate(temps):
# 위와 같이 전달하면 enumerate가 temps 리스트를 순회하면서
# 반환해준 (인덱스, 해당인덱스의값)을
# 각자 idx에 인덱스 값을 할당, t에 해당 인덱스값을 할당
# 두 개의 값을 바로 사용할 수 있게 해줌

for idx, t in enumerate(temps):
  print(f"현재 인덱스: {idx}")
  print(f"{idx}인덱스의 값: {t}")
  print(f"{idx+1}번째 반복 끝")
# 앞에서 range에 썼던 i와 지금 enumerate의 idx는 다르다 i는 인덱스가 아니고 idx는 순수 인덱스다

# 안녕의 인덱스 출력

# 이를 위해서는 값을 비교하기위해 모든 리스트의 값이 필요
# 그리고 그 값의 인덱스를 알아야 출력
list1 = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# 리스트의 모든 요소에 접근을 해야 하는 경우가 잦음
# 그래서 Python이 반복문에서 이를 쉽게 할 수 있도록
# enumerate라는 내장 함수를 제공
# enumerate은 리스트의 모든 요소를 앞에서부터
# 순서대로 하나씩 찍어가면서 접근
# 접근해서 각자의 인덱스와 그 값을 뽑아줌 -> 돌려주는 값은 2개
# 값을 두 개 받으니 우리도 변수 2개 준비하면
# 각 변수에 쏙쏙 값이 할당
# 돌려주는 순서는 인덱스, 값
# 그렇기 때문에 우리는 enumerate를 사용할 때
# for 뒤에 변수를 두 개 전달
for index, value in enumerate(list1):
  if value == "안녕":
    print(index) # 채고다 enumerate!!!
# 참고로 위에 있는 코드는 "안녕"이라 적힌 요소값의 인덱스를 뽑아내는 코드다

# range > 인덱스 추출인데 요소값 뽑아내는 법
list1_len = int(len(list1))
print(list1_len) # 6
for i in range(list1_len):
  print(list1[i])

# 실습
N = int(input("숫자: "))
result = 0

for i in range(1, N+1):
  result += i
  print(result)
# ===============================
# 구구단 만들기

# 2단
for su in range(1,10):
  print(f"2 X {su} = {2 * su}")

# 1~5단 출력
# 필요한 변수: 2개 (몇 단을 출력할건지, 거기에 얼마나 곱할건지)
# 몇 단을 출력할건지 1~5, 거기서 얼마나 곱할건지: 1~9
# for문 중첩을 사용

# 단수를 유지하고 아네서 또 점점 커지는 변수가 있어야 하니
# 바깥 for문은 단수를 늘리고
# 안쪽 for문은 곱할 수를 늘리도록 구성
for i in range(1, 6): # 1~5 까지 반복
  for j in range(1, 10): # 1~9 까지 반복 종료
    print(f"{i} X {j} = {i * j}")
  print(f"===={i}단 끝====")

# 1~9 단 사이 2의 배수 단만 구구단 출력
# 2, 4, 6, 8단 만 출력
# 방법1) range에 간격 전달
# 방법2) if문 사용

for i in range(2, 10, 2):
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")

for i in range(1,10):
  for j in range(1,10):
    if i % 2 == 0: # i = 2, 4, 6, 8
      print(f"{i} X {j} = {i * j}") # 2 X 1 = 2 시작해서, 8 X 9 = 72 로 끝남
