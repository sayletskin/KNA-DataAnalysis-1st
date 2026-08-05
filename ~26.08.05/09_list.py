# list는 python의 자료형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

temps = [35, 36, 37, 38] # int 리스트
float_temps = [36.4, 36.5, 36.6, 36.7] # float 리스트
machines = ["펌프", "압축기", "모터"] # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(temps[2]) # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고싶다면?
print(temps[-1]) # 38 > [-1] 가장 마지막 요소 출력

# 빈 리스트
empty = []

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용
print(len(temps)) # 4 
print(len(empty)) # 0

# 리스트의 담긴 값의 갯수 변수에 저장
temps_length = len(temps) # 변수에 4라는 값이 할당
print(temps_length) # 4 

# 실습
t = [35, 35, 34, 33, 32, 33]
print(t) # [35, 35, 34, 33, 32, 33]
print(len(t)) # 6
print(t[-1]) # 33
zero = []
print(len(zero)) # 0

# 리스트의 인덱스
print(temps[0], temps[-1]) # 가장 첫 번째, 가장 마지막 요소
# -1 을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이-1 로 계산잉 가능하지만
# 이 작업이 번거로워 -1 을 가장 많이 사용

# 없는 인덱스 호출
# temps 리스트는 길이가 5
## print(temps[5]) # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

# 실습 64
p = [120, 135, 150, 175, 190, 200]
pf, pl = p[0], p[-1]
print(pf + pl,(pf + pl) / 2) # 320 160.0

# 리스트의 자료형
print(f"temps: {temps}") # temps: [35, 36, 37, 38]
print(f"type(temps): {type(temps)}") # type(temps): <class 'list'>
print(f"type(temps[0]): {type(temps[0])}") # type(temps[0]): <class 'int'>

# 다른 자료형의 값이 들어있는 리스트의 요소 타입
# float 값이 들어잇는 float_temps 리스틍의 0번째 요소
print(type(float_temps[0])) # <class 'float'>
print(type(machines[0])) # <class 'str'>

# 리스트 슬라이싱
# 리스트[시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능 (문자열과 동일)

# temps = [35, 36, 37, 38]
print(temps[1:3]) # [36, 37]
print(temps[1:2]) # [36]
print(temps[:2]) # [35, 36]
print(temps[:2], temps[3:]) # [35, 36] [38]
print(temps[::1]) # [35, 36, 37, 38]
print(temps[::3]) # [35, 38]
print(temps[100:999]) # [] -> 슬라이싱은 없는 인덱스를 넣으면 빈 값을 반환

# 인덱싱 vs 슬라이싱

# 인덱싱 temps[0]은 값 하나 (35)
# temps[999]와 같이 없는 인덱스 사용 시 에러

# 슬라이싱 temps[0:2]은 리스트 ([35, 36])
# 슬라이싱은 영역을 잘라내는 역할이기 때문에 리스트를 반환하는 것
# temps[100:999]) 에러 발생하지 않음
# 슬라이싱은 '있는 만큼만' 잘라주기 때문에 에러 발생하지 않음

# 실습 4
t = [20, 20, 21, 21, 22, 23, 24, 26, 25, 23]
print(t[:3]) # [20, 20, 21]
print(t[-3:]) # [26, 25, 23]
print(len(t[:3]), len(t[-3:])) # 3 3
# 실습 5
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12]
first = l[:6]
print(first) # [1, 2, 3, 4, 5, 6]
second = l[-6:]
print(second) # [7, 8, 9, 0, 11, 12]
print(len(first), len(second)) # 6 6

# 인덱스로 특정 값 바꾸기 > 문자열과 다름
# temps = [35, 36, 37, 38]

print("원본:", temps)
temps[2] = 999
print("2번 인덱스 값 변경 결과:", temps)

# in (존재 확인)
# machines = ["펌프", "압축기", "모터"]
print("펌프" in machines) # True
print("펌프" not in machines) # False
print("프레스" in machines) # False

# 특정 값의 인덱스 찾기
i = machines.index("압축기")
print(i) # 1

# .index() 메서드는 리스트엣 가장 처음 등장하는 인덱스만 반환
machines2 = ["펌프", "압축기", "모터", "압축기"]

i2= machines.index("압축기") # 1

# 실습 6
t = [20, 20, 21, 21, 22, 23, 240, 26, 25, 23]
print(240 in t) # True
i = t.index(240) # 6
t[i] = 24
print(t) # [20, 20, 21, 21, 22, 23, 24, 26, 25, 23]
print(240 in t) # False

# 리스트 값 추가
# .append(추가할값)
# 리스트의 가장 마지막에 값을 추가
# 리스트 원본이 수정 (재할당 필요 X)
nums = [1, 2, 3, 4, 5]

nums.append(999)
print(nums) # [1, 2, 3, 4, 5, 999]

# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면
# 원본 리스트를 복사해서 리스트 수정 진행
# nums = [1, 2, 3, 4, 5, 999] > 기존 리스트는 원본으로 둠
new_nums = nums # 스스로의 메모리를 할당받지 않고, 메모리 주소만 복사
print(new_nums) # [1, 2, 3, 4, 5, 999]

