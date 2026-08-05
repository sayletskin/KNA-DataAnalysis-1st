# 07_03 함수 설계와 활용

# 기본값 인자
# name과 value는 호출할 때 꼭 매개변수를 지정해줘야하지만
# unit은 지정/언급 안해주면 "도(℃)" 기본값으로 정해진다

def report(name, value, unit = "도(℃)"):
  print(f"{name} : {value}{unit}")

report("압축기A", 75.3)

# 기본값 알아보기
def is_over_limit(value, limit = 90):
  if value > limit:
    return True # 위험 맞음
  return False # 위험 아님

print(is_over_limit(88)) 
# limit은 보통 고정값인 경우가 많음 ex)교통속도
# 따라서 이런 변수들은 기본값 인자로 처리하면 좋음
print(is_over_limit(88, 80))

# 실습1
# 기본값이 인자 함수 만들기
#①def 괄호안매개변수에=로기본값을지정
#②인자를생략하고호출해기본값이쓰이는지확인
#③인자를넣어호출해기본값을덮어쓰는지확인
#④필수매개변수는앞, 기본값매개변수는뒤순서규칙확인

# 바로 앞 코드들로 대체

# 02. 지역변수와 범위
# scope!!!
# 코드의 어디부터 어디까지 이 변수 데이터가 살아있을까?

outter = 100

def change_outter():
  # 아래 코드는 함수 내부에서 처음 언급
  # 새롭게 만들어진 내부 outter이고 (지역변수)
  # 함수가 조료되면 메모리에서 사라진다
  # 함수 바깥의 같은 이름의 존재에는 영향x
  outter = 50

change_outter()
print(outter) # 100

# 실습 2
# 함수 안에서 만든 지역변수가 함수 밖에서 보이지 않음을 확인
# 앞의 예제