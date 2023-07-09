thislist = ["apple", "banana", "cherry"]
thislist[1] = "bonbon"
print(thislist)
#['apple', 'bonbon', 'cherry']
#1번 인덱스를 bonbon으로 바꿨음.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["bonbon", "cola"]
print(thislist)
#['apple', 'bonbon', 'cola', 'orange', 'kiwi', 'mango']
#1번부터 3번 인덱스까지(단 3번은 포함하지 않음) bonbon, cola로 바꿈.

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["bonbon", "cola"]
print(thislist)
#['apple', 'bonbon', 'cola', 'cherry']
#1번부터 2번 인덱스(2번 인덱스는 미포함)까지 단 하나의 아이템인데 그보다 더 많은 수를 넣을 경우 그냥 리스트 안에 있는 아이템의 총 갯수를 늘림.

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["cat"]
print(thislist) 
#['apple', 'cat']
#2개의 아이템을 하나의 아이템으로 교체하면 수를 줄여버림.

thislist = ["apple", "banana", "cherry"]
thislist.insert(3, "cat")
print(thislist)
#['apple', 'banana', 'cherry', 'watermelon']
#insert()메소드를 사용해서 올릴 수 있음. insert(인덱스번호, 넣을 아이템)
