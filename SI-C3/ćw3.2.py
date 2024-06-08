# Definicja funkcji sprawdzającej ograniczenia
def check_constraints(X1, X2, X3):
    # Sprawdzenie ograniczenia X1 < X2 i X2 < X3
    if X1 >= X2 or X2 >= X3:
        return False
    return True


# Funkcja znajdująca zmienną z minimalną liczbą pozostałych wartości
def find_variable_with_min_remaining_values(assigned_variables, domains):
    min_remaining_values = float('inf')
    variable_with_min_remaining_values = None
    for variable in domains.keys():
        if variable not in assigned_variables:
            remaining_values = len(domains[variable])
            if remaining_values < min_remaining_values:
                min_remaining_values = remaining_values
                variable_with_min_remaining_values = variable
    return variable_with_min_remaining_values


# Rekurencyjna funkcja przypisująca wartości do zmiennych
def assign_values(assigned_variables, assigned_values, domains):
    if len(assigned_variables) == len(domains):
        print("Znalezione rozwiązanie:", assigned_values)
        return

    variable = find_variable_with_min_remaining_values(assigned_variables, domains)
    for value in domains[variable]:
        if value not in assigned_values.values():
            assigned_variables.append(variable)
            assigned_values[variable] = value

            # Sprawdzenie ograniczeń dla danej kombinacji wartości
            X1 = assigned_values.get('X1', None)
            X2 = assigned_values.get('X2', None)
            X3 = assigned_values.get('X3', None)
            if X1 is not None and X2 is not None and X3 is not None and not check_constraints(X1, X2, X3):
                assigned_variables.pop()
                del assigned_values[variable]
                continue

            assign_values(assigned_variables, assigned_values, domains)

            assigned_variables.pop()
            del assigned_values[variable]


# Definicja dziedzin dla każdej zmiennej
domains = {
    'X1': [1, 2, 3],
    'X2': [2, 3, 4],
    'X3': [3, 4, 5]
}

# Wywołanie rekurencyjnej funkcji przypisującej wartości do zmiennych
assign_values([], {}, domains)
