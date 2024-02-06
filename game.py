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
    
    def evaluate(self, board, maximizing):
        if self.winner(board):
            if maximizing == True:
                return 1
            return -1

        elif self.full(board):
            return 0

    def generate_possible_moves(self, board, player):
        possible_moves = []

        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    newboard = np.copy(board)
                    newboard[row, col] = player
                    possible_moves.append(newboard)
        return possible_moves

    def minimax(self, board, depth, alpha, beta, maximizing):
        if depth == 0 or self.winner(board) == True or self.full(board) == True:
            return self.evaluate(board, maximizing)

        if maximizing:
            maxEval = float('-inf')

            for possibility in self.generate_possible_moves(board, player = "X"):
                eval = self.minimax(possibility, depth - 1, alpha, beta, maximizing=False)
                maxEval = max(eval, maxEval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

            return maxEval
        
        else:
            minEval = float('inf')
            
            for possibility in self.generate_possible_moves(board, player = "O"):
                eval = self.minimax(possibility, depth - 1, alpha, beta, maximizing=True)
                minEval = min(eval, maxEval)
                alpha = min(alpha, eval)

                if beta <= alpha:
                    break

            return minEval

            

