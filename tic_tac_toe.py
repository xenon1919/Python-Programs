from tkinter import *
import numpy as np

BOARD_SIZE = 600
SYMBOL_SIZE = (BOARD_SIZE / 3 - BOARD_SIZE / 8) / 2
SYMBOL_THICKNESS = 50
COLOR_X = '#EE4035'
COLOR_O = '#0492CF'
COLOR_GREEN = '#7BC043'
COLOR_BACKGROUND = '#F9F9F9'
COLOR_GRID = '#B0B0B0'
COLOR_TEXT = '#333333'

class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=BOARD_SIZE, height=BOARD_SIZE, bg=COLOR_BACKGROUND)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click_handler)

        self.setup_board()
        self.current_player_X = True
        self.board_matrix = np.zeros((3, 3))

        self.X_starts = True
        self.reset_game = False
        self.game_over = False
        self.tie_game = False
        self.X_winner = False
        self.O_winner = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def setup_board(self):
        self.canvas.create_rectangle(5, 5, BOARD_SIZE - 5, BOARD_SIZE - 5, width=5, outline=COLOR_GRID)
        for i in range(2):
            self.canvas.create_line((i + 1) * BOARD_SIZE / 3, 0, (i + 1) * BOARD_SIZE / 3, BOARD_SIZE, width=5, fill=COLOR_GRID)
            self.canvas.create_line(0, (i + 1) * BOARD_SIZE / 3, BOARD_SIZE, (i + 1) * BOARD_SIZE / 3, width=5, fill=COLOR_GRID)

    def restart_game(self):
        self.canvas.delete("all")
        self.setup_board()
        self.X_starts = not self.X_starts
        self.current_player_X = self.X_starts
        self.board_matrix = np.zeros((3, 3))

    def draw_O(self, pos):
        grid_pos = self.convert_logical_to_grid(pos)
        self.draw_heart(grid_pos[0], grid_pos[1], SYMBOL_SIZE, COLOR_O)

    def draw_X(self, pos):
        grid_pos = self.convert_logical_to_grid(pos)
        self.draw_star(grid_pos[0], grid_pos[1], SYMBOL_SIZE, COLOR_X)

    def draw_heart(self, x, y, size, color):
        self.canvas.create_polygon(
            x, y - size / 2,
            x - size / 2, y - size / 4,
            x - size / 2, y + size / 4,
            x, y + size / 2,
            x + size / 2, y + size / 4,
            x + size / 2, y - size / 4,
            x, y - size / 2,
            outline=color, fill=color, width=SYMBOL_THICKNESS // 4)

    def draw_star(self, x, y, size, color):
        self.canvas.create_polygon(
            x, y - size,
            x + size * 0.2245, y - size * 0.309,
            x + size, y - size * 0.309,
            x + size * 0.363, y + size * 0.118,
            x + size * 0.5878, y + size * 0.809,
            x, y + size * 0.38197,
            x - size * 0.5878, y + size * 0.809,
            x - size * 0.363, y + size * 0.118,
            x - size, y - size * 0.309,
            x - size * 0.2245, y - size * 0.309,
            outline=color, fill=color, width=SYMBOL_THICKNESS // 4)

    def display_winner(self):
        self.canvas.delete("all")
        self.setup_board()
        if self.X_winner:
            self.X_score += 1
            result_text = 'Winner: Player 1 (X)'
            result_color = COLOR_X
        elif self.O_winner:
            self.O_score += 1
            result_text = 'Winner: Player 2 (O)'
            result_color = COLOR_O
        else:
            self.tie_score += 1
            result_text = 'It\'s a Tie'
            result_color = 'gray'

        self.canvas.create_text(BOARD_SIZE / 2, BOARD_SIZE / 3, font="Arial 60 bold", fill=result_color, text=result_text)
        score_text = 'Scores\n'
        self.canvas.create_text(BOARD_SIZE / 2, 5 * BOARD_SIZE / 8, font="Arial 40 bold", fill=COLOR_GREEN, text=score_text)
        score_details = f'Player 1 (X): {self.X_score}\nPlayer 2 (O): {self.O_score}\nTie: {self.tie_score}'
        self.canvas.create_text(BOARD_SIZE / 2, 3 * BOARD_SIZE / 4, font="Arial 30 bold", fill=COLOR_GREEN, text=score_details)
        self.reset_game = True
        restart_text = 'Click to play again'
        self.canvas.create_text(BOARD_SIZE / 2, 15 * BOARD_SIZE / 16, font="Arial 20 bold", fill="gray", text=restart_text)

    def convert_logical_to_grid(self, logical_pos):
        return (BOARD_SIZE / 3) * np.array(logical_pos, dtype=int) + BOARD_SIZE / 6

    def convert_grid_to_logical(self, grid_pos):
        return (np.array(grid_pos) // (BOARD_SIZE / 3)).astype(int)

    def is_grid_occupied(self, logical_pos):
        return self.board_matrix[logical_pos[0], logical_pos[1]] != 0

    def check_winner(self, player):
        player_value = -1 if player == 'X' else 1

        for i in range(3):
            if np.all(self.board_matrix[i, :] == player_value) or np.all(self.board_matrix[:, i] == player_value):
                return True

        if self.board_matrix[0, 0] == self.board_matrix[1, 1] == self.board_matrix[2, 2] == player_value:
            return True
        if self.board_matrix[0, 2] == self.board_matrix[1, 1] == self.board_matrix[2, 0] == player_value:
            return True

        return False

    def check_tie(self):
        return not np.any(self.board_matrix == 0)

    def check_gameover(self):
        self.X_winner = self.check_winner('X')
        self.O_winner = not self.X_winner and self.check_winner('O')
        self.tie_game = not self.X_winner and not self.O_winner and self.check_tie()

        return self.X_winner or self.O_winner or self.tie_game

    def click_handler(self, event):
        grid_pos = [event.x, event.y]
        logical_pos = self.convert_grid_to_logical(grid_pos)

        if not self.reset_game:
            if self.current_player_X:
                if not self.is_grid_occupied(logical_pos):
                    self.draw_X(logical_pos)
                    self.board_matrix[logical_pos[0], logical_pos[1]] = -1
                    self.current_player_X = not self.current_player_X
            else:
                if not self.is_grid_occupied(logical_pos):
                    self.draw_O(logical_pos)
                    self.board_matrix[logical_pos[0], logical_pos[1]] = 1
                    self.current_player_X = not self.current_player_X

            if self.check_gameover():
                self.display_winner()
        else:
            self.canvas.delete("all")
            self.restart_game()
            self.reset_game = False

if __name__ == "__main__":
    TicTacToe().mainloop()
