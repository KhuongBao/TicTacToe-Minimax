import numpy as np
from random import randint

class TicTacToe:

    def __init__(self, player):
        if player != "X" and player != "O":
            raise ValueError("Player can only be 'X' or 'O'")

        self.board = np.full((3, 3), "-")
        self.player = player
        self.com = "O" if self.player == "X" else "X"

        

    def player_move(self, board, move):
        while True:
            position = input("Enter your move (row, col): ").split()

            if len(position) == 2 and all(value.isdigit() for value in position):
                if int(position[0]) <= 3 and int(position[1]) <= 3:
                    if board[int(position[0]) - 1, int(position[1]) - 1] == '-':
                        board[int(position[0]) - 1, int(position[1]) - 1] = move
                        break
                    else:
                        print("Invalid move")
                else:
                    print("Invalid position")
            else:
                print("Invalid input")



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
            return self.evaluate(board, not maximizing)

        if maximizing:
            maxEval = float('-inf')

            for possibility in self.generate_possible_moves(board, self.com):
                eval = self.minimax(possibility, depth - 1, alpha, beta, maximizing=False)
                maxEval = max(eval, maxEval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

            return maxEval
        
        else:
            minEval = float('inf')
            
            for possibility in self.generate_possible_moves(board, self.player):
                eval = self.minimax(possibility, depth - 1, alpha, beta, maximizing=True)
                minEval = min(eval, minEval)
                alpha = min(alpha, eval)

                if beta <= alpha:
                    break

            return minEval
#your mom fat
=======
    def play(self):

        if self.com == "X":
            self.board[randint(0, 2)][randint(0, 2)] = self.com

        print(self.board)

        last_move = ''
        while not self.winner(self.board):
            if not self.full(self.board):
                self.player_move(self.board, self.player)
                print(self.board)
                last_move = 'Player'
            else: 
                break

            if not self.full(self.board):
                scores = []
                moves = []
                for move in self.generate_possible_moves(self.board, self.com):
                    score = self.minimax(move, 10, float("-inf"), float("inf"), False)
                    scores.append(score)
                    moves.append(move)

                best_move = moves[np.argmax(scores)]
                self.board = best_move

                print(f"COM's move: {scores}")
                print(self.board)
                last_move = 'COM'
            else:
                break
        
        if self.winner(self.board):
            print(f"Gameover! {last_move} wins!")
        else:
            print("Gameover! It's a tie!")
        
        replay = input("Play again? Yes or No: ").lower()
        while True:
            if replay == "yes":
                self.__init__(self.player)
                self.play()
                break
            elif replay == "no":
                print("Thanks for playing!")
                break

            
game = TicTacToe(player="X")
game.play()
