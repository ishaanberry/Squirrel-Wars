import copy
import sys


def find_attack_type(final_i, final_j, board_state, player1):
    if final_i == 0:
        if final_j == 0:
            if board_state[final_i][final_j+1] == player1["symbol"] or board_state[final_i+1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
        elif final_j == 4:
            if board_state[final_i][final_j-1] == player1["symbol"] or board_state[final_i+1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
        else:
            if board_state[final_i][final_j-1] == player1["symbol"] or board_state[final_i+1][final_j] == player1["symbol"] or board_state[final_i][final_j+1] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
    elif final_i == 4:
        if final_j == 0:
            if board_state[final_i][final_j+1] == player1["symbol"] or board_state[final_i-1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
        elif final_j == 4:
            if board_state[final_i][final_j-1] == player1["symbol"] or board_state[final_i-1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
        else:
            if board_state[final_i][final_j-1] == player1["symbol"] or board_state[final_i-1][final_j] == player1["symbol"] or board_state[final_i][final_j+1] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
    else:
        if final_j == 0:
            if board_state[final_i][final_j+1] == player1["symbol"] or board_state[final_i-1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
        elif final_j == 4:
            if board_state[final_i][final_j-1] == player1["symbol"] or board_state[final_i-1][final_j] == player1["symbol"] or board_state[final_i+1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
        else:
            if board_state[final_i][final_j-1] == player1["symbol"] or board_state[final_i-1][final_j] == player1["symbol"] or board_state[final_i][final_j+1] == player1["symbol"] or board_state[final_i+1][final_j] == player1["symbol"]:
                attack_type = "Raid"
            else:
                attack_type = "Sneak"
    return attack_type


def sneak_attack(player, board_state, board_values, final_i, final_j):
    player["score"] += int(board_values[final_i][final_j])
    board_state[final_i][final_j] = player["symbol"]
    return


def raid_attack(player1, player2, board_state, board_values, final_i, final_j):
    player1["score"] += int(board_values[final_i][final_j])
    board_state[final_i][final_j] = player1["symbol"]
    if final_i == 0:
        if final_j == 0:
            if board_state[final_i][final_j+1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j+1])
                player2["score"] -= int(board_values[final_i][final_j+1])
                board_state[final_i][final_j+1] = player1["symbol"]

            if board_state[final_i+1][final_j] == player2["symbol"]:
                player1["score"] += int(board_values[final_i+1][final_j])
                board_state[final_i+1][final_j] = player1["symbol"]
                player2["score"] -= int(board_values[final_i+1][final_j])
        elif final_j == 4:
            if board_state[final_i][final_j-1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j-1])
                player2["score"] -= int(board_values[final_i][final_j-1])
                board_state[final_i][final_j-1] = player1["symbol"]

            if board_state[final_i+1][final_j] == player2["symbol"]:
                player1["score"] += int(board_values[final_i+1][final_j])
                board_state[final_i+1][final_j] = player1["symbol"]
                player2["score"] -= int(board_values[final_i+1][final_j])

        else:
            if board_state[final_i][final_j-1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j-1])
                player2["score"] -= int(board_values[final_i][final_j-1])
                board_state[final_i][final_j-1] = player1["symbol"]

            if board_state[final_i+1][final_j] == player2["symbol"]:
                player1["score"] += int(board_values[final_i+1][final_j])
                board_state[final_i+1][final_j] = player1["symbol"]
                player2["score"] -= int(board_values[final_i+1][final_j])

            if board_state[final_i][final_j+1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j+1])
                player2["score"] -= int(board_values[final_i][final_j+1])
                board_state[final_i][final_j+1] = player1["symbol"]

    elif final_i == 4:
        if board_state[final_i-1][final_j] == player2["symbol"]:
                player1["score"] += int(board_values[final_i-1][final_j])
                board_state[final_i-1][final_j] = player1["symbol"]
                player2["score"] -= int(board_values[final_i-1][final_j])
        if final_j == 0:
            if board_state[final_i][final_j+1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j+1])
                player2["score"] -= int(board_values[final_i][final_j+1])
                board_state[final_i][final_j+1] = player1["symbol"]
        elif final_j == 4:
            if board_state[final_i][final_j-1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j-1])
                player2["score"] -= int(board_values[final_i][final_j-1])
                board_state[final_i][final_j-1] = player1["symbol"]
        else:
            if board_state[final_i][final_j-1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j-1])
                player2["score"] -= int(board_values[final_i][final_j-1])
                board_state[final_i][final_j-1] = player1["symbol"]

            if board_state[final_i][final_j+1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j+1])
                player2["score"] -= int(board_values[final_i][final_j+1])
                board_state[final_i][final_j+1] = player1["symbol"]

    else:
        if board_state[final_i+1][final_j] == player2["symbol"]:
            player1["score"] += int(board_values[final_i+1][final_j])
            board_state[final_i+1][final_j] = player1["symbol"]
            player2["score"] -= int(board_values[final_i+1][final_j])
        if board_state[final_i-1][final_j] == player2["symbol"]:
            player1["score"] += int(board_values[final_i-1][final_j])
            board_state[final_i-1][final_j] = player1["symbol"]
            player2["score"] -= int(board_values[final_i-1][final_j])
        if final_j == 0:
            if board_state[final_i][final_j+1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j+1])
                player2["score"] -= int(board_values[final_i][final_j+1])
                board_state[final_i][final_j+1] = player1["symbol"]

        elif final_j == 4:
            if board_state[final_i][final_j-1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j-1])
                player2["score"] -= int(board_values[final_i][final_j-1])
                board_state[final_i][final_j-1] = player1["symbol"]

        else:
            if board_state[final_i][final_j-1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j-1])
                player2["score"] -= int(board_values[final_i][final_j-1])
                board_state[final_i][final_j-1] = player1["symbol"]

            if board_state[final_i][final_j+1] == player2["symbol"]:
                player1["score"] += int(board_values[final_i][final_j+1])
                player2["score"] -= int(board_values[final_i][final_j+1])
                board_state[final_i][final_j+1] = player1["symbol"]
    return


