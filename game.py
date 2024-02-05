import numpy as np

class TicTacToe:

    def __init__(self):
        self.board = np.full((3, 3), "-")

    def winner(self, board):
        for row in board:
            if np.all(row == row[0]) and row[0] != '-':
                return True

        for col in range(len(board)):
            if np.all(board[:, col] == board[0, col]) and board[0, col] != '-':
                return True

        if np.all(np.diagonal(board) == board[0, 0]) and board[0, 0] != '-':
            return True

        if np.all(np.diagonal(np.fliplr(board)) == board[0, -1]) and board[0, -1] != '-':
            return True

        return False
    
    def full(self, board):
        return np.all(board != '-')
    
    def evaluate(self, board):
        pass

    def minimax(self, position, depth, alpha, beta, maximizing):
        if depth == 0 or self.winner(position) == True or self.full(position) == True:
            return self.evaluate(position)
    