new_nums.append(111)
print(f"원본 nums 리스트: {nums}")
# 예상 : [1, 2, 3, 4, 5, 999]
# 실제 : [1, 2, 3, 4, 5, 999, 111]
# 복사한 메모리 주소에 append를 했기 때문엥 원본까지 영향을 받음

# 이를 해결하기 위해서 .copy()라는 메서드를 사용
# new_nums2라는 새로운 메모리에 nums 배열을 새로 저장
new_nums2 = nums.copy()
new_nums2.append(222) # nums 배열에 영향을 미치지 않고 사용
print(f"원본 nums 리스트: {nums}")
print(f"복사본 new_nums에 111 append 결과: {new_nums}")

# .insert(위치, 값)
# 리스트에서 원하는 위치에 값을 삽입
# 원본 배열에 바로 삽입
# 기존 배열에서 삭제는 되지 않고, 해당하는 인덱스 값이 삽입(뒤에 요소는 밀려남)
nums.insert(3, 333)
print(nums) # [1, 2, 3, 333, 4, 5, 999, 111]

# extend()
# 리스트 연결
# 다른 리스트의 값들을 "풀어서" 이어붙임
data = [1, 2, 3]
new_data = [7, 8, 9]
data.extend(new_data)
print(data)

print(data.extend(new_data)) 
# 기대 [1, 2, 3, 7, 8, 9] 실제 None
# extend() 메서드는 data라는 리스트를 "수정" 이를 반환하지 않음
# 반환값이 없어서 print를 할 값이 없는 것
### data 라는 리스트를 new_data에 붙여주기만 하고 반환은 안해줘서 None
print(data) # [1, 2, 3, 7, 8, 9]

# 실습 7
a = []
a.append(7) # [7]
a.insert(0, 3) # [3, 7]
a.extend([11, 15]) # [3, 7, 11, 15]
print(a) # [3, 7, 11, 15]


# 정리
# 오늘 꼭 알아야 하는 리스트 수정 메서드와 개념
# .append(추가할 값): 리스트의 가장 마지막 값을 추가
# .insert(위치, 값): 첫 번째 인자인 위치 인덱스에 값을 삽입
# .extend(합칠리스트): 두 리스트를 하나의 리스트로 합체

# ===================================

# 리스트에서 요소 삭제
# .remove(값) : 위치는 모르고 삭제할 "값"만 알때 사용하는 요소 삭제 메서드
list1 = ["딸기", "사과", "배", "포도", "수박", "망고"]
list1.remove("수박")
print(list1) # ['딸기', '사과', '배', '포도', '망고']

# .pop(인덱스) : 인덱스로 특정 요소를 삭제할 때 사용
#삭제한 인덱스의 값을 반환
list1.pop(0)
print(list1) # ['사과', '배', '포도', '망고']
print(list1.pop(2)) # 포도 / 삭제한 인덱스 2번의 값인 포도 출력(반환O)
print(list1) # ['사과', '배', '망고']

# del: 인덱스로 리스트의 요소 삭제 (슬라이싱으로 영역 삭제 가능)
del list1[0]
print(list1) # ['배', '망고']

del list1[:] # 처음부터 끝까지 삭제
print(list1) # [] > 빈 리스트가 됨

# del 건너뛰기
list2 = ["빨강", "노랑", "초록", "파랑", "남색", "보라"]
del list2[::2] # 빨, 초 , 남 을 삭제하겠다는 의미
print(list2) # ['노랑', '파랑', '보라']

# 실습
b = [30, 40, 999, 50, 60, 70]
b.remove(999) 
print(b) # [30, 40, 50, 60, 70]
print(b.pop(2)) # 50
del b[0]
print(b) # [40, 60, 70]

# 리스트 정렬하기
# 리스트.sort()
# 데이터를 정렬하는 친구
# 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# 내림차순으로 정렬하고 싶은 경우 .sort(reverse=True)

n = [37, 2, 8, 109, 1004, -1, 22]
print('n 리스트 원본:', n)

# 오름차순 정렬
n.sort() # 원본 리스트 수정
print('n 리스트 오름차순 정렬 결과:', n)

# 내림차순 정렬
n.sort(reverse=True)
print('n 리스트 내림차순 정렬 결과:', n)

n = [37, 2, 8, 109, 1004, -1, 22]
print('n 리스트 원본:', n)
# 리스트 순서 뒤집기
# .reverse()
# 값의 크기로 정렬은 해주지 않음
# 뒤로 계속 쌓인 결과(최신)를 앞에서부터 보고싶을 때 사용
n.reverse()
print('n 리스트 뒤집기 결과:', n)

# 리스트 안 값의 갯수 구하기
# .count(찾을값)

f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
print(f.count("일회용컵")) # 3
print(f) # 원본에 변화 없음

# 특정 값의 위치 찾기
# .index(위치를찾을값)
# 리스트에서 가장 처음 위치만 찾아줌
print(f.index("일회용컵")) # 1
print(f) # 원본 변화 x

# 실습 9
temps = [15, 17, 23, 32, 21]
temps.sort() 
print(temps) # [15, 17, 21, 23, 32] 
temps.reverse() 
print(temps) # [32, 23, 21, 17, 15]
print(temps.count(32), temps.index(32)) # 1 0

