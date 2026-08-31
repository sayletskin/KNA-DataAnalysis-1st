# 실습3. 두조건묶기
# 두 조건을 그리고·또는로 묶어 행을 추출
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
# df.info()

# 비스킷두께 조건과 사이클타임 조건을 각각 괄호로 감싸기
df_sub1 = df["비스킷두께"] >= 15
df_sub2 = df['사이클타임'] >= 30
print(len(df[df_sub1]), len(df[df_sub2])) # 5, 6

# 두 조건을 그리고 기호로 묶어 모두 만족하는 행 추출
print(len(df[ (df_sub1) & (df_sub2) ])) # 4

# 같은 두 조건을 또는 기호로 묶어 결과 수 비교
print(len(df[ (df_sub1) | (df_sub2) ])) # 7
