temp = -1

try:
  temp = int("스쿨")
except:
  print("해봤는데 안되네요^^")
  temp = 0 # 후처리, 문제가 있어도 잘 진행되도록 대안/추가 처리 필요

print(temp) # 0