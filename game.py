

def map():
    global current_position
    print(
        f" {current_position[0]}  |  {current_position[1]}  |  {current_position[2]}  ")
    print("------------")
    print(
        f" {current_position[3]}  |  {current_position[4]}  |  {current_position[5]}  ")
    print("------------")
    print(
        f" {current_position[6]}  |  {current_position[7]}  |  {current_position[8]}  \n")


position_user_1 = []
position_user_2 = []
current_position = ["", "", "", "", "", "", "", "", ""]
move_time = 0
user_turn = "X"
winner = ""

win_condition = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    [0, 4, 8],
    [2, 4, 6]
]

while True:
    map()
    if(winner == "X" or winner == "O"):
        print("User " + winner + " is Winner !")
        break
    
    move = int(input("User " + user_turn + " move : "))
    move_time += 1
    if move in position_user_1 or move in position_user_2 or move < 0 or move > 8 or move_time == 9:
        if move_time == 9:
            print("Tie !")
            break
        else:
            print("Invalid Move")
    else:
        current_position[move] = user_turn
        if user_turn == "X":
            position_user_1.append(move)
            user_turn = "O"
        elif user_turn == "O":
            position_user_2.append(move)
            user_turn = "X"

        for i in range(8):
            cnt1 = 0
            cnt2 = 0
            for k in range(len(position_user_1)):
                if(position_user_1[k] in win_condition[i]):
                    cnt1 = cnt1 + 1
                    if cnt1 == 3:
                        winner = "X"
            for k in range(len(position_user_2)):
                if(position_user_2[k] in win_condition[i]):
                    cnt2 = cnt2 + 1
                    if cnt2 == 3:
                        winner = "O"
