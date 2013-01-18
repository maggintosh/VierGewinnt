class game:
    def __init__(self, rows = "4", columns = "4", players = 1):
        self.rows = rows
        self.columns = columns
        self.players = players

class board:
    def __init__(self, blank = "|___|", one = "|_X_|", two = "|_O_|", matrix = "", insert = ""):
        self.blank = blank
        self.one = one
        self.two = two
        self.matrix = martix
        self.insert = insert

def players():
    p = input("How many players?\nOne player (1) or two players (2)? ")
    if p == "1":
        game.players = "1"
    elif p == "2":
        game.players = "2"
    else:
        print("No way, dude!")
        players()
    make_board()

def make_board():
    board.matrix = dict()
    print("Ok, and now the size of the board:")
    r = input("How many rows? ")
    c = input("How many columns? ")
    if int(r) < 4 or int(c) < 4:
        print("No way, dude!")
        make_board()
    else:
        game.rows = r
        game.columns = c
    blank_board()

def blank_board():
    board.blank = "|___"
    board.matrix = dict()
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            board.matrix[(x, y)] = board.blank
    print_board()
    game()

def print_board():
    board.one = "|_X_"
    board.two = "|_O_"
    table = ""
    print ("\n###### VIER GEWINNT ######\n")
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            if board.matrix[(x, y)] == board.blank:
                table += board.blank
            elif board.matrix[(x, y)] == board.one:
                table += board.one
            elif board.matrix[(x, y)] == board.two:
                table += board.two
        table += "|\n"
    for x in range(int(game.columns)):
        table += "  " + str(x+1) + " "
    table += "\n"
    print(table)

def pvcpu():
    player_1()
    player_2()
    pvcpu()

def player_1():
    board.insert = int(input("Put a disc, Player 1 >>> "))
    if board.insert in range(int(game.columns)+1):
        i = int(game.rows)-1
        if board.matrix[(i, (int(board.insert)-1))] == board.blank:
            board.matrix[(i, (int(board.insert)-1))] = board.one
        else:
            while board.matrix[(i, (int(board.insert)-1))] != board.blank:
                i -= 1
            board.matrix[(i, (int(board.insert)-1))] = board.one
        print_board()
        win_check()
    else:
        print("No way, dude!")
        player_1()

def player_2():
    board.insert = int(input("Put a disc, Player 2 >>> "))
    if board.insert in range(int(game.columns)+1):
        i = int(game.rows)-1
        if board.matrix[(i, (int(board.insert)-1))] == board.blank:
            board.matrix[(i, (int(board.insert)-1))] = board.two
        else:
            while board.matrix[(i, (int(board.insert)-1))] != board.blank:
                i -= 1
            board.matrix[(i, (int(board.insert)-1))] = board.two
        print_board()
        win_check()
    else:
        print("No way, dude!")
        player_2()
     
def one_player():
    pass

def new_game():
    new = input("Wanna start a new game (n) or quit (q)? ")
    if new == "n" or new == "N":
        connectfour()
    elif new == "q" or new == "Q":
        quit()
    else:
        print("No way, dude!")
        new_game()
def game():
    if game.players == "1":
        pvp()
    elif game.players == "2":
        pvcpu()

def win_check():
    win_vertical()
    win_horizontal()
    win_diagonal_down()
    win_diagonal_up()

def win_vertical():
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x+1, y)] == board.one and board.matrix[(x+2, y)] == board.one and board.matrix[(x+3, y)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x+1, y)] == board.two and board.matrix[(x+2, y)] == board.two and board.matrix[(x+3, y)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()
            except KeyError:
                pass

def win_horizontal():
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x, y+1)] == board.one and board.matrix[(x, y+2)] == board.one and board.matrix[(x, y+3)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x, y+1)] == board.two and board.matrix[(x, y+2)] == board.two and board.matrix[(x, y+3)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()
            except KeyError:
                pass

def win_diagonal_down():
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x+1, y+1)] == board.one and board.matrix[(x+2, y+2)] == board.one and board.matrix[(x+3, y+3)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x+1, y+1)] == board.two and board.matrix[(x+2, y+2)] == board.two and board.matrix[(x+3, y+3)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()       
            except KeyError:
                pass

def win_diagonal_up():
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            try:
                if board.matrix[(x, y)] == board.one and board.matrix[(x-1, y+1)] == board.one and board.matrix[(x-2, y+2)] == board.one and board.matrix[(x-3, y+3)] == board.one:
                    print("\n###########################\n###### Player 1 wins ######\n###########################\n")
                    new_game()
                elif board.matrix[(x, y)] == board.two and board.matrix[(x-1, y+1)] == board.two and board.matrix[(x-2, y+2)] == board.two and board.matrix[(x-3, y+3)] == board.two:
                    print("\n###########################\n###### Player 2 wins ######\n###########################\n")
                    new_game()                
            except KeyError:
                pass

def connectfour():
    players()

connectfour()
