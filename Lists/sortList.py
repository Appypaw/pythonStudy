thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']
#sort() 메소드는 정렬함.

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#[23, 50, 65, 82, 100]
#숫자도 잘 됨

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']
#내림차순은 sort(reverse = True) 붙이면 됨

def closest(n):
    return abs(n - 50)

numbers = [10,40,30,68,41,54]
thislist.sort(key = closest)
print(thislist)