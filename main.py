from graphics import *

win = GraphWin("Tic-Tac-Toe", 300, 300)
# Vertical lines

Line(Point(100, 0), Point(100, 300)).draw(win)

Line(Point(200, 0), Point(200, 300)).draw(win)

# Horizontal lines

Line(Point(0, 100), Point(300, 100)).draw(win)

Line(Point(0, 200), Point(300, 200)).draw(win)
board = ["", "", "", "", "", "", "", "", ""]

board = ["", "", "", "", "", "", "", "", ""]


def get_box_number(point):

    x = point.getX()

    y = point.getY()

    if x < 100:

        col = 0

    elif x < 200:

        col = 1

    else:

        col = 2

    if y < 100:

        row = 0

    elif y < 200:

        row = 1

    else:

        row = 2

    return row * 3 + col

def get_box_number(point):

    x = point.getX()

    y = point.getY()

    if x < 100:

        col = 0

    elif x < 200:

        col = 1

    else:

        col = 2

    if y < 100:

        row = 0

    elif y < 200:

        row = 1

    else:

        row = 2

    return row * 3 + col

def draw_x_o(box_number, turn):

    x = (box_number % 3) * 100 + 50

    y = (box_number // 3) * 100 + 50

    if turn == "X":

        x_shape = Text(Point(x, y), "X")

        x_shape.setStyle("bold")

        x_shape.setSize(36)

        x_shape.draw(win)

    else:

        o_shape = Circle(Point(x, y), 40)

        o_shape.setWidth(10)

        o_shape.draw(win)
def check_game_over():

    for i in range(3):

        # Check rows

        if board[i*3] != "" and board[i*3] == board[i*3+1] == board[i*3+2]:

            return board[i*3] + " wins!"

        # Check columns

        if board[i] != "" and board[i] == board[i+3] == board[i+6]:

            return board[i] + " wins!"

    # Check diagonals

    if board[0] != "" and board[0] == board[4] == board[8]:

        return board[0] + " wins!"

    if board[2] != "" and board[2] == board[4] == board[6]:

        return board[2] + " wins!"

    # Check tie

    if "" not in board:

        return "It's a tie!"

    return ""
turn = "X"

while True:

    message = Text(Point(150, 20), "Player " + turn + "'s turn")

    message.draw(win)

    point = win.getMouse()

    box_number = get_box_number(point)

    if board[box_number] == "":

        draw_x_o(box_number, turn)

        board[box_number] = turn

        game_over = check_game_over()

        if game_over != "":

            message.setText(game_over)

            break

        turn = "O" if turn == "X" else "X"

        message.setText("Player " + turn + "'s turn")

    else:

        message.setText("That box is already taken")
closing_message = Text(Point(150, 280), "Click anywhere to close")

closing_message.draw(win)

win.getMouse()

win.close()





