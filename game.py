import numpy as np

class TicTacToe:

    def __init__(self):
        self.board = np.full((3, 3), "-")

    def player_move(self, board, move='X'):
        while True:
            position = input("Enter your move (row, col): ").split()
            if int(position[0]) <= 3 and int(position[1]) <= 3:
                if board[int(position[0]) - 1, int(position[1]) - 1] == '-':
                    board[int(position[0]) - 1, int(position[1]) - 1] = move
                    break


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
            #print(board, self.evaluate(board, depth, maximizing), self.winner(board), maximizing, end='\n\n')
            return self.evaluate(board, not maximizing)

        if maximizing:
            maxEval = float('-inf')

            for possibility in self.generate_possible_moves(board, player = "O"):
                #print(possibility, self.winner(possibility), self.evaluate(possibility, depth, maximizing=True), end='\n\n')
                eval = self.minimax(possibility, depth - 1, alpha, beta, maximizing=False)
                maxEval = max(eval, maxEval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

            return maxEval
        
        else:
            minEval = float('inf')
            
            for possibility in self.generate_possible_moves(board, player = "X"):
                #print(possibility, self.winner(possibility), self.evaluate(possibility, depth, maximizing=False), end='\n\n')
                eval = self.minimax(possibility, depth - 1, alpha, beta, maximizing=True)
                minEval = min(eval, minEval)
                alpha = min(alpha, eval)

                if beta <= alpha:
                    break

            return minEval
    
    def play(self):
        print(self.board)
        while self.winner(self.board) == False or not self.full(self.board) == False:

            self.player_move(self.board)
            print(self.board)

            scores = []
            moves = []

            for move in self.generate_possible_moves(self.board, "O"):
                score = self.minimax(move, 10, float("-inf"), float("inf"), False)
                scores.append(score)
                moves.append(move)

            best_move = moves[np.argmax(scores)]
            self.board = best_move

            print(f"BOT's move: {scores}")
            print(self.board)


        print("Gameover!")



            
game = TicTacToe()
game.play()
