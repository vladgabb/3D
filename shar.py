import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создаем фигуру
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Параметры шарика
radius = 10
center = [50, 50]
speed = 0
g = 9.8

# Функция для вычисления коэффициентов биномиального распределения
def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k+1):
        result *= (n - i + 1) / i
    return result

# Функция для расчета кривой Безье
def bezier(points, t):
    n = len(points) - 1
    result = np.zeros_like(points[0])
    for i, point in enumerate(points):
        result += binomial_coefficient(n, i) * (1 - t)**(n - i) * t**i * point
    return result

# Функция для рисования шарика на основе кривых Безье
def draw_ball(center, radius):
    t = np.linspace(0, 1, 100)
    points = np.array([[center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta)] for theta in np.linspace(0, 2 * np.pi, 4)])
    curve = np.array([bezier(points, ti) for ti in t])
    ax.plot(curve[:, 0], curve[:, 1], color='red')

# Инициализация шарика
draw_ball(center, radius)

# Функция для анимации
def animate(frame):
    global center, speed

    ax.clear()

    # Часть 1: движение
    if frame < 50:
        speed += g
        center[1] -= speed
        draw_ball(center, radius)
    # Часть 2: деформация
    elif frame < 100:
        deform_frame = frame - 50
        upper_radius = radius - deform_frame * 0.2
        lower_radius = radius - deform_frame * 0.2
        draw_ball([center[0], center[1] + radius - deform_frame * 0.1], upper_radius)
        draw_ball([center[0], center[1] - radius + deform_frame * 0.1], lower_radius)
    # Часть 3: возврат к исходной форме
    else:
        restore_frame = frame - 100
        restore_radius = restore_frame * 0.2
        draw_ball([center[0], center[1] + radius - restore_frame * 0.1], restore_radius)
        draw_ball([center[0], center[1] - radius + restore_frame * 0.1], restore_radius)

# Создание анимации
ani = FuncAnimation(fig, animate, frames=150, interval=50)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
