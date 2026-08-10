# except들의 연속과 finally 코드

# text = "24.5" # 정상
text = "영크크" # 비정상

try:
  temp = float(text)
except ValueError:
  print("ValueError문제가 발생했습니다")
  temp = 0
except NameError:
  print("NameError문제가 발생했습니다")  
finally:
  # 오류가 있건 없건 finally의 코드 실행
  print(temp * 2)

print(text * 2)
