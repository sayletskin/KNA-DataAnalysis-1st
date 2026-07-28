# """ """ - 여러 줄 문자열
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""

print(notice)
#
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
#
# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# 읽는 사람 > 협업자 > 나  

notice = """
설비 점검 안내
    1. 전원 확인
2. 센서 점검

"""

print(notice)
# """ """ 삼중 따옴표 사용 시 그 내부의 모든 줄바꿈이 다 반영되어 출력

# ================================================
# 이스케이프 문자

# notice 이스케이프 사용해서 개선
notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
print(notice)

tap = "이름\t상태"
print(tap, "이름 상태")

backslash = "이름\\상태"
print(backslash) # 이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

quotes = 'It\'s me' # 감싸는 따옴표와 str 내부 따옴표가 같을 때 \ 사용(하나만 적용)
print(quotes)

# 빈 문자열, 공백 문자열 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다면 "빈 문자열"
# "빈 문자열은" 글자 수 0, 길이 0
# " " 따옴표 안에 공백이 있는 경우는 "공백 문자열"
# 공백의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
print("" == "  ") # False

# ===============================
# 인덱싱 - 위치 번호로 글자 하나를 꺼내기
# 문자열[인덱스번호]
# 문자열의 첫 글자 번호 0, 뒤에서 부터는 -1

word = "PYTHON"
print(word[0], word[3], word[5])
# 문자열의 길이보다 긴 인덱스를 호출하면 index error가 뜸

# 자기 이름 출력
abc = "abcdefghijklmnopqrstuvwxyz" # jeong ryeol
print(abc[9] + abc[4] + abc[14] + abc[13] + abc[6] + " " + abc[17] + abc[24]
      + abc[4] + abc[14] + abc[11])

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1 부터 시작

# ==========================
print("=== 슬라이싱 ===")

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함되는데
# 끝 인덱스는 출력 안됨

print(word[3:7]) # HON
print(word[5]) # N
# 인덱싱은 정확하게 마지막 인덱스 까지만 쓸 수 있고, 넘치면 error
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 인덱스 6 이상 도 사용가능

print(word[:3]) # PYT
print(word[3:]) # HON
# 슬라이싱 start나 end를 비우면 처음부터나 끝까지 구간을 뽑아냄

# 슬라이싱 - 전체 생략
print(word[:]) # 시작부터 끝까지 뽑아냄

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:]) # HON
# 음수 인덱스 입력 시 그 인덱스부터 정방향 추출
print(word[:-1]) # PYTHO
# 처음부터 -1을 제외한 구간까지
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
# 문자열[시작:끝:간격(step)]
print(word[0:6:2]) # PTO  
# 시작부터 6까지 첫 문자부터 2 간격으로 추출

# start와 end를 생략하고 step을 쓰면 모든 문자열의 step 인덱스만큼 추출
print(word[::2]) # PTO

# ★순서 뒤집기
print(word[::-1]) # NOHTYP
# step은 인덱스가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# ==================================
# len() - 문자열의 길이 반환 
# len(문자열)

print("=== len() 활용 ===")

print(len("Hello World!")) # 12 (공백도 취급)
print(len("")) # 0 (빈 문자열은 0)

var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요!"
print(len(var)) # 36 (변수에 담긴 문자열 길이 출력 가능)

print(len("이것도") + len("가능할까?"))
# len() 은 int를 반환하기 때문에 계산 가능

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
print("abc"[len("abc") - 1]) # 할 수 있지만 실용적이지 않음

# =============================
print("=== in 활용 ===")

# in - 특정 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# 찾을문자열 in 문자열 (변수 치환 가능)
print("고장" in "설비 고장 발생")
# 찾을 문자열 "고장" 이 "설비 '고장' 발생"에 있어서 True
print("정상" in "설비 고장 발생") # False
print("설비에서 고장" in "설비 고장 발생") # False
print("설비에서 고장" in "설비에서 고장 발생") # True

