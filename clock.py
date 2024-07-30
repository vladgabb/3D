import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_bezier_curve(P0, P1, P2, P3, color):
    t_values = np.linspace(0, 1, 100)
    x_values = np.array([bezier_curve(P0[0], P1[0], P2[0], P3[0], t) for t in t_values])
    y_values = np.array([bezier_curve(P0[1], P1[1], P2[1], P3[1], t) for t in t_values])
    plt.plot(x_values, y_values, color=color)

def bezier_curve(p0, p1, p2, p3, t):
    return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

def update(frame):
    plt.cla()
    t = frame / 100
    # Исходные координаты прямоугольника
    rectangle = np.array([(-3, -1), (-3, 1), (3, 1), (3, -1), (-3, -1)])
    # Координаты кривой Безье, которая будет превращать прямоугольник в песочные часы
    curve = np.array([(-3, -1), (-1, 3), (1, 3), (3, -1)])

    # Интерполируем точки прямоугольника и кривой Безье
    interpolated_rectangle = [(1 - t) * rectangle[i] + t * rectangle[i + 1] for i in range(len(rectangle) - 1)]
    interpolated_curve = [(1 - t) * curve[i] + t * curve[i + 1] for i in range(len(curve) - 1)]

    # Рисуем прямоугольник и кривую Безье
    plt.plot([point[0] for point in interpolated_rectangle], [point[1] for point in interpolated_rectangle], color='brown')
    plot_bezier_curve(curve[0], curve[1], curve[2], curve[3], 'brown')

    plt.axis('equal')
    plt.axis('off')

fig = plt.figure(figsize=(6, 6))
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
