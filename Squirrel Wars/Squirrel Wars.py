import copy
import sys
from decimal import Decimal
pos_inf = Decimal('Infinity')
neg_inf = Decimal('-Infinity')

def identifyTask():
    my_file = open(sys.argv[2], "r")
    task = my_file.readline().strip()
    my_file.close()
    return int(task)

def parse_file():
    my_file = open(sys.argv[2], "r")
    task = my_file.readline().strip()
    player = my_file.readline().strip()
    depth = my_file.readline().strip()
    Grid = []
    for i in range(5):
        row = my_file.readline().split();
        Grid.append(row);

    State = []
    for j in range(5):
        row = my_file.readline().strip();
        ROW = list(row)
        State.append(ROW);

    my_file.close()

    return(task, player, depth, Grid, State)

def parseBattleShipFile():
    my_file = open(sys.argv[2], "r")
    task = my_file.readline().strip()
    player = my_file.readline().strip()
    playerAlgorithm = my_file.readline().strip()
    playerDepth = my_file.readline().strip()

    opponentPlayer = my_file.readline().strip()
    opponentAlgorithm = my_file.readline().strip()
    opponentPlayerDepth = my_file.readline().strip()

    Grid = []
    for i in range(5):
        row = my_file.readline().split()
        Grid.append(row)

    State = []
    for j in range(5):
        row = my_file.readline().strip();
        ROW = list(row)
        State.append(ROW);

    my_file.close()
    return (task, player, playerAlgorithm, playerDepth, opponentPlayer, opponentAlgorithm, opponentPlayerDepth, Grid, State)

def getPossibleMoves(currentState):
    return [
        (i, j)
            for i in range(len(currentState))
                for j in range(len(currentState[i]))
                    if currentState[i][j] == '*'
    ]

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print board[i][j],
        print
    print

def opponentPlayer(currentPlayer):
    if(currentPlayer == 'X'):
        return 'O'
    else:
        return 'X'

def movesAvailable(currentState):
    for i in range(len(currentState)):
        for j in range(len(currentState[i])):
            if(currentState[i][j] == '*'):
                return 1
    return 0

def isValidMove(currentState, row, col):
    tempBoard = copy.deepcopy(currentState)
    if(tempBoard[row][col] == '*'):
        return 1
    else:
        return 0

def isRaid(currentState, row, col, player):
    tempBoard = copy.deepcopy(currentState)
    if(row >0 and col <=len(currentState)-1):
        if(tempBoard[row-1][col] == player):
            return 1
    if(col >0 and row <=len(currentState)-1):
        if(tempBoard[row][col-1] == player):
            return 1
    if(row <len(currentState)-1 and col <=len(currentState)-1):
        if(tempBoard[row+1][col] == player):
            return 1
    if(row <= len(currentState)-1 and col <len(currentState)-1):
        if(tempBoard[row][col+1] == player):
            return 1

    return 0

def calculateBoardValue(currentState, valueGrid, player):
    tempBoard = copy.deepcopy(currentState)
    boardValue = 0
    opponent = opponentPlayer(player)
    for i in range(len(tempBoard)):
        for j in range(len(tempBoard[i])):
            if(tempBoard[i][j] == player):
                boardValue += int(valueGrid[i][j])
            elif(tempBoard[i][j] == opponent):
                boardValue -= int(valueGrid[i][j])
    return boardValue

def changeBoardRaid(currentState, player, row, col):
    otherPlayer = opponentPlayer(player)
    tempBoard = copy.deepcopy(currentState)
    if(col > 0 and row  <=len(currentState)-1):
        if(tempBoard[row][col-1] == otherPlayer):
            tempBoard[row][col-1] = player
    if(row <=len(currentState)-1 and col <len(currentState)-1):
        if(tempBoard[row][col+1] == otherPlayer):
            tempBoard[row][col+1] = player
    if(row >0 and col <= len(currentState)-1):
        if(tempBoard[row-1][col] == otherPlayer):
            tempBoard[row-1][col] = player
    if(row <len(currentState)-1 and col <= len(currentState)-1):
        if(tempBoard[row+1][col] == otherPlayer):
            tempBoard[row+1][col] = player

    return tempBoard

