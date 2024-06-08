import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dane: rok i odpowiedni procent bezrobocia
years = np.array([2000, 2002, 2005, 2007, 2010]).reshape(-1, 1)
unemployment = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

# Tworzenie modelu regresji liniowej
model = LinearRegression()
model.fit(years, unemployment)

# Wydruk współczynników modelu
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Przewidywanie roku, w którym bezrobocie przekroczy 12%
target_unemployment = 12
year_when_exceeds_12 = (target_unemployment - model.intercept_) / model.coef_[0]
print("Year when unemployment exceeds 12%:", year_when_exceeds_12)

# Animacja procesu regresji liniowej
# Punkt startowy m i b
m_start = 0
b_start = 0

# Ustalenie parametrów nauki
learning_rate = 0.0001
num_iterations = 100

# Wartości m i b do animacji
ms = [m_start]
bs = [b_start]

# Funkcja do obliczania MSE i gradientów
def compute_gradient(m, b, X, Y):
    n = len(Y)
    Y_pred = m * X.flatten() + b
    dJ_dm = (-2/n) * sum(X.flatten() * (Y - Y_pred))
    dJ_db = (-2/n) * sum(Y - Y_pred)
    return dJ_dm, dJ_db

# Symulacja procesu uczenia
current_m, current_b = m_start, b_start
for _ in range(num_iterations):
    dJ_dm, dJ_db = compute_gradient(current_m, current_b, years, unemployment)
    current_m -= learning_rate * dJ_dm
    current_b -= learning_rate * dJ_db
    ms.append(current_m)
    bs.append(current_b)

# Przygotowanie animacji
fig, ax = plt.subplots()
ax.scatter(years, unemployment, color='red')
line, = ax.plot(years, ms[0] * years + bs[0], 'b-')

def update(frame):
    m = ms[frame]
    b = bs[frame]
    line.set_ydata(m * years.flatten() + b)
    return line,

ani = FuncAnimation(fig, update, frames=num_iterations, blit=True, repeat=False)
plt.show()
