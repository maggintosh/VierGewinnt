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

def print_board():
    board.one = "|_X_"
    board.two = "|_O_"
    table = ""
    for x in range(int(game.rows)):
        for y in range(int(game.columns)):
            if board.matrix[(x, y)] == board.blank:
                table += board.blank
            elif board.matrix[(x, y)] == board.one:
                table += board.one
            elif board.matrix[(x, y)] == board.two:
                table += board.two
        table += "|\n"
    print(table)
    game()

def two_players():
    board.insert = int(input("Put a disc >>> "))
    if board.insert > int(game.columns):
        print("No way, dude!")
        two_players()
    else:
        i = int(game.rows)-1
        if board.matrix[(i, (int(board.insert)-1))] == board.blank:
            board.matrix[(i, (int(board.insert)-1))] = board.one
        else:
            while board.matrix[(i, (int(board.insert)-1))] != board.blank:
                i -= 1
            board.matrix[(i, (int(board.insert)-1))] = board.one
                    
        print_board()
     
def one_player():
    pass

def game():
    if game.players == "1":
        one_player()
    elif game.players == "2":
        two_players()

def connectfour():
    players()

connectfour()