def makeMove(board, valueGrid, row, col, player):
    tempBoard = copy.deepcopy(board)
    tempBoard[row][col] = player
    if(isRaid(tempBoard, row, col, player) == 1):
        tempBoard = changeBoardRaid(tempBoard, player, row, col)
    value = calculateBoardValue(tempBoard, valueGrid, player)
    return (value, tempBoard)

def compareAndUpdateBounds(score, alpha, beta, isMaxPlayer):
    if isMaxPlayer:
        alpha = max(alpha, score)
    else:
        beta = min(beta, score)
    return (alpha, beta)

def greedyBestFirstSearch(currentState, valueGrid, player, depth):

    path = []
    result = copy.deepcopy(currentState)
    possibleMoves = getPossibleMoves(currentState)
    if(len(possibleMoves) == 0):
        return calculateBoardValue(result, valueGrid, player)
    currentSquareScore = 0
    row = 0
    col = 0
    for i in range(len(currentState)):
        for j in range(len(currentState[i])):
            tempBoard = copy.deepcopy(currentState)
            if isValidMove(tempBoard, i, j):
                tempSquareScore = makeMove(tempBoard, valueGrid, i, j, player)
                if tempSquareScore > currentSquareScore:
                    currentSquareScore = tempSquareScore
                    row = i
                    col = j

    result[row][col] = player
    if(isRaid(result, row, col, player) == 1):
        result = changeBoardRaid(result, player, row, col)
    path.append(result)
    bestScore = calculateBoardValue(result, valueGrid, player)
    return(path, bestScore)

def miniMax(currentState, valueGrid, player, maxPlayer, currentDepth, maxDepth, curTile):
    path = []
    tempboard = currentState
    if currentDepth == maxDepth:
        currentBoardValue = calculateBoardValue(tempboard, valueGrid, maxPlayer)
        print(curTile, currentDepth, currentBoardValue)
        return (path, currentBoardValue)

    if movesAvailable(tempboard) == 0:
        currentBoardValue = calculateBoardValue(tempboard, valueGrid, maxPlayer)
        print(curTile, currentDepth, currentBoardValue)
        return (path, currentBoardValue)

    isMaxPlayer = player == maxPlayer

    if isMaxPlayer:
        newBestScore = lambda x,y : x < y
        bestScore = neg_inf
    else:
        newBestScore = lambda x,y : x > y
        bestScore = pos_inf

    print(curTile, currentDepth, bestScore)

    bestBoard = None
    for i in range(len(tempboard)):
        for j in range(len(tempboard[i])):
            if isValidMove(tempboard, i, j):
                (value, possibleBoard) = makeMove(tempboard, valueGrid, i, j, player)
                otherPlayer = opponentPlayer(player)
                chosenTile = "" + chr(65 + j) + str(i + 1)
                (path, boardValue) = miniMax(possibleBoard, valueGrid, otherPlayer, maxPlayer, currentDepth + 1, maxDepth, chosenTile)
                if newBestScore(bestScore, boardValue) == True:
                    bestScore = boardValue
                    bestBoard = possibleBoard
                print(curTile, currentDepth, bestScore)

    path.append(bestBoard)
    return (path, bestScore)

