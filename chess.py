# The goal of this program is to build a program that plays chess against user

class chess():
    def __init__(self):
        self.dict = make_dict()
        self.turn = 'W'
        self.run = True
        self.winner = 0
        
        make_board(self)
        display(self)
        while self.run:
            move(self)
            make_board(self)
            # print(len(self.dict.keys())) # Prints the number of pieces left
            if 'WK1' not in self.dict.keys():
                self.winner = 'Black'
                self.run = False
            elif 'BK1' not in self.dict.keys():
                Self.winner = 'White'
                self.run = False
            else:
                display(self)
        
# Put the pieces into a dictionary
def make_dict():
    pcs = {}
    titles = ['R1', 'N1', 'B1', 'K1', 'Q1', 'B2', 'N2', 'R2']
    rows1 = [0, 7]
    rows2 = [1, 6]
    colors = ['B', 'W']
    for k in range(2):
        for title in titles:
            pcs[f'{colors[k]}{title}'] = [colors[k], title[0], [rows1[k], titles.index(title)]]
        for m in range(8):
            pcs[f'{colors[k]}P{m+1}'] = [colors[k], 'P', [rows2[k], m]]
    return pcs

# Make the initial board for the game
def make_board(self):
    pieces = self.dict
    board = []
    for m in range(8):
        board.append([])
        for n in range(8):
            board[m].append(' . ')
    for key in pieces.keys():
        board[pieces[key][2][0]][pieces[key][2][1]] = f'{key}'
    self.board = board

# Show the user the current board
def display(self):
    if self.turn == 'B': turn = 'Black'
    elif self.turn == 'W': turn = 'White'
    if self.run:
        print(f'\n\tTurn: {turn}')
    else:
        print('\n\n\n\n\n\tFinal Game Board')
    print('___________________________________')
    print('|  1   2   3   4   5   6   7   8  |')
    for row in range(len(self.board)):
        line = f'{row+1} '
        for col in self.board[row]:
            line = f'{line}{col} '
        line = f'{line}|'
        print(line)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
    if not self.run:
        if self.winner == 0:
            print(f'\tGame was a draw\n')
        else:
            print(f'\tGame was won by {self.winner}\n')
    

