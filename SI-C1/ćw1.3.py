import numpy as np

# Ścieżka do pliku car.txt
car_data_path = "car.txt"

# Ścieżka do pliku car-type.txt
car_type_path = "car-type.txt"

# Wczytywanie systemu decyzyjnego
with open(car_data_path, 'r') as file:
    decision_system = [line.strip().split() for line in file]

# Wczytywanie informacji o typie atrybutów
with open(car_type_path, 'r') as file:
    attribute_types = dict(line.strip().split() for line in file)

# a) Wypisanie istniejących w systemie symbole klas decyzyjnych
decision_classes = set(row[-1] for row in decision_system)
print("a) Symbole klas decyzyjnych:", decision_classes)

# b) Wielkości klas decyzyjnych (liczby obiektów w klasach)
class_sizes = {cls: sum(1 for row in decision_system if row[-1] == cls) for cls in decision_classes}
print("b) Wielkości klas decyzyjnych:", class_sizes)

# c) Minimalne i maksymalne wartości poszczególnych atrybutów (dotyczy atrybutów numerycznych)
numeric_attributes = [i for i, attr_type in enumerate(attribute_types.values()) if attr_type == 'n']
numeric_values = np.array([[float(row[i]) for i in numeric_attributes] for row in decision_system])
min_values = np.min(numeric_values, axis=0)
max_values = np.max(numeric_values, axis=0)
print("c) Minimalne wartości atrybutów numerycznych:", min_values)
print("   Maksymalne wartości atrybutów numerycznych:", max_values)

# d) Liczba różnych dostępnych wartości dla każdego atrybutu
unique_values_counts = [len(set(row[i] for row in decision_system)) for i in range(len(decision_system[0])-1)]
print("d) Liczba różnych dostępnych wartości dla każdego atrybutu:", unique_values_counts)

# e) Lista wszystkich różnych dostępnych wartości dla każdego atrybutu
unique_values_lists = [list(set(row[i] for row in decision_system)) for i in range(len(decision_system[0])-1)]
print("e) Lista wszystkich różnych dostępnych wartości dla każdego atrybutu:", unique_values_lists)

# f) Odchylenie standardowe dla poszczególnych atrybutów w całym systemie i w klasach decyzyjnych (dotyczy atrybutów numerycznych)
std_deviation_system = np.std(numeric_values, axis=0)
print("f) Odchylenie standardowe dla atrybutów numerycznych w całym systemie:", std_deviation_system)

std_deviation_classes = {cls: np.std(numeric_values[np.array([row[-1] for row in decision_system]) == cls], axis=0) for cls in decision_classes}
print("   Odchylenie standardowe dla atrybutów numerycznych w klasach decyzyjnych:", std_deviation_classes)
