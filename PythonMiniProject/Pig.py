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
        if players < 4 or players > 2:
            break
        else:
            print("1~4명의 숫자를 입력해주세요.")
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요.")

print(players, "명의 플레이어가 플레이합니다.")

max_score = 50
player_scores = [0 for _ in range(players)]         #0으로 채워진 players만큼의 리스트 생성을 반복함. 10 for _ in range(players)하면 10으로 아이템 채움.

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "턴이 시작됐습니다!\n")
        current_score = 0

        while True:
            should_roll = input ("주사위를 던지시겠습니까? (y)?")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("1이 나왔습니다! 턴 종료")
                current_score = 0
                break
            else:
                current_score = current_score + value
                print(value, "이(가) 나왔습니다.")

            print("당신의 점수는 : ", current_score)
        
        player_scores[player_idx] += current_score
        print("당신의 총 점수는:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(winning_idx + 1, "번 플레이어가", player_scores[player_idx], "로 승리하였습니다.")