import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("플레이어 수를 입력하세요. (2-4명): ")
    if players.isdigit():
        players = int(players)
        if players < 4 or players > 2
            break
        else:
            print("1~4명의 숫자를 입력해주세요.")
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요.")

print(players, "명의 플레이어가 플레이합니다.")

max_score = 50
player_scores = [0 for _ in range(players)]         #0으로 채워진 players만큼의 리스트 생성을 반복함. 10 for _ in range(players)하면 10으로 아이템 채움.

while max(player_scores) < max_score:

    current_score = 0

    should_roll = input ("주사위를 던지시겠습니까? (y)?")
    if should_roll.lower() == "y":
        break
    
    value = roll()

    print(value, "가 나왔습니다. 차례가 끝났습니다.")
    value = current_score + value

#마저 짜기