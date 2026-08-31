import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding='utf-8')
# print(df.columns)
# Index(['측정시각', '불량여부', '사출기', '사이클시간', '성형사이클', '배럴온도1', '배럴온도2', '배럴온도3',
#        '배럴온도4', '호퍼온도', '스크루속도', '사출압력', '스크루위치', '전환위치', '계량시간', '계량시작위치',
#        '계량시작점', '최소쿠션', '최대사출압', '전환압력', '최대사출속도', '감압시간'],
#       dtype='str')

#  실습5. fillna 평균·중앙값대체
# 결측을 평균과 중앙값으로 채우고 차이 이해
print(df['전환압력'].isna().sum()) # 68
# 전환압력 열에 68개의 NaN확인

# · 대상 컬럼의 평균과 중앙값을 각각 구해 비교
v_mean = df['전환압력'].mean()
v_median = df['전환압력'].median()
print(v_mean, v_median) # 1211.9797252747253 1223.63

# · fillna로 평균을 채운 결과 만들기
v_fillmean = df['전환압력'].fillna(v_mean)
# v_fillmean = 전환압력 열의 NaN을 전환압력 평균값으로 채움 
print(v_fillmean.head())
# 0    1211.979725 평균
# 1    1211.979725 평균
# 2    1234.850000
# 3    1228.120000
# 4    1211.979725 평균

print(v_fillmean.isna().sum()) # 0

# · fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
v_fillmedian = df['전환압력'].fillna(v_median)
# v_fillmedian = 전환압력 열의 NaN을 전환압력 중앙값으로 채움
print(v_fillmedian.head())
# 0    1223.63 중앙값
# 1    1223.63 중앙값
# 2    1234.85
# 3    1228.12
# 4    1223.63 중앙값

print(v_fillmedian.isna().sum()) # 0
