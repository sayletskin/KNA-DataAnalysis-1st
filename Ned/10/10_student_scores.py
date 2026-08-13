# 학생들의 점수를 가져와서
# 각 학생별 합계와
# 모든 학생들의 평균 점수를 내는 코드
# 뭘 먼저 해야할까?
import os
import sys
import csv

# 0. 전체 미리 합산 점수 낼 준비를 한다(선택)
total_all = 0
students_count = 0
high_score = 0
low_score = 101
kor_total, eng_total, math_total = 0, 0, 0

# 1. 파일을 연다
file_path = os.path.join("data", "student_scores.csv")

# 1-2 파일이 있는지 확인
if not os.path.exists(file_path):
  print("거기에 파일이 없어!")
  sys.exit(1) # if문의 파일 없으면 출력 죽을게ㅇㅇ

# 2. 연 파일을 리스트 데이터로 뽑아낸다.
with open(file_path, "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)

  for row in reader:
    name = row.get("\ufeff이름", "(이름없음)")

    kor = int(row.get("국어", "0"))
    eng = int(row.get("영어", "0"))
    math = int(row.get("수학", "0"))
    total = round((kor + eng + math) / 3, 2)
    print(f"{name} | {kor} | {eng} | {math}, {total}")
    
    # 3. 점수 계산
    students_count += 1
    total_all += total 
    # [제출 안하는 실습5]
    # 5-1.
    if high_score < total:
      high_name = name
      high_score = total
    elif low_score > total:
      low_name = name
      low_score = total
    # 5-2.
    kor_total += kor
    eng_total += eng
    math_total += math

# 4. 새로 파일 만들어 저장하기 or 
# 결과를 화면에 출력(우리가 할거)
avg_all = round(total_all / students_count, 2)
print("=" * 20)

print(f"전체 평균 {avg_all}점")

print("=" * 20)

print(f"최고점 | {high_name} 학생 | {high_score}점") 
print(f"최저점 | {low_name} 학생 | {low_score}점")

print("=" * 20)

print(f"국어 평균 | {kor_total / students_count}점")
print(f"영어 평균 | {eng_total / students_count}점")
print(f"수학 평균 | {math_total / students_count}점")

# [제출 안하는 실습5]
# 5-1. 실행 끝날 때 과목별? 평균? 최고점 학생, 최저점 학생도 찾아 출력
# 5-2. 실행 끝날 때 각 과목별 평균도 출력 (선택)

# high_score = 0
# low_score = 101

# # 1. 실행 끝날 때 과목별? 평균? 최고점 학생, 최저점 학생도 찾아 출력
# with open(file_path, "r", encoding="utf-8") as f:
#   reader = csv.DictReader(f)

#   for row in reader:
#     name = row.get("\ufeff이름", "0")
#     kor = int(row.get("국어", "0"))
#     eng = int(row.get("영어", "0"))
#     math = int(row.get("수학", "0"))
#     total = round((kor + eng + math) / 3, 2) 
#     if high_score < total:
#       high_name = name
#       high_score = total
#     elif low_score > total:
#       low_name = name
#       low_score = total

# print(f"최고점인 {high_name} 학생은 {high_score}점 이다") 
# print(f"최저점인 {low_name} 학생은 {low_score}점 이다")

# print("=" * 20)

# # 2. 실행 끝날 때 각 과목별 평균도 출력 (선택)
# students_count = 0
# kor_total, eng_total, math_total = 0, 0, 0

# with open(file_path, "r", encoding="utf-8") as f:
#   reader = csv.DictReader(f)

#   for row in reader:
#     name = row.get("\ufeff이름", "0")
#     kor = int(row.get("국어", "0"))
#     eng = int(row.get("영어", "0"))
#     math = int(row.get("수학", "0"))
#     kor_total += kor
#     eng_total += eng
#     math_total += math
#     students_count += 1

# print(f"국어 평균 {kor_total / students_count}점")
# print(f"영어 평균 {eng_total / students_count}점")
# print(f"수학 평균 {math_total / students_count}점")
