# 09_01_예외처리_기초
# 실습 2

origin = input("온도 : ")

print(f"입력한 온도는 {origin}")

temp = 0 

try:
    temp = int(origin)
except ValueError:
    # ValueError인 상황이었다면 여기로 예외처리
    print("숫자 아니면 왜 저를 부르셨어요? 0으로 생각할께요")
except TypeError:
    # TypeError인 상황이었다면 여기로 예외처리
    print("타입 문제는 전지구적 문제입니다.")

next_temp = temp + 10
print(f"10도만 더 높으면 {next_temp}")