def board_init(width, height):
    return [[None for _ in range(width)] for _ in range(height)]


def print_board(board):
    for row in board:
        print(row)


def all_equal(lst):
    return all([x == lst[0] and x is not None for x in lst])


def check_horizontal_win(board):
    for y, row in enumerate(board):
        for x in range(len(row) - 2):
            if all_equal(row[x : x + 3]):
                return True
    return False


def check_vertical_win(board):
    for x in range(3):
        cur = []
        for y in range(3):
            cur.append(board[y][x])
        if all_equal(cur):
            return True
    return False


def check_diagonal_win(board):
    for y in range(len(board) - 2):
        for x in range(len(board[0]) - 2):
            cur = []
            for i in range(3):
                cur.append(board[y + i][x + i])
            if all_equal(cur):
                return True
    return False


def check_board(board):
    if (
        check_horizontal_win(board)
        or check_vertical_win(board)
        or check_diagonal_win(board)
    ):
        return True
    return False


def get_input(board):
    while True:
        try:
            x, y = [int(x) for x in input("Next Move: ").split(" ")]
            if board[y][x] is None:
                return x, y
            else:
                print("Invalid move. The cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalud input. Please enter two integers separated by a space.")


def run():
    board = board_init(3, 3)
    curPlayer = 0
    while True:
        print_board(board)
        x, y = get_input(board)
        board[y][x] = curPlayer
        if check_board(board):
            print(f"{curPlayer} wins")
            break
        curPlayer = (curPlayer + 1) % 2


if __name__ == "__main__":
    run()
