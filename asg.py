import random 
import os
import time


life = 5
score = 0
combo = 0


while True:

    print("="*30)
    print("● "*life + "○ "*(5-life))
    print(f"{combo} COMBO")
    print(f"SCORE {score}")
    print("="*30)

    A = random.randint(1,9)
    B = random.randint(1,9)
    op = random.randint(1,2) 
    s200 = random.randint(1,5) 
    l2 = random.randint(1,7)

    if s200 == 1:
        print("이번문제 score +200")
        점수 = 200
    else:
        점수 = 100

    if l2 == 1:
        print("이번문제 life - 2")
        라이프 = 2
    else:
        라이프 = 1

    
    if op == 1:
        user = int(input(f"{A} + {B} = "))
        정답 = A + B
    elif op == 2:
        if A >= B:
            user = int(input(f"{A} - {B} = "))
            정답 = A - B
        else:
            user = int(input(f"{B} - {A} = "))
            정답 = B - A
    

    if user == 정답:
        print("맞았습니다.")
        score += 점수 + 20*combo
        combo += 1
    else:
        print("틀렸습니다.")
        combo = 0
        life -= 라이프   
        if life == 0:
            print("GAMEOVER")
            break
