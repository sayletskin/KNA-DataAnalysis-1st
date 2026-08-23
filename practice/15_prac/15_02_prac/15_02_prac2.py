import pandas as pd

df = pd.read_csv('data/15_02_사출성형_공정.csv', encoding='utf-8')
# print(df.columns)
# Index(['측정시각', '불량여부', '사출기', '사이클시간', '성형사클', '이배럴온도1', '배럴온도2', '배럴온도3',
#        '배럴온도4', '호퍼온도', '스크루속도', '사출압력', '스크루위치', '전환위치', '계량시간', '계량시작위치',
#        '계량시작점', '최소쿠션', '최대사출압', '전환압력', '최대사출속도', '감압시간'],
#       dtype='str')

# 실습 2. dropna 옵션 조절
# how·thresh·subset로 삭제 기준을 세밀하게 조절

# · how로 완전히 빈 행만 삭제하는 기준 적용 -> how = 'all'
print(df.dropna(how = 'all').shape) # (250, 22)
# 250개 row가 다 살아남았다는 의미 
# : NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻

# · thresh로 값이 일정(예, 20개) 개수 "이상"인 행만 남기기 -> thresh = 20
print(df.dropna(thresh = 20).shape) # (162, 22)
# 250 - 162 = 88개 row는 NaN이 3개 이상이라는 뜻

# · subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거 -> subset = ['불량여부']
print(df.dropna(subset = ['불량여부']).shape) # (250, 22)
# '불량여부' 컬럼에는 NaN이 하나도 없다고 판단 가능

print(df.dropna(subset = ['사이클시간']).shape) # (250, 22)
print(df.dropna(subset = ['최대사출압']).shape) # (190, 22)
print(df.dropna(subset = ['전환압력']).shape) # (182, 22)
