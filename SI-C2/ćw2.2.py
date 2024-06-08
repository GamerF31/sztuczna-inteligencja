import heapq

class PuzzleState:
    def __init__(self, board, g=0, h=0, parent=None, move=None):
        self.board = board
        self.g = g  # cost to reach this state
        self.h = h  # heuristic cost to reach goal from this state
        self.parent = parent
        self.move = move

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def get_empty_pos(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j

    def get_possible_moves(self):
        empty_x, empty_y = self.get_empty_pos()
        moves = []
        if empty_x > 0:  # Move empty space up
            moves.append('up')
        if empty_x < 2:  # Move empty space down
            moves.append('down')
        if empty_y > 0:  # Move empty space left
            moves.append('left')
        if empty_y < 2:  # Move empty space right
            moves.append('right')
        return moves

    def generate_child(self, move):
        x, y = self.get_empty_pos()
        new_board = [row[:] for row in self.board]
        if move == 'up':
            new_board[x][y], new_board[x-1][y] = new_board[x-1][y], new_board[x][y]
        elif move == 'down':
            new_board[x][y], new_board[x+1][y] = new_board[x+1][y], new_board[x][y]
        elif move == 'left':
            new_board[x][y], new_board[x][y-1] = new_board[x][y-1], new_board[x][y]
        elif move == 'right':
            new_board[x][y], new_board[x][y+1] = new_board[x][y+1], new_board[x][y]
        return PuzzleState(new_board, self.g + 1, parent=self, move=move)

def heuristic(state, goal):
    # Manhattan distance heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0:
                x, y = divmod(state.board[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def a_star_search(start, goal):
    start_state = PuzzleState(start, h=heuristic(PuzzleState(start), goal))
    goal_state = PuzzleState(goal)
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state == goal_state:
            path = []
            while current_state.parent is not None:
                path.append(current_state.move)
                current_state = current_state.parent
            return path[::-1]  # Return reversed path

        closed_list.add(current_state)

        for move in current_state.get_possible_moves():
            child_state = current_state.generate_child(move)
            if child_state in closed_list:
                continue

            child_state.h = heuristic(child_state, goal)
            heapq.heappush(open_list, child_state)

    return None

# Definicja stanu początkowego i stanu docelowego
start = [
    [0, 1, 3],
    [4, 2, 5],
    [7, 8, 6]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Przeszukiwanie A*
path = a_star_search(start, goal)
print("Ścieżka do osiągnięcia celu:", path)
