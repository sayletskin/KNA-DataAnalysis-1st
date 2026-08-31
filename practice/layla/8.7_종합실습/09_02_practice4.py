# [실습4] 함수 안에서 입력값 검증하기
# 1) 입력값을 받은 함수를 정의
def output_float(value):
# 2) try에서 float로 변환해 검증
  try:
    num = float(value)
    return num 
# 3) 변환 실패 시 except로 안내하고 기본값 처리
  except ValueError:
    print("ValueError발생, 기본값 0으로 대체")
    return 0
# 4) 정상·비정상 입력을 각각 넣어 확인
print(output_float("222")) # 정상
print(output_float("영크크"))
# ValueError발생, 기본값 0으로 대체, 0