points_table_mine = {"X": 1, "Y": 2, "Z": 3}
points_table_opponent = {"A": 1, "B": 2, "C": 3}
game_values = {"rock": 1, "paper": 2, "scissors": 3}
game_score = 0

with open("test.txt") as data:
    for line in data:
        play = line.strip('\n').split(" ")
        opponent_hand = line[0]
        opponent_hand_score =  points_table_opponent[opponent_hand]
        me_hand = line[2]
        me_hand_score =  points_table_mine[me_hand]
        me_hand_score_throw = list(game_values.keys())[list(game_values.values()).index(me_hand_score)]
        opponent_hand_score_throw = list(game_values.keys())[list(game_values.values()).index(opponent_hand_score)]
        me_hand_score_throw_value = game_values.get(me_hand_score_throw)
        opponent_hand_score_throw_value = game_values.get(opponent_hand_score_throw)
        print(opponent_hand_score_throw_value)
        print(me_hand_score_throw_value)

        if me_hand_score_throw_value == 1 and opponent_hand_score_throw_value == 3:
             game_score += me_hand_score + 6
        elif opponent_hand_score_throw_value == 1 and me_hand_score_throw_value == 3:
            game_score += me_hand_score + 0
        elif opponent_hand_score_throw_value > me_hand_score_throw_value:
            game_score += me_hand_score + 0
        elif me_hand_score_throw_value > opponent_hand_score_throw_value:
            game_score += me_hand_score + 6
        elif me_hand_score_throw_value == opponent_hand_score_throw_value:
            game_score += me_hand_score + 3

print(f"Total_score_i: {game_score}") 




        