def calculate_eval_func(player1, player2, board_state, board_values):
    eval_func_list = []
    temp_board_state = copy.deepcopy(board_state)
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)
    for i in range(0, 5):
        eval_func_list.append([])
        for j in range(0, 5):
            if temp_board_state[i][j] == "*":
                attack_type = find_attack_type(i, j, temp_board_state, player1)
                if attack_type == "Raid":
                    raid_attack(temp_player1, temp_player2, temp_board_state, board_values, i, j)
                else:
                    sneak_attack(temp_player1, temp_board_state, board_values, i, j)
                eval_func_list[i].append(temp_player1["score"] - temp_player2["score"])
            else:
                eval_func_list[i].append(-9999)
            temp_board_state = copy.deepcopy(board_state)
            temp_player1 = copy.deepcopy(player1)
            temp_player2 = copy.deepcopy(player2)
    return eval_func_list


def greedy(player1, player2, board_state, board_values):
    eval_func_list = calculate_eval_func(player1, player2, board_state, board_values)
    possible_i = []
    possible_j = []
    max_eval = -10000
    for i in range(0, 5):
        for j in range(0, 5):
            if max_eval < eval_func_list[i][j]:
                max_eval = eval_func_list[i][j]
    if max_eval == -9999:
        print "Game Over"
        if player1["score"] > player2["score"]:
            print player1["symbol"] + " wins!"
        elif player1["score"] < player2["score"]:
            print player2["symbol"] + " wins!"
        else:
            print "Its a tie!!"
    else:
        for i in range(0, 5):
            for j in range(0, 5):
                if max_eval == eval_func_list[i][j]:
                    possible_i.append(i)
                    possible_j.append(j)
        final_ij = tie_breaker(possible_i, possible_j)
    return final_ij


def minimax(player1, player2, board_state, board_values, cutoff_depth):
    depth = 0
    possible_i = []
    possible_j = []
    traverse = open("traverse_log.txt", "w")

    eval_func_list = calculate_eval_func(player1, player2, board_state, board_values)
    if depth < cutoff_depth:
        max_eval = max_func(player1, player2, board_state, board_values, cutoff_depth, depth, eval_func_list, traverse, -1, -1)
    for i in range(0, 5):
        for j in range(0, 5):
            if max_eval == eval_func_list[i][j]:
                possible_i.append(i)
                possible_j.append(j)
        final_ij = tie_breaker(possible_i, possible_j)
    traverse.close()
    return final_ij


