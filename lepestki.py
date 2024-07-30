import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Функция для построения кривой Безье по контрольным точкам
def bezier_curve(P0, P1, P2, P3, t):
    P0, P1, P2, P3 = np.array(P0), np.array(P1), np.array(P2), np.array(P3)
    return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

# Функция для вращения точки (x, y) на угол angle относительно точки (origin_x, origin_y)
def rotate_point(x, y, origin_x, origin_y, angle):
    angle_rad = np.deg2rad(angle)
    x_rotated = origin_x + (x - origin_x) * np.cos(angle_rad) - (y - origin_y) * np.sin(angle_rad)
    y_rotated = origin_y + (x - origin_x) * np.sin(angle_rad) + (y - origin_y) * np.cos(angle_rad)
    return x_rotated, y_rotated

# Функция для вращения кривой Безье
def rotate_bezier_curve(P0, P1, P2, P3, origin_x, origin_y, angle):
    rotated_P0 = rotate_point(P0[0], P0[1], origin_x, origin_y, angle)
    rotated_P1 = rotate_point(P1[0], P1[1], origin_x, origin_y, angle)
    rotated_P2 = rotate_point(P2[0], P2[1], origin_x, origin_y, angle)
    rotated_P3 = rotate_point(P3[0], P3[1], origin_x, origin_y, angle)
    return rotated_P0, rotated_P1, rotated_P2, rotated_P3

# Функция для изменения размера кривой Безье
def scale_bezier_curve(P0, P1, P2, P3, scale_factor):
    P0, P1, P2, P3 = np.array(P0), np.array(P1), np.array(P2), np.array(P3)
    scaled_P1 = ((P1[0] - P0[0]) * scale_factor + P0[0], (P1[1] - P0[1]) * scale_factor + P0[1])
    scaled_P2 = ((P2[0] - P3[0]) * scale_factor + P3[0], (P2[1] - P3[1]) * scale_factor + P3[1])
    return P0, scaled_P1, scaled_P2, P3

# Функция для рисования кривой Безье
def plot_bezier_curve(ax, P0, P1, P2, P3, color):
    t_values = np.linspace(0, 1, 100)
    x_values = np.array([bezier_curve(P0, P1, P2, P3, t)[0] for t in t_values])
    y_values = np.array([bezier_curve(P0, P1, P2, P3, t)[1] for t in t_values])
    ax.plot(x_values, y_values, color=color)

# Функция для рисования лепестка с учетом вращения и изменения размера
def plot_petal(ax, P0, P1, P2, P3, rotation_origin, rotation_angle, scale_factor, color):
    rotated_P0, rotated_P1, rotated_P2, rotated_P3 = rotate_bezier_curve(P0, P1, P2, P3, *rotation_origin, rotation_angle)
    scaled_P0, scaled_P1, scaled_P2, scaled_P3 = scale_bezier_curve(rotated_P0, rotated_P1, rotated_P2, rotated_P3, scale_factor)
    plot_bezier_curve(ax, scaled_P0, scaled_P1, scaled_P2, scaled_P3, color)

# Функция для инициализации графика
def init():
    ax.clear()
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor('green')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

# Функция для обновления графика на каждом кадре анимации
def update(frame):
    ax.clear()
    init()
    plot_petal(ax, P0, P1, P2, P3, (0, 0), frame, 1 + 0.01 * frame, 'yellow')
    plot_petal(ax, P0, P1, P2, P3, (0, 0), -frame, 1 - 0.01 * frame, 'yellow')
    plot_petal(ax, P0, P1, P2, P3, (0, 0), frame * 2, 1, 'yellow')

# Создание фигуры и осей для анимации
fig, ax = plt.subplots(figsize=(8, 6))

# Контрольные точки для лепестков
P0 = (0, 0)
P1 = (0, 10)
P2 = (10, 10)
P3 = (10, 0)

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), init_func=init, blit=False, repeat=True)

plt.show()