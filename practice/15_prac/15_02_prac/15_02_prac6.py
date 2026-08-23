import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')

# 실습 6. 최빈값·앞뒤 값 대체
# 범주형은 최빈값, 시계열은 앞뒤 값으로 채우기

# · 범주형 열의 최빈값을 구해 채우기
# 사출기 컬럼은 1혹기~3호기 범주형으로 판단
# 감압시간 컬럼으로 해보기
print(df['감압시간'].isna().sum()) # 109 개 ㄷㄷ
print(df['감압시간'].mode()[0]) # 0.32 값이 가장 많음 

df['감압시간'] = df['감압시간'].fillna(df['감압시간'].mode()[0])
print(df['감압시간'].isna().sum()) 
# 109개의 NaN을 0.32로 채워서 0개

# · 측정시각 순으로 정렬해 시계열 순서 만들기
df = df.sort_values('측정시각')
# 과거에서 현재 순서로 정렬

# · ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
# 전환압력 컬럼을 계량시작점 컬럼으로 바꿔서 해보기
print(df['계량시작점'].isna().sum()) # 34개 NaN 확인
df['계량시작점'] = df['계량시작점'].ffill().bfill()
# 자주 볼 시계열 채우기 패턴
print(df['계량시작점'].isna().sum()) # 0개 NaN 확인
