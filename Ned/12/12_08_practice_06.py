# 실습 6. read_csv 옵션 종합 연습
# G O A L 경로· 인코딩· 구분자· 열 선택을 한 번에 적용

# 세미콜론+한글 파일에서 필요한 열만
# sep + encoding + usecols → 200행 3열

# 여러 옵션을 함께 써서 shape 확인

# -------------------------------------
# 파일 : data 폴더 안의 12_metro_compressor_semicolon.csv
# sep를 잘 사용해서 여러 컬럼이 읽히도록 해주세요
# encoding도 지정해주세요
# 모든 컬럼을 다 읽지는 마시고, '측정시각', '오일온도', '모터전류' 컬럼만 읽어주세요

import pandas as pd
import os

path = os.path.join("data", "12_metro_compressor_semicolon.csv")

df = pd.read_csv(path, encoding="utf-8", sep=";", 
     usecols=['측정시각', '오일온도', '모터전류'])

print(df.shape) # (200, 3)
print(df.head()) 
#                   측정시각  오일온도  모터전류
# 0  2020-02-27 06:38:47  51.3  6.04
# 1  2020-02-27 07:28:21  56.8  0.04
# 2  2020-02-27 08:17:54  55.7  0.03
# 3  2020-02-27 09:07:27   NaN  3.81
# 4  2020-02-27 09:57:01  55.3  0.04