myset = {"apple", "banana", "cherry"}
#세트란 무엇인가? 세트는 순서가 없고 변경 불가능하며 인덱스화되지 않은 집합을 말함.
#근데 아이템을 지우거나 추가할 순 있음.

thisset = {"apple", "banana", "cherry"}
print(thisset) 
#{'cherry', 'apple', 'banana'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#{'cherry', 'banana', 'apple'}
#중복된 아이템은 걍 씹어버림

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{'banana', True, 2, 'apple', 'cherry'}
#True와 1은 같은 것으로 취급함.

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#3