# Prompt user for move, validate, and remove piece if required
def move(self):
    while True:
        rows, cols = get_input('start')
        if rows == 'q':
            self.run = False
            break
        rowf, colf = get_input('finish')
        if rowf == 'q':
            self.run = False
            break

        # Find if there is a piece on the board that is on the coordinates  
        all_locs = []
        opponents = []
        for key in self.dict.keys():
            all_locs.append(self.dict[key][2])
        if [rows, cols] in all_locs:
            key = list(self.dict.keys())[all_locs.index([rows, cols])] 
            color = self.dict[key][0]
            for key in self.dict.keys():
                if self.dict[key][0] != color:
                    opponents.append(self.dict[key][2])
            key = list(self.dict.keys())[all_locs.index([rows, cols])]
            break
        else:
            import colorama
            print(colorama.Fore.RED)
            print(f'There is no piece at [{rows+1}, {cols+1}]')
            print('Please select another piece')
            print(colorama.Style.RESET_ALL)

    # Check if the move is valid for the piece in question to move to
    valid = False

    if self.run:
        # Make sure the destination is on the board    
        if rowf > 7 or rowf < 0 or colf > 7 or colf < 0:
            pass
        elif [rows, cols] == [rowf, colf]:
            pass
        elif color != self.turn:
            import colorama
            print(colorama.Fore.RED)
            print('\nPlease choose the proper color of piece.')
            print(colorama.Style.RESET_ALL)
        else:
            # Check the move specific to the piece.
            title = self.dict[key][1]
            color = self.dict[key][0]            
            if title == 'P': # Pawns
                if color == 'B':
                    start_row = 1
                    sign = 1
                elif color == 'W':
                    start_row = 6
                    sign = -1
                diff = (rowf - rows) * sign
                if rows == start_row:
                    index = 2
                else:
                    index = 1
                if diff > 0 and diff <= index and cols == colf:
                    betweens = 0
                    for k in range(abs(diff)):
                        if [(k+1)*sign+rows, colf] in all_locs:
                            betweens += 1
                    if betweens == 0:
                        valid = True
                elif rowf-rows == sign and abs(colf-cols) == 1:
                    if [rowf, colf] in all_locs:
                        valid = True
                        rid(self, rowf, colf)
                        
            elif title == 'R': # Rooks
                if rowf == rows:
                    if abs(colf-cols) == 1:
                        if [rowf, colf] not in all_locs:
                            valid = True
                        elif [rowf, colf] in opponents:
                            valid = True
                            rid(self, rowf, colf)
                    else:
                        diff = abs(colf-cols)
                        betweens = 0
                        for k in range(1, diff):
                            if [rowf, int(cols + k*(colf-cols)/diff)] in all_locs:
                                betweens += 1
                        if betweens == 0:
                            if [rowf, colf] not in all_locs:
                                valid = True
                            elif [rowf, colf] in opponents:
                                valid = True
                                rid(self, rowf, colf)
                elif colf == cols:
                    if abs(rowf-rows) == 1:
                        if [rowf, colf] not in all_locs:
                            valid = True
                        elif [rowf, colf] in opponents:
                            valid = True
                            rid(self, rowf, colf)
                    else:
                        diff = abs(rowf-rows)
                        betweens = 0
                        for k in range(1, diff):
                            if [int(rows + k*(rowf-rows)/diff), colf] in all_locs:
                                betweens += 1
                        if betweens == 0:
                            if [rowf, colf] not in all_locs:
                                valid = True
                            elif [rowf, colf] in opponents:
                                valid = True
                                rid(self, rowf, colf)

            elif title == 'B': # Bishops
                if abs(rowf-rows) != abs(colf-cols):
                    pass
                else:
                    row_sign = int((rowf-rows)/abs(rowf-rows))
                    col_sign = int((colf-cols)/abs(colf-cols))
                    betweens = 0
                    k = 1
                    while k < abs(rowf-rows):
                        if [rows+k*row_sign, cols+k*col_sign] in all_locs:
                            betweens += 1
                        k += 1
                    if betweens == 0:
                        if [rowf, colf] not in all_locs:
                            valid = True
                        elif [rowf, colf] in opponents:
                            valid = True
                            rid(self, rowf, colf)
                            
            elif title == 'Q': # Queens
                if rowf == rows:
                    if abs(colf-cols) == 1:
                        if [rowf, colf] not in all_locs:
                            valid = True
                        elif [rowf, colf] in opponents:
                            valid = True
                            rid(self, rowf, colf)
                    else:
                        diff = abs(colf-cols)
                        betweens = 0
                        for k in range(1, diff):
                            if [rowf, int(cols + k*(colf-cols)/diff)] in all_locs:
                                betweens += 1
                        if betweens == 0:
                            if [rowf, colf] not in all_locs:
                                valid = True
                            elif [rowf, colf] in opponents:
                                valid = True
                                rid(self, rowf, colf)
                elif colf == cols:
                    if abs(rowf-rows) == 1:
                        if [rowf, colf] not in all_locs:
                            valid = True
                        elif [rowf, colf] in opponents:
                            valid = True
                            rid(self, rowf, colf)
                    else:
                        diff = abs(rowf-rows)
                        betweens = 0
                        for k in range(1, diff):
                            if [int(rows + k*(rowf-rows)/diff), colf] in all_locs:
                                betweens += 1
                        if betweens == 0:
                            if [rowf, colf] not in all_locs:
                                valid = True
                            elif [rowf, colf] in opponents:
                                valid = True
                                rid(self, rowf, colf)
                elif abs(rowf-rows) == abs(colf-cols):
                    row_sign = int((rowf-rows)/abs(rowf-rows))
                    col_sign = int((colf-cols)/abs(colf-cols))
                    betweens = 0
                    k = 1
                    while k < abs(rowf-rows):
                        if [rows+k*row_sign, cols+k*col_sign] in all_locs:
                            betweens += 1
                        k += 1
                    if betweens == 0:
                        if [rowf, colf] not in all_locs:
                            valid = True
                        elif [rowf, colf] in opponents:
                            valid = True
                            rid(self, rowf, colf)
            elif title == 'K': # King
                if abs(rowf-rows) <= 1 and abs(colf-cols) <= 1:
                    if [rowf, colf] not in all_locs:
                        valid = True
                    elif [rowf, colf] in opponents:
                        valid = True
                        rid(self, rowf, colf)

            elif title == 'N': # Knight
                if abs(rowf-rows) == 1 and abs(colf-cols) == 2:
                    if [rowf, colf] not in all_locs:
                        valid = True
                    elif [rowf, colf] in opponents:
                        valid = True
                        rid(self, rowf, colf)
                elif abs(rowf-rows) == 2 and abs(colf-cols) == 1:
                    if [rowf, colf] not in all_locs:
                        valid = True
                    elif [rowf, colf] in opponents:
                        valid = True
                        rid(self, rowf, colf)
                        
            print(valid)
            if valid:
                self.dict[key][2] = [rowf, colf]
                if self.turn == 'B': self.turn = 'W'
                elif self.turn == 'W': self.turn = 'B'

# Removes the selected piece from the dictionary
def rid(self, rowf, colf):
    stuff = []
    for key in self.dict.keys():
        if self.dict[key][2] == [rowf, colf]:
            stuff.append(key)
    for key in stuff:
        del self.dict[key]

# Ask the player for their input for the game
def get_input(word):
    while True:
        block = str(input(f'{word.title()}: '))
        if len(block) != 2:
            if block == 'q':
                return block, block
            import colorama
            print(colorama.Fore.RED)
            print('Please input the coordinates as a two digit number')
            print(colorama.Style.RESET_ALL)
        else:
            try:
                int(block[0])
                try:
                    int(block[1])
                    return int(block[0])-1, int(block[1])-1
                except ValueError:
                    pass
            except ValueError:
                pass

game = chess()
