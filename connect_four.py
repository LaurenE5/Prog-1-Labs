# blank board
def print_board(board):
    for row in board[::-1]:
        for element in row:
            print(element, end='')
        print()


# board is boarding
def initialize_board(num_rows, num_cols):
    return[['-' for j in range(num_cols)]
           for i in range(num_rows)]


# places x or o chip on board
def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row


# checks to see if there are four of the same chip types in a row
def check_if_winner(board, col, row, chip_type):
    count = 0
    for i in board[row]:
        # counts numbers of chips in a row
        if i == chip_type:
            count += 1
            # player wins if 4 in row
            if count == 4:
                return True
        # count restarts
        else:
            count = 0
    count = 0
    if row >= 3:
        for i in range(row + 1):
            # counts number of chips in a row
            if board[row - i][col] == chip_type:
                count += 1
                # player wins if 4 in a row
                if count == 4:
                    return True
            # count restarts
            else:
                count = 0
    # they didnt win :(
    return False


# checks to see if game tied
def draw_game(board):
    for row in board:
        for element in row:
            # if there is an empty element, no tie game
            if element == '-':
                return False
    # tie game is board full and no 4 chip type in row
    return True


def main():
    # user input
    num_rows = int(input('What would you like the height of the board to be? '))
    num_cols = int(input('What would you like the length of the board to be? '))
    board = initialize_board(num_rows, num_cols)
    # prints initial board
    print_board(board)

    # assigns each player chip type
    print('\nPlayer 1: x\nPlayer 2: o\n')

    player = 1
    chip_type = ' x '

    while True:
        # game begin
        col = int(input(f"Player {player}: Which column would you like to choose? "))

        # reestablishes row where chip fell
        row = insert_chip(board, col, chip_type)

        # sees if player won
        win_game = check_if_winner(board, col, row, chip_type)

        print_board(board), print('\n')

        # ends game if player won, otherwise goes to tie game function
        if win_game == True:
            print(f'Player {player} won the game!')
            exit()
        elif win_game == False:
            for element in board[-1]:
                if element == '-':
                    break
                else:
                    if draw_game(board):
                        print('Draw. Nobody wins.')
                        exit()

        # changes from player 1 to player 2
        player = 2 if player == 1 else 1
        # changes chip type from x to o
        chip_type = ' o ' if chip_type == ' x ' else ' x '

if __name__ == '__main__':
    main()
