# Definicja funkcji sprawdzającej ograniczenia
def check_constraints(X1, X2, X3):
    # Sprawdzenie ograniczenia X1 < X2 i X2 < X3
    if X1 >= X2 or X2 >= X3:
        return False
    return True

# Pętla po wszystkich możliwych wartościach X1, X2, X3
for X1 in range(1, 4):
    for X2 in range(2, 5):
        for X3 in range(3, 6):
            # Sprawdzenie ograniczeń dla danej kombinacji wartości
            if check_constraints(X1, X2, X3):
                print("Znalezione rozwiązanie: X1 =", X1, ", X2 =", X2, ", X3 =", X3)
