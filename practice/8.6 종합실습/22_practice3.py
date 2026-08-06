# 실습3. 구체적 예외로 입력 검증하기
# 1) 입력을 int로 바꾸는 코드를 try에 넣기
try:
  num = int(input("숫자 입력(1~100, 0제외): "))
  print(f"100을 {num}등분하면 {100 / num}등분")
# 2) ValueError를 except로 잡아 안내
except ValueError:
  print("ValueError발생, 숫자 입력하라고")
# 3) 여러 except로 ZeroDivisionError도 구분해 처리  
except ZeroDivisionError:
  print("ZeroDivisionError발생, 0제외라고")
# 4) 잘못된 입력을 넣어 프로그램이 멈추지 않는지 확인
# 논리적 에러를 제외한 
# str은 ValueError로 0은 ZeroDivisionError으로
# 정상작동