list = ["망고", "사과", "사람"]
print(list[1])
#사과

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#cherry
#-1은 리스트의 마지막 아이템 리턴함. -2는 리스트의 마지막에서 두번째 아이템 리턴함. -3는 그럼 세번째겠지?

manylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(manylist[2:5])
#['cherry', 'orange', 'kiwi']
#3번째에서 5번째 리스트만 내놓음. slicing이랑 비슷함.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#['apple', 'banana', 'cherry', 'orange']
#4번째 인덱스까지 올림. 근데 4번 인덱스는 "미포함!!"임.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#['cherry', 'orange', 'kiwi', 'melon', 'mango']
#2번째 인덱스부터 끝까지 올림. 근데 이건 또 포함임.. 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#['orange', 'kiwi', 'melon']
#"orange"(-4)부터 "mango"(-1)전까지. 망고는 미포함임..

cats = ["치즈태비", "고등어태비", "얼룩고양이"]
if "치즈태비" in cats:
  print("'치즈태비'는 고양이 리스트에 있습니다.") 
#'치즈태비'는 고양이 리스트에 있습니다.
#in 사용법.