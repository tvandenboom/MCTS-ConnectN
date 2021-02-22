import numpy as np

class ConnectFour:
    win_length = 4
    num_rows = 6
    num_cols = 7

    #Each ConnectFour object is a board_state, which is an array
    #of 0's (empty squares), 1's (red chips) and -1's (black chips).
    #The red chips are played on odd turns, black chips on even turns.
    def __init__(self):
        #On initialization, the board_state is empty and the turn is 1
        self.board_state = np.zeros((self.num_rows,self.num_cols), dtype=int)
        self.turn = 0
        self.is_won = False
        self.legal_moves = np.arange(7)
        self.last_move = (-1,-1)

    def play_chip(self, column):
        #First check if the game is over:
        if self.is_won == True:
            print('The game is over; %s has won.' % self.winner)
        else:
            #Player whose turn it is places a chip in column
            #Determine whose turn it is:
            if self.turn % 2 == 0:
                chip = 1
            else:
                chip = -1

            #If suggested move is legal, play the chip in column and go to next turn.
            if column in self.legal_moves:
                self.last_move = np.amax(np.where(self.board_state[:,column] == 0)),column
                self.board_state[self.last_move] = chip
                self.turn += 1
            else:
                print('Column is full; please suggest another move.')


            #Check to see if the game has been won:
            self.check_win()
            
            if self.is_won == True:
                print('The game is over; %s wins!' % self.winner)
            else:
                #Redetermine the legal moves in the board_state:
                self.legal_moves = np.where(self.board_state[0]==0)[0]

    def check_win(self):
        #Checks for a winning position for both players relative to self.last_move:
        #Check for row wins
        y,x = self.last_move

        #Check for column wins containing self.last_move (there can be only one):
        if (y <= self.num_rows - self.win_length):
            sum_temp = 0
            for k in range(0,self.win_length):
                sum_temp += self.board_state[y+k][x]
            if sum_temp == self.win_length:
                self.winner = 'Player 1'
                self.is_won = True
                return
            elif sum_temp == -self.win_length:
                self.winner = 'Player 2'
                self.is_won = True
                return

        #Check for row wins containing self.last_move:
        for i in range(0,self.win_length):
            if (x-i <= self.num_cols - self.win_length and x-i >= 0):
                sum_temp = 0
                for k in range(0,self.win_length):
                    sum_temp += self.board_state[y][x-i+k]
                if sum_temp == self.win_length:
                    self.winner = 'Player 1'
                    self.is_won = True
                    return
                elif sum_temp == -self.win_length:
                    self.winner = 'Player 2'
                    self.is_won = True
                    return

        #Check for diagonal \\ wins containing self.last_move:
        for i in range(0,self.win_length):
            if (x-i <= self.num_cols-self.win_length and x-i >=0 and y-i <= self.num_rows - self.win_length and y-i >= 0):
                sum_temp = 0
                for k in range(0,self.win_length):
                    sum_temp += self.board_state[y-i+k][x-i+k]
                if sum_temp == self.win_length:
                    self.winner = 'Player 1'
                    self.is_won = True
                    return
                elif sum_temp == -self.win_length:
                    self.winner = 'Player 2'
                    self.is_won = True
                    return

        #Check for diagonal // wins containing self.last_move:
        for i in range(0,self.win_length):
            if (x-i <= self.num_cols-self.win_length and x-i >= 0 and y+i > self.num_rows - self.win_length and y+i <= 5):
                sum_temp = 0
                for k in range(0,self.win_length):
                    sum_temp += self.board_state[y+i-k][x-i+k]
                if sum_temp == self.win_length:
                    self.winner = 'Player 1'
                    self.is_won = True
                    return
                elif sum_temp == -self.win_length:
                    self.winner = 'Player 2'
                    self.is_won = True
                    return
