# 인삿말 출력 함수 간단 버전
def say_hello():
  print("안녕하세요")

say_hello()

# 인삿말 출력 함수 친근 버전
def say_hello_ned():
  print("안녕하세요, Ned")

def say_hello_tuna():
  print("안녕하세요, Tuna")

say_hello_ned()
say_hello_tuna()

# 인사할 대상이 많아진다고 함수를 더 많은건 비효율
# 해결책은 하나의 함수에서 다양성을 대응해주는 것
# 그것을 해결해줄 함수 매개변수 활용

def say_hi(name):
  print(f"안녕, {name}")

say_hi("Ned")
say_hi("Tuna")

# 예제코드 : 특정 장비 이름을 알려주면 해당 장비의 체크를 시작 알림
def check(name):
  print(f"{name} 장비의 점검을 시작합니다")

check("압축기")

# 매개변수가 2개 이상인 - 덧셈
def calc_sum(number_a, number_b):
  #number_a = 1
  #number_b = 2
  total = number_a + number_b
  print(f"{number_a} + {number_b} = {total}")

calc_sum(2,2)

# 매개변수가 2개 이상인 - 장비 이름과 온도
def report(name, temp):
  # name = "압축기A"
  # temp = 75.3
  print(f"{name}의 온도는 {temp}도 입니다")

report("압축기A", 75.3)
report("펌프B", 85.2)

# 엉뚱하게 호출
report(85.2, "펌프B")
# 원하지 않는 결과가 나올 수 있다

# 매개변수가 부족하거나 더 있으면
# report(85.2, "펌프B", "가동률") error
# report("펌프B") error

# 키워드 인자
def report_keywords(name, temp):
  print(f"{name}의 온도는 {temp}도 입니다")

# 키워드 인자 없이 호출
report_keywords(37.4, "펌프A") # 서순 문제 발생

# 키워드 인자 사용해 호출
report_keywords(temp = 37.4, name = "펌프A") # 잘나옴
# 순서 바꿔 호출해 생기는 문제 근본 차단

# ===========================================
# 반환값

def ad(a, b):
  total = a+b
  return total

print(ad(1, 2))

def add(a, b):
  return a + b

# 여러번 같은 결과를 호출한다면
# 차다리 변수에 담아서 쓰자
result = add(1, 2)
print(result + 1)
print(result + 2)
print(result + 3)

# 평균 내는 함수 만들기
def calc_average(a, b):
  return (a + b) / 2

avg = calc_average(75.3, 88.7)
print(f"평균 온도: {avg}")

# 여러 값을 한번에 반환하기
# 다음의 함수는 배열을 받아서 그 안의 
# 최소값과 최대값을 동시에 return한다

def calc_min_max(values):
  minimum = min(values)
  maximum = max(values)
  return minimum, maximum

target_list = [1,2,3,4,5,6]
result = calc_min_max(target_list)
print(result) # 튜플인 것을 확인 (1, 6)

# 반환값을 언패킹으로 받기
# 함수의 결과를 받는 순간에
# 결과 튜플의 내용을 풀어서
# 개별 변수에 담아 사용하기
result_min, result_max = calc_min_max(target_list) 
print("최소값:", result_min,
       "\n최대값:", result_max)

# return 반환값이 없는 함수를 호출해놓고
# 결과를 어디에 담겠다고 하면,
# 담기는 값은 None이 된다

def say_great():
  print("반갑습니다")
  return

great = say_great()
print(great)