def max_func(player1, player2, board_state, board_values, cutoff_depth, depth, eval_func_list, traverse, xi, xj):
    root = -9998
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)
    temp_board_state = copy.deepcopy(board_state)

    depth += 1
    if depth == cutoff_depth:
        for i in range(0, 5):
            for j in range(0, 5):
                if eval_func_list[i][j] != -9999:
                    if root < eval_func_list[i][j]:
                        root = eval_func_list[i][j]
    else:
        for i in range(0, 5):
            for j in range(0, 5):
                if board_state[i][j] == "*":
                    attack_type = find_attack_type(i, j, board_state, player1)
                    if attack_type == "Raid":
                        raid_attack(temp_player1, temp_player2, temp_board_state, board_values, i, j)
                    else:
                        sneak_attack(temp_player1, temp_board_state, board_values, i, j)
                    temp = min_func(temp_player1, temp_player2, temp_board_state, board_values, cutoff_depth, depth, traverse, i, j)
                    eval_func_list[i][j] = temp

                    temp_board_state = copy.deepcopy(board_state)
                    temp_player1 = copy.deepcopy(player1)
                    temp_player2 = copy.deepcopy(player2)
                if eval_func_list[i][j] != -9999:
                    if root < eval_func_list[i][j]:
                        root = eval_func_list[i][j]
    return root


def min_func(player1, player2, board_state, board_values, cutoff_depth, depth, traverse, xi, xj):
    depth += 1
    root = 9999
    eval_list = []
    temp_board_state = copy.deepcopy(board_state)
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)
    if depth == cutoff_depth:
        for i in range(0, 5):
            eval_list.append([])
            for j in range(0, 5):
                if temp_board_state[i][j] == "*":
                    attack_type = find_attack_type(i, j, temp_board_state, temp_player2)
                    if attack_type == "Raid":
                        raid_attack(temp_player2, temp_player1, temp_board_state, board_values, i, j)
                    else:
                        sneak_attack(temp_player2, temp_board_state, board_values, i, j)
                    eval_list[i].append(cal_eval(temp_player1, temp_player2))

                else:
                    eval_list[i].append(-9999)

                temp_board_state = copy.deepcopy(board_state)
                temp_player1 = copy.deepcopy(player1)
                temp_player2 = copy.deepcopy(player2)
                if eval_list[i][j] != -9999:
                    if root > eval_list[i][j]:
                        root = eval_list[i][j]
    else:
        for i in range(0, 5):
            eval_list.append([])
            for j in range(0, 5):
                if temp_board_state[i][j] == "*":
                    attack_type = find_attack_type(i, j, temp_board_state, temp_player2)
                    if attack_type == "Raid":
                        raid_attack(temp_player2, temp_player1, temp_board_state, board_values, i, j)
                    else:
                        sneak_attack(temp_player2, temp_board_state, board_values, i, j)
                    eval_func_list = calculate_eval_func(temp_player1, temp_player2, temp_board_state, board_values)
                    eval_list[i].append(max_func(temp_player1, temp_player2, temp_board_state, board_values, cutoff_depth, depth, eval_func_list, traverse, i, j))

                else:
                    eval_list[i].append(-9999)
                temp_board_state = copy.deepcopy(board_state)
                temp_player1 = copy.deepcopy(player1)
                temp_player2 = copy.deepcopy(player2)
                if eval_list[i][j] != -9999:
                    if root > eval_list[i][j]:
                        root = eval_list[i][j]
    return root


def cal_eval(player1, player2):
    return player1["score"] - player2["score"]


def alpha_beta(player1, player2, board_state, board_values, cutoff_depth):
    depth = 0
    possible_i = []
    possible_j = []

    eval_func_list = calculate_eval_func(player1, player2, board_state, board_values)
    if depth < cutoff_depth:
        max_eval = alpha_beta_max(player1, player2, board_state, board_values, cutoff_depth, depth, eval_func_list, -1, -1, -9998, 9998, 0)
    for i in range(0, 5):
        for j in range(0, 5):
            if max_eval == eval_func_list[i][j]:
                possible_i.append(i)
                possible_j.append(j)
        final_ij = tie_breaker(possible_i, possible_j)
    return final_ij


def alpha_beta_max(player1, player2, board_state, board_values, cutoff_depth, depth, eval_func_list, xi, xj, alpha, beta, count):
    root = -9998
    ccount = 0
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)
    temp_board_state = copy.deepcopy(board_state)

    depth += 1
    if depth == cutoff_depth:
        for i in range(0, 5):
            for j in range(0, 5):
                if count == 1:
                    if eval_func_list[i][j] != -9999:
                        if eval_func_list[i][j] < beta:
                            if root < eval_func_list[i][j]:
                                root = eval_func_list[i][j]
                                alpha = max(alpha, root)
                        else:
                            root = eval_func_list[i][j]
                            return root
                else:
                    if eval_func_list[i][j] != -9999:
                        if eval_func_list[i][j] < beta:
                            if root < eval_func_list[i][j]:
                                root = eval_func_list[i][j]
                                alpha = max(alpha, root)
                        else:
                            root = eval_func_list[i][j]
                            return root
    else:
        for i in range(0, 5):
            for j in range(0, 5):
                if board_state[i][j] == "*":
                    attack_type = find_attack_type(i, j, board_state, player1)
                    if attack_type == "Raid":
                        raid_attack(temp_player1, temp_player2, temp_board_state, board_values, i, j)
                    else:
                        sneak_attack(temp_player1, temp_board_state, board_values, i, j)
                    ccount += 1
                    temp = alpha_beta_min(temp_player1, temp_player2, temp_board_state, board_values, cutoff_depth, depth, i, j, alpha, beta, ccount)
                    eval_func_list[i][j] = temp
                    temp_board_state = copy.deepcopy(board_state)
                    temp_player1 = copy.deepcopy(player1)
                    temp_player2 = copy.deepcopy(player2)
                    if root < eval_func_list[i][j]:
                        root = eval_func_list[i][j]
                        alpha = max(alpha, root)

    return root


