import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
df.info()

# 실습 1. dropna로 행·열 삭제
# 결측 있는 행과 열을 삭제하고 크기 변화 확인
# 결측 있는 행과 열을 삭제하고 크기 변화 확인

# · 원본 크기를 shape로 확인
print(df.shape) # (250, 22)

# · dropna로 결측 있는 행을 모두 삭제
print(df.dropna().shape) # (76, 22)
# 250-76= 174개의 행이 NaN가 있어서 삭제됨

# · 방향을 열로 바꿔 결측 있는 열을 삭제
print(df.dropna(axis = 1).shape) # (250, 10)
# 22-10 = 12개의 열에 NaN가 있어서 삭제됨

# 예상 결과
# 250×22 → 행삭제 76×22, 열삭제 250×10