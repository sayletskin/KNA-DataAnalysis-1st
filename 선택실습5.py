# 선택실습 5. 센서 통계 함수 만들기
# 1) 센서값 목록을 매개변수로 받는 함수를 정의
# 2) min,max, min-max평균 계산
# 3) 세 값을 쉼표로 함께 return
sensors = [ 78, 79, 91, 92]

def calc_min_max(value):
    minimum = min(value)
    maximum = max(value)
    return minimum, maximum, round((minimum + maximum) / 2, 1)

# 4) 돌려받은 값을 세 변수로 언패킹해 출력
result = calc_min_max(sensors)
print(result) # (78, 92, 85.0) 튜플