# not in- in의 정반대 동작
print("고장"not in "설비 고장 발생") # False
print("정상"not in "설비 고장 발생") # True
print("설비에서 고장"not in "설비 고장 발생") # True
print("설비에서 고장"not in "설비에서 고장 발생") # False

print(" " in "설비 고장 발생") # True
# 따옴표로 감싼 공백은 정말 한 글자로 취급

print("=== count() ====")

# .count - 문자열에 특정 글자의 수(int)를 반환 .(점)붙이기 조심
# 문자열.count("찾을 글자")
print("banana".count("a")) # 3
print("010-1234-1234".count("-")) # 2
print("layla@spreatics.com".count("@")) # 1 
# 이메일에는 @가 포함되어있어서 in이나 count로 찾을 수 있음, 곧 find도 배우네

# =======================
print("=== find() ===")
# find - 전달받은 글자의 '첫 번째'로 나온 위치 인덱스 반환
# 찾는 글자가 없으면 -1
email = "hong@company.com"
at = email.find("@") # 4
user_id = email[:at] # hong
print(user_id) # hong > 이메일 @ 이용해서 아이디만 뽑아내기

# SQE-00Q8 이라는 설비의 SQE만 뽑아내기 (find(index)와 슬라이싱 사용)
sqe = "SQE-00Q8"
sqe_index = sqe.find("SQE")
print(sqe_index) # 0
sqe_index = sqe.find("-")
print(sqe_index) # 3
sqe_fin = sqe[:sqe_index] # sqe[0:3] -> "SQE"
print(sqe_fin)

# index를 써서 위 실습 다시하기
sqe_index = sqe.index("-")
sqe_fin = sqe[:sqe_index] # sqe[0:3] -> "SQE"
print(sqe_fin)

nick = "saylets kin"
nick_index = nick.index(" ")
nick_fin = nick[:nick_index]
print(nick_fin) # saylets

# =======================
# 특정 문자열의 위치(인덱스 번호)를 반환 (앞에서 나오는 가장 처음 나오는 인덱스 번호만 반환)
# 찾는 문자열이 없으면 오류
email = "layla@spreatics.com"
at = email.index("@") # 5
print(email[:at]) # layla (랄라)
print(email[at+1:]) # spreatics.com

# ========================
# 특정 문자열의 개수 세기
str1 = "a, b, c, d, e, a, a" 
# a개수를 세고싶으면
print(str1.count("a")) # 3
# 쉼표 개수 세기
print(str1.count(",")) # 6

str1 = "a, b, c, d, e,a, a"
print(str1.count(", ")) # 5 , count는 문자열이 완전히 동일해야함

#=======================
# startswith, endswith 특정 문자열로 시작/끝 나는지 검사 (bool형으로 반환)
nick = "sayletskin"
#saylets로 시작하는지 검사
nick_sta = "saylets"
print(nick.startswith(nick_sta)) # True
# 변수명은 ""따옴표 금지
nick_end = "kin"
print(nick.endswith(nick_end)) # True

str2 = "월요일 좋아, 정말로 최고야!"
print(str2.endswith("!")) # True
print(str2.endswith("야!")) # True
print(str2.endswith("요!")) # False
print(str2.endswith(" 월요일 좋아, 정말로 최고야! ")) # 띄어쓰기 공백이 있어 다르기 때문에 False

# ====================
print("=== 값은 객체다 ===")

print(type("절대로 잊어먹어버리지말기")) # str
# endswith와 len의 차이
# endswith는 .으로 연결
    # .으로 연결하는 도구들은 "메서드"
    # 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# len은 . 사용 안함
    # () -> 함수
    # len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장 함수"
"saylets".startswith("say")
## 123.startswith(1) # 오류
# .으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음

## print(len(123)) # int는 길이가 없다고 오류
# len 내장함수 길이를 정의하기 때문에 int형은 받지 않는다

# ==============
# 재할당 복습

num = 1
num = num + 1 # 2
num += 1 # 복합할당연산자 # 3

