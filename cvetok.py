import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определение круга
theta = np.linspace(0, 2*np.pi, 100)
radius = 1
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)

# Определение цветка
petals = 6
angles = np.linspace(0, 2*np.pi, petals+1)
petal_length = 0.5
x_petal = []
y_petal = []

# Создание координат для каждого лепестка
for angle in angles:
    x_petal.extend([radius * np.cos(angle), (radius+petal_length) * np.cos(angle + np.pi/petals)])
    y_petal.extend([radius * np.sin(angle), (radius+petal_length) * np.sin(angle + np.pi/petals)])

# Выравнивание длины массивов круга и лепестков
max_len = max(len(x_circle), len(x_petal))
x_circle = np.pad(x_circle, (0, max_len - len(x_circle)), 'constant', constant_values=0)
y_circle = np.pad(y_circle, (0, max_len - len(y_circle)), 'constant', constant_values=0)
x_petal = np.pad(x_petal, (0, max_len - len(x_petal)), 'constant', constant_values=0)
y_petal = np.pad(y_petal, (0, max_len - len(y_petal)), 'constant', constant_values=0)

# Создание анимации
fig, ax = plt.subplots()
line_circle, = ax.plot([], [], color='blue')
line_petal, = ax.plot([], [], color='red')

def update(frame):
    t = frame / 100
    # Интерполяция координат для преобразования круга в цветок
    x_interpolated = (1 - t) * x_circle + t * x_petal
    y_interpolated = (1 - t) * y_circle + t * y_petal
    line_circle.set_data(x_interpolated, y_interpolated)
    line_petal.set_data(x_interpolated, y_interpolated)

    return line_circle, line_petal

# Установка пределов для осей и отображение анимации
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', 'box')
ax.grid(False)
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)
plt.show()
