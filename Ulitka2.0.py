import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(50000)

def create_image(heigh, widht, background_color):
    img = np.ones((heigh, widht, 3), np.uint8)
    img[:, :, :3] = background_color
    return img

def set_color(img, x, y, color):
    img[x, y, :3] = color
    return img

def draw_line(img, x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    
    sign_x = 1 if dx>0 else -1 if dx<0 else 0
    sign_y = 1 if dy>0 else -1 if dy<0 else 0
    
    dx, dy = abs(dx), abs(dy)
    
    if dx > dy:
        step_x, step_y = sign_x, 0
        height, length = dy, dx
    else:
        step_x, step_y = 0, sign_y
        height, length = dx, dy
    
    x, y = x1, y1
    
    error, steps = length/2, 0
    
    img = set_color(img, int(x), int(y), color)
    
    while steps < length:
        error -= height
        if error < 0:
            error += length
            x += sign_x
            y += sign_y
        else:
            x += step_x
            y += step_y
        steps += 1
        img = set_color(img, int(x), int(y), color)
    return img

def fill_area(img, x, y, color, bg):
    if (False not in np.equal(img[x][y], bg)):
        img = set_color(img, x, y, color)
    if (False not in np.equal(img[x-1][y], bg)):
        img = fill_area(img, x-1, y, color, bg)
    if (False not in np.equal(img[x][y-1], bg)):
        img = fill_area(img, x, y-1, color, bg)
    if (False not in np.equal(img[x+1][y], bg)):
        img = fill_area(img, x+1, y, color, bg)
    if (False not in np.equal(img[x][y+1], bg)):
        img = fill_area(img, x, y+1, color, bg)
    return img

center = 512
x = 512
y = 512
d = 10
n = 0
img = create_image(1024, 1024, np.array([255, 255, 255], dtype=np.uint8))
red = np.array([255, 0, 0], dtype=np.uint8)

while n < 50:
    for i in range(1, 5):
        if (i == 1):
            draw_line(img, x, y, x+d, y, red)
            x += d
        if (i == 2):
            draw_line(img, x, y, x, y+d, red)
            y += d
        if (i == 3):
            draw_line(img, x, y, x-d, y, red)
            x -= d
        if (i == 4):
            draw_line(img, x, y, x, y-d, red)
            y -= d
        d += 5
        n += 1
        if (n >= 50): break

draw_line(img, x, y, int(x-d/2), y, red)
x = int(x-d/2)
draw_line(img, x, y, center, center, red)

for i in range(center, int(center+d/2)):
    fill_area(img, i, 513, np.array([0, 255, 0], dtype=np.uint8), np.array([255, 255, 255], dtype=np.uint8))

plt.figure()
img = img.transpose([1, 0, 2])
plt.imshow(img)
plt.show()