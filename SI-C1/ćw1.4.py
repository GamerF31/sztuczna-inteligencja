
import pandas as pd

# Wczytanie danych z pliku CSV
file_path = 'Churn Modelling.csv'  # Upewnij się, że podajesz poprawną ścieżkę do pliku
df = pd.read_csv(file_path)

# Wyświetlenie pierwszych kilku wierszy danych
print("Oryginalne dane:")
print(df.head())

# Konwersja atrybutu symbolicznego 'Geography' na zmienne typu dummy
df_with_dummies = pd.get_dummies(df, columns=['Geography'], drop_first=True)

# Wyświetlenie przetworzonych danych
print("\nDane po konwersji 'Geography' na zmienne typu dummy:")
print(df_with_dummies.head())

# Zapisanie przetworzonych danych do nowego pliku CSV
output_file_path = 'path/to/Churn_Modelling_with_dummies.csv'  # Upewnij się, że podajesz poprawną ścieżkę do pliku wyjściowego
df_with_dummies.to_csv(output_file_path, index=False)

print(f"\nPrzetworzone dane zostały zapisane do pliku {output_file_path}")
//