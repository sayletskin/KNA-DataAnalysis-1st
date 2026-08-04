# 실습 4. 반환값으로 간단 계산기 만들기
# 1) 값을 받아 계산하는 함수를 정의
# 2) 계산 결과를 print말고 return쓰기
def calc_sum(a, b):
    return a + b

# 3) 호출 결과를 변수에 담기
result = calc_sum(10, 12)
# 4) 담은 값을 다음 계산.출력에 이어 쓰기
print(result) # 22