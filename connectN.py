import numpy as np

#Create a class defining an instance of a Connect Four board.

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
        self.turn = 1
        self.is_won = False

    def play_chip(self, column):
        #First check if the game is over:
        if self.is_won == True:
            print('The game is over; %s has won.' % self.winner)
        else:
            #Player whose turn it is places a chip in column
            #Determine whose turn it is:
            if self.turn % 2 == 1:
                chip = 1
            else:
                chip = -1
            #Determine the legal moves in the board_state:
            self.legal_moves = np.where(self.board_state[0]==0)[0]

            #If suggested move is legal, play the chip in column and go to next turn.
            if column in self.legal_moves:
                self.board_state[np.amax(np.where(self.board_state[:,column] == 0)),column] = chip
                self.turn += 1
            else:
                print('Column is full; please suggest another move.')

    def check_win(self):
        #Checks for a winning position for both players.
        #Check for row wins
        for i in range(self.num_rows-1,-1,-1):
            #Check if row is empty
            if any(self.board_state[i,:] != 0):
                #Check if row has enough chips for a win
                if (len(np.where(self.board_state[i,:] != 0)[0]) >= self.win_length):
                    for j in range(np.amin(np.where(self.board_state[i,:] != 0)[0]),np.amax(np.where(self.board_state[i,:] != 0)[0])+self.win_length):
                        if all(self.board_state[i,j:j+self.win_length] == 1):
                            self.winner = 'Player 1'
                            self.is_won = True
                            return
                        elif all(self.board_state[i,j:j+self.win_length] == -1):
                            self.winner = 'Player 2'
                            self.is_won = True
                            return
                else:
                    #If a row doesn't have enough chips to win, no row above it can, either
                    break
            else:
                break


        #Check for column wins
        for j in range(0,self.num_cols):
            #Check if column is empty
            if any(self.board_state[:,j] != 0):
                #Check if column has enough chips for a win
                if (len(np.where(self.board_state[:,j] != 0)[0]) >= self.win_length):
                    #Check for win starting at top chip (no need to look below; else game was already over.)
                    if all(x in self.board_state[np.amin(np.where(self.board_state[:,j] != 0)):np.amin(np.where(self.board_state[:,j] != 0))+self.win_length,j] == 1):
                        self.winner = 'Player 1'
                        self.is_won = True
                        return
                    elif all(x in self.board_state[np.amin(np.where(self.board_state[:,j] != 0)):np.amin(np.where(self.board_state[:,j] != 0))+self.win_length,j] == -1):
                        self.winner = 'Player 2'
                        self.is_won = True
                        return

        #Check if up-right diagonal wins are possible:

        for i in range(np.amin(np.where(self.board_state !=0)[0]),self.num_rows - self.win_length + 1):
            for j in range(0,num_cols - win_length + 1):
                diag_temp_prod = 1
                for k in range(0,win_length):
                    diag_temp_prod = diag_temp_prod*matrix[i+k][j+k]
                if (diag_temp_prod > diag_max_prod_down):
                    diag_max_prod_down = diag_temp_prod

        #Compute maximum of diagonal (down-left) products

        for i in range(0,num_rows - win_length + 1):
            for j in range(win_length - 1,num_cols):
                diag_temp_prod = 1
                for k in range(0,win_length):
                    diag_temp_prod = diag_temp_prod*matrix[i+k][j-k]
                if (diag_temp_prod > diag_max_prod_up):
                    diag_max_prod_up = diag_temp_prod