def alphaBeta(currentState, valueGrid, player, maxPlayer, currentDepth, maxDepth, curTile, alpha, beta):
    path = []

    if currentDepth == maxDepth:
        currentBoardValue = calculateBoardValue(currentState, valueGrid, maxPlayer)
        print(curTile, currentDepth, currentBoardValue, alpha, beta)
        return (path, currentBoardValue)

    possibleMoves = getPossibleMoves(currentState)

    if len(possibleMoves) == 0:
        currentBoardValue = calculateBoardValue(currentState, valueGrid, maxPlayer)
        print(curTile, currentDepth, currentBoardValue, alpha, beta)
        return (path, currentBoardValue)

    isMaxPlayer = player == maxPlayer

    if isMaxPlayer:
        newBestScore = lambda x,y : x < y
        bestScore = neg_inf
    else:
        newBestScore = lambda x,y : x > y
        bestScore = pos_inf

    print(curTile, currentDepth, bestScore, alpha, beta)
    bestBoard = None
    for (i, j) in possibleMoves:
        (value, possibleBoard) = makeMove(currentState, valueGrid, i, j, player)
        otherPlayer = opponentPlayer(player)
        chosenTile = "" + chr(65 + j) + str(i + 1)
        (path, boardValue) = alphaBeta(possibleBoard, valueGrid, otherPlayer, maxPlayer, currentDepth + 1, maxDepth, chosenTile, alpha, beta)
        if newBestScore(bestScore, boardValue) == True:
            bestScore = boardValue
            bestBoard = possibleBoard
            (alpha, beta) = compareAndUpdateBounds(bestScore, alpha, beta, isMaxPlayer)
        print(curTile, currentDepth, bestScore, alpha, beta)
        if beta <= alpha:
            break

    path.append(bestBoard)
    return (path, bestScore)

def battleShip(currentState, valueGrid, player, opponentPlayer, playerDepth, opponentPlayerDepth, playerAlgorithm, opponentPlayerAlgorithm):

    tempBoard = copy.deepcopy(currentState)
    possibleMoves = getPossibleMoves(tempBoard)
    numberOfPossibleMoves = len(possibleMoves)

    while(numberOfPossibleMoves > 0):
        path = []
        print "Player " + player + "'s Turn"
        if playerAlgorithm == 1:
            (path, BestScore) = greedyBestFirstSearch(tempBoard, valueGrid, player, playerDepth)
        if playerAlgorithm == 2:
            (path, BestScore) = miniMax(tempBoard, valueGrid, player, player, 0, playerDepth, "root")
        if playerAlgorithm == 3:
            (path, BestScore) = alphaBeta(tempBoard, valueGrid, player, player, 0, playerDepth, "root", neg_inf, pos_inf)

        printBoard(path[len(path) - 1])
        tempBoard = path[len(path) - 1]

        numberOfPossibleMoves -= 1
        if numberOfPossibleMoves == 0:
            break;

        print "Player " + opponentPlayer + "'s Turn"

        if opponentPlayerAlgorithm == 1:
            (path, BestScore) =  greedyBestFirstSearch(tempBoard, valueGrid, opponentPlayer, opponentPlayerDepth)
        if opponentPlayerAlgorithm == 2:
            (path, BestScore) = miniMax(tempBoard, valueGrid, opponentPlayer, opponentPlayer, 0, opponentPlayerDepth, "root")
        if opponentPlayerAlgorithm == 3:
            (path, BestScore) = alphaBeta(tempBoard, valueGrid, opponentPlayer, opponentPlayer, 0, opponentPlayerDepth, "root", neg_inf, pos_inf)

        printBoard(path[len(path) - 1])
        tempBoard = path[len(path) - 1]

        numberOfPossibleMoves = numberOfPossibleMoves - 1
    return 0


def main():
    task = identifyTask()
    if task < 4:
        (task, player, depth, boardGrid, boardState) = parse_file()
    else:
        (task, player, playerAlgorithm, playerDepth, opponentPlayer, opponentPlayerDepth, opponentPlayerAlgorithm,  boardGrid, boardState) = parseBattleShipFile()




    if task == "1":
        (path, bestScore) = greedyBestFirstSearch(boardState, boardGrid, player, depth)
    elif task == "2":
        print "----TRACE LOG----"
        (path, miniMaxValue) = miniMax(boardState, boardGrid, player, player, 0, 2, "root")
    elif task == "3":
        print "----TRACE LOG----"
        (path, bigFatPig) = alphaBeta(boardState, boardGrid, player, player, 0, 2, "root", neg_inf, pos_inf)
    print
    print
    print "----NEXT STATE----"
    printBoard(path[len(path)- 1])


if __name__ == '__main__':
    main()
