from collections import deque

def is_goal(state):
    return state['A'] == 'clean' and state['B'] == 'clean'

def get_successors(state):
    successors = []
    if state['location'] == 'A':
        successors.append(('right', {'location': 'B', 'A': state['A'], 'B': state['B']}))
    if state['location'] == 'B':
        successors.append(('left', {'location': 'A', 'A': state['A'], 'B': state['B']}))
    if state[state['location']] == 'dirty':
        new_state = state.copy()
        new_state[state['location']] = 'clean'
        successors.append(('suck', new_state))
    return successors

def bfs(initial_state):
    frontier = deque([(initial_state, [])])
    explored = set()

    while frontier:
        state, path = frontier.popleft()
        if is_goal(state):
            return path
        explored.add((state['location'], state['A'], state['B']))
        for action, next_state in get_successors(state):
            if (next_state['location'], next_state['A'], next_state['B']) not in explored:
                frontier.append((next_state, path + [action]))

initial_state = {'location': 'A', 'A': 'dirty', 'B': 'dirty'}
solution = bfs(initial_state)
print("Sequence of actions to reach the goal:", solution)
