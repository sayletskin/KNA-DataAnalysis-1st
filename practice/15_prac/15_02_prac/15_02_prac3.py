import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
print(df.shape) # (250, 22)
print(df.isna().sum())

# 실습 3. 결측 비율 기준 컬럼 제거
# 결측 비율이 높은 컬럼만 골라 제거

# 단계
# · 컬럼별 결측 비율을 계산
df_rate = df.isna().sum() / len(df)
# 컬럼별 결측 비율 = (각 컬럼) 결측 수 / 전체 row 개수 
print(df_rate)

# · 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기 
# -> 40% 이상 NaN으로 채워진 컬럼 목록
df_terminates = df_rate[df_rate > 0.4]
# 컬렴별 결측 비율이 0.4 이상인 컬럼
print(df_terminates)

# 최초 컬럼 이름들이 df_terminates의 index labels가 되었다.
list_terminates = df_terminates.index.tolist() # ['최대사출속도', '감압시간']
# 0.4 이상인거 컬럼 리스트로 뽑아내기
print(list_terminates)

# · 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
df_final = df.drop(columns = list_terminates)
print(df_final.shape) # (250, 20)
# (250, 22)였던 df가 결측 비율 0.4 이상인 컬럼 2개를 지워서
# (250, 20)가 되었다.

# 예상 결과
# 40% 초과 센서19·20 제거 → 250×20