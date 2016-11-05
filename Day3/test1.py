box = ['a','b','c','d','e']

if 'f' in box:
    print("f가 있습니다.")
else:
    print("f가 없습니다.")


a = 0
while a < 10:
    a = a + 1           # while문을 돌 때마다 a가 1씩 증가
    if(a % 2 == 0):     # a를 2로 나눈 나머지가 0이면
        continue        # 넘긴다.
    print(a)            # a를 2로 나눈 나머지가 0이 아니라면


marks = [190, 50, 60]
number = 0
for mark in marks:
    number = number + 1
    if(mark < 60):
        print("%d반 학생 분발하세요. 불합격입니다." % number)
        continue
    print("%d반 학생 축하합니다. 합격입니다." % number)
