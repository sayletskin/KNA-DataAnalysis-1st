# 실습 1. 첫 함수 만들고 호출하기
def start_checking():
    print("점검을 시작합니다")

start_checking()
start_checking()

# 실습 2. 모범답안
def start_check():
   print("점검을 시작합니다")
   print("안전 장비를 확인하세요")
   print("기록을 준비하세요")

start_check() # 압축기A
start_check() # 펌프1

# 실습 4. 함수 설비 점검 자동화하기
# ①구분선을출력하는함수를정의
# ②점검안내여러줄을출력하는함수를정의
# ③두함수를설비마다순서대로호출
# ④실행해각설비마다같은안내가반복되는지확인

def print_line():
    print("-" * 20)

def check_guide():
    print("점검 안내 출력 시작")
    print("점검 안내 출력 종료")

# 장비1에 대한 함수 호출
print_line()
check_guide()

# 장비2에 대한 함수 호출
print_line()
check_guide()

# 실습2. 다중매개변수로센서값계산하기
# 매개변수두세개를가진함수로센서데이터를처리하기
# 단계
# ①def 괄호안에매개변수두개를쉼표로정의
# ②함수안에서두매개변수를함께활용
# ③인자두개를순서대로전달해호출
# ④인자순서를바꾸면결과가어떻게달라지는지확인

#실습4. 반환값으로간단계산기만들기
#print가아니라return으로결과를돌려주고변수에담기
#단계
#①값을받아계산하는함수를정의
#②계산결과를print가아니라return으로돌려주기
#③호출결과를변수에담기
#④담은값을다음계산·출력에이어쓰기
#예상 결과
#85.0
#90.0 (담은값을이어씀)

#def calc_num(a, b, c):
#    return round(( a + b ) / c, 2)

#print(calc_num(c = 12, a = 121, ))

#실습5. 센서통계함수만들기
#목록을받아여러통계를한번에돌려주고언패킹으로나눠받기
#단계
#①센서값목록을매개변수로받는함수를정의
#②min·max·합÷개수로최소·최대·평균을계산
#③세값을쉼표로함께return
#④돌려받은값을세변수로언패킹해출력#
#예상 결과
#78 92 85.0
#64

# 지금까지 배운 내용을 활용해서
# 재미?있는 함수? 만들기 예제
import random

groups = ["에스파", "하트2하트", "리센느", "태연", "엔믹스"]

# 랜덤 뽑기!!!!!
my_group = random.choice(groups)
print(my_group)


def get_random_group():
    groups = [
    {
        "이름": "에스파",
        "리더": "카리나"
    },
    {
        "이름": "엔믹스",
        "리더": "해원"
    },
    {
        "이름": "리센느",
        "리더": "원희"
    }
]
    my_group = random.choice(groups)
    return my_group.get("이름"), my_group.get("리더")

group_name, group_leader = get_random_group()
print(group_name, group_leader)

# 가봤거나, 가보고싶은 여행지 정보 (최소 5개 이상)
# 함수를 호출하면 랜덤으로 해당 여행지의 국가이름과 수도
# "환영합니다! 000 나라의 수도 000 입니다!" 출력 

# country = [ "일본", "미국", "중국", "스위스", "이탈리아"]

def get_random_country():
    country = [
        {
            "국가": "일본",
            "수도": "도쿄"
        },
        {
            "국가": "미국",
            "수도": "워싱턴"
        },
        {
            "국가": "중국",
            "수도": "베이징"
        },
        {
            "국가": "스위스",
            "수도": "베른"
        },
        {
            "국가": "이탈리아",
            "수도": "로마"
        }
    ]
    my_country = random.choice(country)
    return my_country.get("국가"), my_country.get("수도")

# "환영합니다! 000 나라의 수도 000 입니다!" 출력 
country_name, country_capital = get_random_country()
print(f"환영합니다! {country_name} 나라의 수도 {country_capital} 입니다!")

def get_random_chara():
    chara = [
        {
            "name": "eli",
            "ski" : "mega"
        },
        {
            "name": "lir",
            "ski" : "metal"
        },
        {
            "name": "arme",
            "ski" : "stone"
        }
    ]    
    random_chara = random.choice(chara)
    return random_chara.get("name"), random_chara.get("ski")
chara_name, chara_ski = get_random_chara()
print(chara_name, chara_ski)

# 선택실습 5. 센서 통계 함수 만들기
# 1) 센서값 목록을 매개변수로 받는 함수를 정의
# 2) min,max, min-max평균 계산
# 3) 세 값을 쉼표로 함께 return
sensors = [ 78, 79, 91, 92]

def calc_min_max(value):
    minimum = min(value)
    maximum = max(value)
    return minimum, maximum, round((minimum + maximum) / 2, 1)

# 4) 돌려받은 값을 세 변수로 언패킹해 출력
result = calc_min_max(sensors)
print(result) # (78, 92, 85.0) 튜플


