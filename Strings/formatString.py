'''
age = 36
txt = "제 이름은 준재준이고요, 저는 " + age + "살입니다."
print(txt)
'''

#안됨. 이런 식으로 문자열과 숫자를 합칠 수 없음.

#그래서 format() 메소드를 사용한다! 중괄호 {}를 이용해서 문자열 내에서 대체필드를 정의함.

age = 22
txt = "제 이름은 준재준이고요, 저는 {} 살입니다"
print(txt.format(age))

#제 이름은 준재준이고요, 저는 22 살입니다

total = 100
score = 99.8
grade = "A"

mine = "제 점수는 총점 {} 중에 {}점을 획득하여 {}를 받았습니다."
print(mine.format(total,score,grade))

#제 점수는 총점 100 중에 99.8점을 획득하여 A를 받았습니다.

total = 100
score = 99.8
grade = "A"

mine = "제 점수는 총점 {0} 중에 {1}점을 획득하여 {2}를 받았습니다."
print(mine.format(total,score,grade))

#제 점수는 총점 100 중에 99.8점을 획득하여 A를 받았습니다.
#배열은 0부터 시작