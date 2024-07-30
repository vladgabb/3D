import matplotlib.pyplot as plt
import numpy as np

def draw_bezier_curve(points, n_points=100):
    t = np.linspace(0, 1, n_points)
    n = len(points) - 1
    curve = np.zeros((n_points, 2))
    for i in range(n + 1):
        curve += np.outer(np.power(1 - t, n - i) * np.power(t, i), points[i])
    return curve

def bezier(points):
    curve = draw_bezier_curve(points)
    plt.plot(curve[:, 0], curve[:, 1], color='blue')

def interpolate_color(start_color, end_color, t):
    r = int(start_color[0] + (end_color[0] - start_color[0]) * t)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * t)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * t)
    return (r, g, b)

def draw_snail():
    num_points = 50
    radius = 10
    points = []

    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = (radius - 0.1 * i) * np.cos(angle)
        y = (radius - 0.1 * i) * np.sin(angle)
        points.append((x, y))

    # Создаем массивы координат X и Y из списка точек
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    for i in range(num_points - 1):
        color = interpolate_color((255, 0, 0), (0, 0, 0), i / (num_points - 1))
        plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], color='#%02x%02x%02x' % color)
        draw_bresenham_line(int(points[i][0]), int(points[i][1]), int(points[i+1][0]), int(points[i+1][1]))

    color = interpolate_color((255, 0, 0), (0, 0, 0), 1)
    plt.plot([points[-1][0], points[0][0]], [points[-1][1], points[0][1]], color='#%02x%02x%02x' % color)
    draw_bresenham_line(int(points[-1][0]), int(points[-1][1]), int(points[0][0]), int(points[0][1]))

    bezier(points)

    # Создаем кривую Безье
    curve = draw_bezier_curve(points)

    # Закрашиваем внутренность улитки
    plt.fill(curve[:, 0], curve[:, 1], color='red')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def draw_bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x0 != x1:
            plt.plot(x0, y0, 'ro')
            err -= dy
            if err < 0:
                y0 += sy
                err += dx
            x0 += sx
    else:
        err = dy / 2.0
        while y0 != y1:
            plt.plot(x0, y0, 'ro')
            err -= dx
            if err < 0:
                x0 += sx
                err += dy
            y0 += sy
    plt.plot(x0, y0, 'ro')

draw_snail()
