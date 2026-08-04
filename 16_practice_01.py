# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)
# 

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 (누적변수)


# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)


# TODO 4. 전체 평균 온도 출력 (round)


# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)


# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())


# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
num, normal, warning, danger, temp_total, first = 0, 0, 0, 0, 0, 0 
temp_max = first
danger_name = []
print("========================================")
print("         설비 종합 모니터링 리포트        ")
print("========================================")
for name, temp, vip in sensors:
    num += 1
    if temp > 90 or vip > 5.0:
        danger += 1
        stat = "위험"
        danger_name.append(name)
    elif temp >= 80 or vip > 3.0:
        warning += 1
        stat = "주의"
    else:
        normal += 1
        stat = "정상"
    print(f"{num}. {name} | 온도 {temp} | 진동 {vip}mm/s | {stat}")
    if temp_max < temp:
        temp_max = temp
        name_max = name
    temp_total += temp
print("----------------------------------------")
sens_count = danger + warning + normal
danger_name.sort()
print(f"총 설비: {sens_count}대")
print(f"정상: {normal} / 주의: {warning} / 위험: {danger}")
print(f"이상 설비 비율: {round((danger + warning)/sens_count*100,1)}%")
print(f"평균 온도: {round(temp_total/sens_count,1)}℃")
print(f"최고 온도 설비: {name_max} ({temp_max}℃)")
print(f"위험 설비 목록: {danger_name} ")
print("========================================")