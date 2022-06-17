import random

import data
import string


def find_word_rec(check_board, mn_board, word, possibleCoordinates, temp, pos_words=[], cur_step=1):
    # print('temp', temp, 'word', word)
    _x, _y = possibleCoordinates

    if len(temp) == len(word):
        print('worked')
        pos_words.append(temp)
        return

    pos_movements = [
        (1, 1), (1, 0), (0, 1), (1, -1),
        (0, -1), (-1, 0), (-1, -1), (-1, 1)
    ]

    for movement in pos_movements:
        xTotalMovement = _x + movement[0]
        yTotalMovement = _y + movement[1]

        #  if len(check_board[:_x])-1 < xTotalMovement:
        #             if len(check_board[:_x][:_y]) < yTotalMovement:
        #                 print('check_board[xMovement]',check_board[xTotalMovement])
        #                 print('check_board[xMovement][yMovement]', check_board[xTotalMovement][yTotalMovement])
        # print("check_board", len(check_board), ' xTotalMovement', xTotalMovement)
        if xTotalMovement < len(check_board) and yTotalMovement < len(check_board[xTotalMovement]):
            print('word[cur_step]', word[cur_step])
            checkCondition = \
                check_board[xTotalMovement][yTotalMovement] == 'n' and \
                mn_board[xTotalMovement][yTotalMovement] == word[cur_step] and \
                xTotalMovement >= 0 and \
                yTotalMovement >= 0

            if checkCondition:
                check_board[xTotalMovement][yTotalMovement] = 'y'
                find_word_rec(check_board, mn_board, word, [xTotalMovement, yTotalMovement],
                              temp + mn_board[xTotalMovement][yTotalMovement],
                              pos_words, cur_step + 1)


def find_word(board, word):
    # print("Board Inside Find Words: ", board)
    check_board = []
    boardInternalArrayWidth = len(board[0])
    boardArrayLength = len(board)

    for i in range(boardArrayLength):
        temp = []
        for j in range(boardInternalArrayWidth):
            temp.append('n')
        # print("Temp: ", temp)
        check_board.append(temp)
    # print("Check Board: ", check_board)

    pos_cord = []  # possible coordinates
    print(word)
    for i in range(boardArrayLength):
        for j in range(boardInternalArrayWidth):
            # print('board[i][j]', board[i][j])
            if board[i][j] == word[0]:
                pos_cord.append([i, j])
                # print("BoardIJ , Word_0, Pos_Cord:", board[i][j], word[0], [i, j])

    pos_words = []  # possible words
    for _cord in pos_cord:
        # print('_cord: ', _cord)
        # Cord 0 means x and cord 1 means y
        check_board[_cord[0]][_cord[1]] = 'y'
        # print(check_board)
        find_word_rec(check_board, board, word, _cord, word[0], pos_words, 1)
        #             check_board, mn_board, word, _x,      _y,      temp,    pos_words=[], cur_step=1

        for c in pos_words:
            if c == word:
                return True
        return False


def renderBoard(checkBoard):
    print(
        '\n'.join(['  '.join(letter) for letter in checkBoard])
    )


board = []
if __name__ == "__main__":
    characters = ''.join(random.choice(string.ascii_uppercase) for _ in range(16))
    board = [[*characters[0:4]], [*characters[4:8]], [*characters[8:12]], [*characters[12:16]]]
    renderBoard(board)
    while True:
        nameToFind = str(input("Name to find: ")).upper()
        if not nameToFind:
            nameToFind = "ILAEC"
        isSuccess = find_word(board, nameToFind)
        print(isSuccess)