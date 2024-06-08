def evaluate_expression(expr, assignment):
    # Funkcja ocenia wartość logiczną wyrażenia na podstawie przypisania
    if expr in assignment:
        return assignment[expr]
    if isinstance(expr, tuple):
        operator = expr[0]
        if operator == 'NOT':
            return not evaluate_expression(expr[1], assignment)
        elif operator == 'AND':
            return evaluate_expression(expr[1], assignment) and evaluate_expression(expr[2], assignment)
        elif operator == 'OR':
            return evaluate_expression(expr[1], assignment) or evaluate_expression(expr[2], assignment)
    return None

def pl_true(S, m):
    return evaluate_expression(S, m)

# Przykładowe zdanie S i przypisanie m
S = ('AND', ('NOT', 'p'), ('OR', 'q', 'r'))
m = {'p': 0, 'q': 1, 'r': 0}

# Sprawdzenie, czy zdanie S jest prawdziwe w przypisaniu m
result = pl_true(S, m)
print(f"Zdanie S jest {'prawdziwe' if result else 'fałszywe'} w przypisaniu m")