nick = "sayletskin"
print(nick.upper()) # "SAYLETSKIN"
nick = nick.upper()
print(nick)

# =========================
print("==== .upper() ====")

str3 = "abcdefg"
print(str3) # abcdefg

str3.upper # ABCDEFG > 반환은 대문자인데, 값에 재할당은 x
print(str3) # abcdefg > 기존 소문자 그대로

str3 = str3.upper() # 계속 대문자로 변환하려면 변수에 "재할당" / 최초 변수 "할당"은 불가능
print(str3) # ABCDEFG
# str4 = str4.upper()

# ==============
user_name = "kim chul soo"

print(user_name.capitalize()) # Kim chul soo
print(user_name.title()) # Kim Chul Soo

print("i'm full".title()) # I'M Full
print("i\'m full".title()) # I'M Full

# ===================
print(" ==== .strip() ====")

# 공백 제거
# .strip(): 앞과 뒤의 모든 공백 제거 (중간 띄어쓰기는 그대로 유지)
# .lstrip(): left(왼쪽) 공백만 제거
# .rstrip(): right(오른쪽) 공백만 제거

raw = "    ㅇㅅㅇ;;       "
print(raw.strip()) # "ㅇㅅㅇ;;"
print(raw.rstrip()) # "    ㅇㅅㅇ;;"
print("   ㅇ   ㅅ   ㅇ   ".strip()) # "ㅇ   ㅅ   ㅇ"
# 문자열의 가운데 공백은 strip으로 지울 수 없음

print(raw) # "    ㅇㅅㅇ;;       "
# strip()도 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("=")) # 정상
# 인자로 전달한 양 끝의 "="이 모두 지워짐

str5 = "=정상=========="
print(str5.strip("=")) # 정상
# 갯수 상관 없이 인자로 전달한 문자를 무조건 모두 삭제

print(str5.strip("= ")) # 정상 
# strip 자체가 공백을 지우는 것이기 때문에 
# 공백 상관없이 양 끝의 해당 문자열 삭제

str6 = "==정==상===="
print(str6.strip("=")) # 정==상
# 글자 중간에 있는 문자열은 건드리지 않음

# strip() 메서드에 인자로 들어가는 문자열은 완전히 동일하지 않아도 전부 삭제
str8 = " ab ㅇㅅㅇ cd  "
print(str8.strip("abcd "))

# =========================
print("=== 체이닝 ===")

raw = "         NORMAL           "

# 체이닝 X
step1 = raw.strip() # NORMAL
step2 = step1.lower() # normal

# 체이닝 X, 기존 변수의 재할당
raw = raw.strip() # NORMAL
raw = raw.lower() # normal

# 체이닝 O (선호1)
chain = raw.strip().lower() # normal

# 기존 변수에 재할당 가능 (선호2)
raw = raw.strip().lower() # normal

str7 = "     Warning     "
str7_low = str7.lower()
print("[" + str7_low + "]") # [     warning     ]
str7_chain = str7.lower().strip()
print("[" + str7_chain + "]") # [warning]

# ========================
print("=== replace() ===")

# 특정 문자열을 제거하거나 치환할 때 사용
# .replace("바꾸고 싶은 문자열","바꿀 문자열")
# 제거할 때는 인자의 두 번째를 ""(빈문자열)로 작성
text = " 정   상  가   동     "
print(text.replace(" ","")) # "정상가동"
print(text.replace("  ","")) # " 정 상가 동 "

# 글자 치환
print("고장".replace("고장", "fault")) # fault
print("고장".replace("고", "fault")) # fault장

# 단어 치환
str9 = "설비 정상 가동"
print(str9.replace("정상", "점검")) # "설비 점검 가동"

# replace() 체이닝 하는 법
num = "           010-1234-1234          "
print(num.replace(" ", "").replace("-", "")) # 01012341234

# ===============================
print("=== split() ===")
# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스프레소 아메리카노 카페라떼"
print(drinks.split()) # ['에스프레소', '아메리카노', '카페라떼']
# 띄어쓰기를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환

