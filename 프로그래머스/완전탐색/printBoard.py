def print_board(board):
    for row in board:
        for col in row:
            if col < 0:
                print(f"{col} ", end='')
            else:
                print(f" {col} ", end='')
        print()
