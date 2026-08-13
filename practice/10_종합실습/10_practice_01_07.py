# 실습7. 센서 데이터 표로 정리하기
import numpy as np

# 시점과 센서 수를 곱한 개수만큼 연속값을 arange로 생성
# 한 시간마다 시점 3시간, 센서 4개
sensors = np.arange(12)

# · 행을 시점, 열을 센서 수로 정해 reshape로 표 형태 변환
converted_sensors = sensors.reshape(3, 4)

# · 정리된 표 배열 출력
print(converted_sensors)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]