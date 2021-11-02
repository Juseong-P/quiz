from random import *
#
# print("번호\t성적")
# print("="*20)
# score = 0
# total = 0
# for num in range(1, 31):
#     score = randint(0,100)
#     print(f"{num}\t{score}")
#     total += score
#
# print("="*20)
# print("총점\t%d" %total)
# print(f"평균\t{round(total/30,2)}")

print('숫자 맞추기 게임')
answer = randint(1,10)
chance = 0
while chance < 10:
    user = int(input('숫자를 맞춰보세요 : '))
    chance += 1
    if answer > user:
        print('답은 더 큰 숫자입니다.')
    elif answer < user:
        print('답은 더 작은 숫자입니다.')
    elif answer == user:
        print(f'축하합니다. {chance}회만에 정답을 맞췄습니다.')
        break

__author__ = 'Juseong Park'

# this is test for merge when the same part is modifed

# test test test
