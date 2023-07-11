list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d"]

list3 = list1 + list2
print(list3)
#[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']

for x in list2:
    list1.append(x)

print(list1)
#[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']
#루프문을 써서 저렇게 리스트2에 있는 인덱스들을 반복하면서 리스트1에 추가해줄 수 있음.

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 
#['a', 'b', 'c', 1, 2, 3]
#이게 제일 간단하기도? extend() 메소드 사용