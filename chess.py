# The goal of this program is to build a program that plays chess against user

class chess():
    def __init__(self):
        self.dict = make_dict()
        self.board = make_board(self.dict)
        while True:
            display(self)
            self.dict = move(self.dict)

# Put the pieces into a dictionary
def make_dict():
    pcs = {}
    titles = ['R1', 'N1', 'B1', 'K', 'Q', 'B2', 'N2', 'R2']
    rows1 = [0, 7]
    rows2 = [1, 6]
    colors = ['B', 'W']
    for k in range(2):
        for title in titles:
            pcs[f'{colors[k]}{title}'] = [title[0], [rows1[k], titles.index(title)]]
        for m in range(8):
            pcs[f'{colors[k]}P{m}'] = ['P', [rows2[k], m]]
    return pcs

# Make the initial board for the game
def make_board(pieces):
    board = []
    for m in range(8):
        board.append([])
        for n in range(8):
            board[m].append('.')
    for key in pieces.keys():
        board[pieces[key][1][0]][pieces[key][1][1]] = f'{pieces[key][0][0]}'
    return board

# Show the user the current board
def display(self):
    print('\n___________________')
    print('| 1 2 3 4 5 6 7 8 |')
    for row in range(len(self.board)):
        line = f'{row+1} '
        for col in self.board[row]:
            line = f"{line}{col} "
        line = f'{line}|'
        print(line)
    print('|_________________|\n')

# Prompt user for move, validate, and remove piece if required
def move(indict):
    start = str(input('\nStart: '))
    rows = start[0]
    cols = start[1]
    fin = str(input('\nFinish: '))
    rowf = fin[0]
    colf = fin[1]
