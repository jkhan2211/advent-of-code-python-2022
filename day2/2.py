game_result = {"X": 1, "Y": 2, "Z": 3}
points_table_opponent = {"A": 1, "B": 2, "C": 3}
user_values = {"rock": 1, "paper": 2, "scissors": 3}
game_score = 0
tracker = []
# x -lose
# y -draw
# z - win

with open("test.txt") as data:
    for line in data:
        play = line.strip('\n').split(" ")
        print(play)
        opponent_hand = line[0]
        opponent_hand_score =  points_table_opponent[opponent_hand]
        game_result_point = line[2]
        game_result_point_score =  game_result[game_result_point]
        
        if opponent_hand_score == 3 and game_result_point_score == 1:
            get_user_value = user_values.get("paper")
            game_score = get_user_value + 0
            tracker.append(game_score)

        elif opponent_hand_score == 2 and game_result_point_score == 1:
            get_user_value = user_values.get("rock")
            game_score = get_user_value + 0
            tracker.append(game_score)

        elif opponent_hand_score == 1 and game_result_point_score == 1:
            get_user_value = user_values.get("scissors")
            game_score = get_user_value + 0
            tracker.append(game_score)

        elif opponent_hand_score == 3 and game_result_point_score == 2:
            get_user_value = user_values.get("scissors")
            game_score = get_user_value + 3
            tracker.append(game_score)

        elif opponent_hand_score == 2 and game_result_point_score == 2:
            get_user_value = user_values.get("paper")
            game_score = get_user_value + 3
            tracker.append(game_score)

        elif opponent_hand_score == 1 and game_result_point_score == 2:
            get_user_value = user_values.get("rock")
            game_score = get_user_value + 3
            tracker.append(game_score)
        elif opponent_hand_score == 3 and game_result_point_score == 3:
            get_user_value = user_values.get("rock")
            game_score = get_user_value + 6
            tracker.append(game_score)
        elif opponent_hand_score == 2 and game_result_point_score == 3:
            get_user_value = user_values.get("scissors")
            game_score = get_user_value + 6
            print(f"final: {game_score}")
            tracker.append(game_score)

        elif opponent_hand_score == 1 and game_result_point_score == 3:
            get_user_value = user_values.get("paper")
            game_score = get_user_value + 6
            print(f"final: {game_score}")
            tracker.append(game_score)



print(tracker)
print(sum(tracker))
        