def alpha_beta_min(player1, player2, board_state, board_values, cutoff_depth, depth, xi, xj, alpha, beta, count):
    depth += 1
    bcount = 0
    broot = 9998
    eval_list = []
    temp_board_state = copy.deepcopy(board_state)
    temp_player1 = copy.deepcopy(player1)
    temp_player2 = copy.deepcopy(player2)
    if depth == cutoff_depth:
        for i in range(0, 5):
            eval_list.append([])
            for j in range(0, 5):
                if temp_board_state[i][j] == "*":
                    attack_type = find_attack_type(i, j, temp_board_state, temp_player2)
                    if attack_type == "Raid":
                        raid_attack(temp_player2, temp_player1, temp_board_state, board_values, i, j)
                    else:
                        sneak_attack(temp_player2, temp_board_state, board_values, i, j)
                    eval_list[i].append(cal_eval(temp_player1, temp_player2))

                else:
                    eval_list[i].append(-9999)

                temp_board_state = copy.deepcopy(board_state)
                temp_player1 = copy.deepcopy(player1)
                temp_player2 = copy.deepcopy(player2)
                if count == 1:
                    if eval_list[i][j] != -9999:
                        if eval_list[i][j] >= alpha:
                            if broot > eval_list[i][j]:
                                broot = eval_list[i][j]
                        beta = min(beta, broot)
                else:
                    if eval_list[i][j] != -9999:
                        if eval_list[i][j] > alpha:
                            if broot > eval_list[i][j]:
                                broot = eval_list[i][j]
                            beta = min(beta, broot)
                        else:
                            broot = eval_list[i][j]
                            return broot

    else:
        for i in range(0, 5):
            eval_list.append([])
            for j in range(0, 5):
                if temp_board_state[i][j] == "*":
                    attack_type = find_attack_type(i, j, temp_board_state, temp_player2)
                    if attack_type == "Raid":
                        raid_attack(temp_player2, temp_player1, temp_board_state, board_values, i, j)
                    else:
                        sneak_attack(temp_player2, temp_board_state, board_values, i, j)
                    eval_func_list = calculate_eval_func(temp_player1, temp_player2, temp_board_state, board_values)
                    bcount += 1
                    eval_list[i].append(alpha_beta_max(temp_player1, temp_player2, temp_board_state, board_values, cutoff_depth, depth, eval_func_list, i, j, alpha, beta, bcount))

                else:
                    eval_list[i].append(-9999)
                temp_board_state = copy.deepcopy(board_state)
                temp_player1 = copy.deepcopy(player1)
                temp_player2 = copy.deepcopy(player2)
                if eval_list[i][j] != -9999:
                    if eval_list[i][j] > alpha:
                        if broot > eval_list[i][j]:
                            broot = eval_list[i][j]
                            beta = min(beta, broot)
    if broot == 9998:
        broot = alpha - 1
    return broot


def tie_breaker(possible_i, possible_j):
    final_ij = []
    if len(possible_i) == 1 and len(possible_j) == 1:
            final_ij.append(possible_i[0])
            final_ij.append(possible_j[0])
    else:
        temp_i = 6
        temp_j = 6
        for i in range(0, len(possible_i)):
            if temp_i > possible_i[i]:
                temp_i = possible_i[i]
                temp_j = possible_j[i]
            elif temp_i == possible_i[i]:
                if temp_j > possible_j[i]:
                    temp_j == possible_j[i]
        final_ij.append(temp_i)
        final_ij.append(temp_j)
    return final_ij


def output(board_state, file_name):

    for state in board_state:
        file_name.write("".join(state) + "\n")