# 구분자를 특정하고 싶은 경우
fruits = "딸기,거봉,키위,사쿠란보"
print(fruits.split(",")) # ['딸기', '거봉', '키위', '사쿠란보']
# 문자열 콤마를 기준으로 분할

fruits2 = "딸기, 거봉, 키위, 사쿠란보"
print(fruits2.split(",")) # ['딸기', ' 거봉', ' 키위', ' 사쿠란보']
# 공백 그대로 유지
print(fruits2.split(", ")) # ['딸기', '거봉', '키위', '사쿠란보']
# ", " 공백 붙여서 정상화

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list)

# 거봉만 출력하기
# 출력하고자 하는 요소의 인덱스를 대괄호로 감싸서 호출
print(fruits_list[1]) # 거봉
print(fruits_list[3]) # 사쿠란보
print(fruits_list[-1]) # 사쿠란보

# split 횟수 제한
num = "010-1234-1234"
# ["010", "1234-1234"] 이렇게 하고 싶을 때
print(num.split("-", 1))
# text.split("구분자", 숫자) 숫자로 원하는 횟수만큼 앞에서 자를 수 있음

# ===============================
print("=== join() ===")
# 리스트를 하나의 문자열로 합침
# "구분자".join(리스트)  으로 구성
# 모든 요소가 합쳐져서 하나의 문자열로 반환

"-".join(fruits_list) # "딸기-거봉-키위-사쿠란보"
",".join(fruits_list) # "딸기,거봉,키위,사쿠란보"
", ".join(fruits_list) # "딸기, 거봉, 키위, 사쿠란보"

# 실습. pyThon 출력하기
print("=== 실습. pyThon 출력하기 ===")

word = "python"

# strip + capitalize(title)
print(word[:2] + word.strip("py").capitalize()) # pyThon

# replace 
print(word.replace("t","T")) # pyThon

# 슬라이싱, + T만 upper 사용
print(word[:2] + word[2].upper() + word[3:])

# 인덱싱으로 글자 하나씩 연결
print(word[0] + word[1] + word[2].upper() + word[3:])

#  split + join
print(word.split("t")) # ['py', 'hon']
print("T".join(word.split("t"))) # pyThon
print(word[2].upper().join(word.split("t"))) # pyThon

# =================================================
print("=== print 함수의 sep, end ===")

print("2026", "07", "27") # 2026 07 27 (기본적으로 ","는 공백이 들어감)

# sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
print("2026", "07", "27", sep="ㅇㅅㅇ") # 2026ㅇㅅㅇ07ㅇㅅㅇ27
# 공백 대신 sep 속성에 전달한 문자열이 삽입되어 이어짐

print("안녕", "하세") # 안녕 하세
print("안녕", "하세", end="요") # 안녕 하세요
# end 속성 사용 시 출력문 마지막에 해당 문자열이 붙어 삽입

# print("안녕", "하세", end="요", ㅎㅎ) # end 속성 뒤에 또 인자를

# print 함수 + 사용 시 sep과 end
print("안녕", "하세", end="요" + " 여러분") # 정상 동작 but 사용 자제

# 기본적으로 print문에는 sep으로 공백 한 칸,
# end로 \n(줄바꿈)이 적용되어 있음
# 근데, 개발자가 각 속성을 직접 부여할 경우
# 기본값이 아닌 전달받은 속성값을 사용
print("이런식으로 쓰죠?", "근데 안보이는 기본값이 있어요", sep=" ", end="\n")

# f-string
# 따옴표 밖에 f 작성
# 변수명은 꼭 {중괄호}에 감싸기
name, temp = "PUMP_A", 87
print(f"설비 {name}, 온도 {temp}도") # 설비 PUMP_A, 온도 87도 
print("설비 " + name + ", 온도 " + str(temp) + "도") # 설비 PUMP_A, 온도 87도 

# f-string 연산
hour = 8
# 우리는 하루에 8시간 수업을 듣고, 이는 480분 입니다.
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분 입니다.")

