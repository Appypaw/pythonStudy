def intro_func(country = "대한민국"):
    print("안녕하세요. 저는 " + country + "에서 왔습니다.")

intro_func("미국")
intro_func("중국")
intro_func("일본")
intro_func("캐나다")

"""
안녕하세요. 저는 미국에서 왔습니다.
안녕하세요. 저는 중국에서 왔습니다.
안녕하세요. 저는 일본에서 왔습니다.
안녕하세요. 저는 캐나다에서 왔습니다.
"""
#인자 없이 함수를 호출한다면, 이건 기본 값을 사용함. 기본 매개변수의 예시는 위와 같음.

def menus(food):
    for x in food:
        print(x)

Korean = ["김치", "불고기", "냉면"]
Japanese = ["초밥", "우동", "소바"]
French = ["감튀", "푸아그라"]

menus(Korean)
"""
김치
불고기
냉면
"""

def multi5(x):
    return x * 5

print(multi5(10))
#50
#return 도 사용 가능함.