def main():
    input_file = open(sys.argv[2], "r")
    algorithm = int(input_file.readline())
    player1 = {

    }
    player2 = {

    }
    temp_symbol = str(input_file.readline())
    player1["symbol"] = temp_symbol[0]
    if player1["symbol"] == "X":
        player2["symbol"] = "O"
    else:
        player2["symbol"] = "X"
    cutoff_depth = int(input_file.readline())
    board_values = []
    for i in range(0, 5):
        temp = input_file.readline().split()
        board_values.append(temp)
    board_state = []
    for i in range(0, 5):
        temp = input_file.readline()
        temp = temp[0:5]
        temp = list(temp)
        board_state.append(temp)
    input_file.close()

    score1 = 0
    score2 = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if board_state[i][j] == player1["symbol"]:
                score1 += int(board_values[i][j])
            elif board_state[i][j] == player2["symbol"]:
                score2 += int(board_values[i][j])

    player1["score"] = score1
    player2["score"] = score2
    next_state = open("next_state.txt", "w")
    if algorithm == 1:
        final_ij = greedy(player1, player2, board_state, board_values)
        make_move(player1, player2, board_state, board_values, final_ij, next_state)
    elif algorithm == 2:
        final_ij = minimax(player1, player2, board_state, board_values, cutoff_depth)
        make_move(player1, player2, board_state, board_values, final_ij, next_state)
    elif algorithm == 3:
        final_ij = alpha_beta(player1, player2, board_state, board_values, cutoff_depth)
        make_move(player1, player2, board_state, board_values, final_ij, next_state)
    else:
        game_time()
    next_state.close()


def make_move(player1, player2, board_state, board_values, final_ij, file_name):

    final_i = final_ij[0]
    final_j = final_ij[1]
    attack_type = find_attack_type(final_i, final_j, board_state, player1)
    if attack_type == "Sneak":
        sneak_attack(player1, board_state, board_values, final_i, final_j)
    else:
        raid_attack(player1, player2, board_state, board_values, final_i, final_j)
    output(board_state, file_name)


def game_time():
    input_file = open(sys.argv[2], "r")
    blah = int(input_file.readline())
    player1 = {

    }
    player2 = {

    }
    temp_symbol = str(input_file.readline())
    player1["symbol"] = temp_symbol[0]
    algorithm1 = int(input_file.readline())
    cutoff_depth1 = int(input_file.readline())
    temp_symbol = str(input_file.readline())
    player2["symbol"] = temp_symbol[0]
    algorithm2 = int(input_file.readline())
    cutoff_depth2 = int(input_file.readline())
    board_values = []
    for i in range(0, 5):
        temp = input_file.readline().split()
        board_values.append(temp)

    board_state = []
    for i in range(0, 5):
        temp = input_file.readline()
        temp = temp[0:5]
        temp = list(temp)
        board_state.append(temp)
    input_file.close()

    score1 = 0
    score2 = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if board_state[i][j] == player1["symbol"]:
                score1 += int(board_values[i][j])
            elif board_state[i][j] == player2["symbol"]:
                score2 += int(board_values[i][j])
    player1["score"] = score1
    player2["score"] = score2
    game_end = False
    turn = 0
    trace_state = open("trace_state.txt", "w")
    while game_end == False:
        flag = 0
        counter = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if board_state == "*":
                    counter += 1
        for i in range(0, 5):
            for j in range(0, 5):
                if board_state[i][j] == "*":
                    flag = 1
                    if turn == 0:
                        turn = 1
                        if algorithm1 == 1:
                            final_ij = greedy(player1, player2, board_state, board_values)
                            make_move(player1, player2, board_state, board_values, final_ij, trace_state)
                        elif algorithm1 == 2:
                            final_ij = minimax(player1, player2, board_state, board_values, cutoff_depth1)
                            make_move(player1, player2, board_state, board_values, final_ij, trace_state)
                        else:
                            final_ij = alpha_beta(player1, player2, board_state, board_values, cutoff_depth1)
                            make_move(player1, player2, board_state, board_values, final_ij, trace_state)

                    else:
                        turn = 0

                        if algorithm2 == 1:
                            final_ij = greedy(player2, player1, board_state, board_values)
                            make_move(player2, player1, board_state, board_values, final_ij, trace_state)
                        elif algorithm2 == 2:
                            final_ij = minimax(player2, player1, board_state, board_values, cutoff_depth2)
                            make_move(player2, player1, board_state, board_values, final_ij, trace_state)
                        else:
                            final_ij = alpha_beta(player2, player1, board_state, board_values, cutoff_depth2)
                            make_move(player2, player1, board_state, board_values, final_ij, trace_state)

        if flag == 0:
            game_end = True
    return
main()
