from collections import Counter
#Counter 요소는 딕셔너리의 키로 저장되고 갯수는 값으로 저장됨.

a = [1,1,1,3,4,5,6,7,8,8,9]
print(Counter(a))

#Counter({1: 3, 8: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 9: 1})
#Counter는 collections 모듈에 있음. 중복된 아이템이 몇 개 인지 알려줌.

def cnts(num_list):
    return Counter(num_list)

b = ["안녕", "안녕", "안녕해?", "안녕하십니까"]

print(cnts(b))
#Counter({'안녕': 2, '안녕해?': 1, '안녕하십니까': 1})
#함수로 만들어놓을수도 있음.