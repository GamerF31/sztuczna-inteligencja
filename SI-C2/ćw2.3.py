class Game:
    def __init__(self, values):
        self.values = values  # Lista wartości końcowych
        self.nodes = ['MAX', 'MIN', 'MIN', 'MAX', 'MAX', 'MAX', 'MAX', None, None, None, None, None, None, None, None]  # Struktura drzewa

    def minimax(self, depth, node_index, maximizing_player, alpha, beta):
        if depth == 3:
            return self.values[node_index]

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(2):
                eval = self.minimax(depth + 1, node_index * 2 + i, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(2):
                eval = self.minimax(depth + 1, node_index * 2 + i, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self):
        best_val = self.minimax(0, 0, True, float('-inf'), float('inf'))
        return best_val

# Wartości końcowe w liściach drzewa
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Inicjalizacja gry
game = Game(values)

# Znalezienie optymalnej strategii dla gracza MAX
best_value = game.find_best_move()
print(f"Optimal value for MAX: {best_value}")
