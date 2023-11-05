import os
import platform
import random
import time

from pynput import keyboard
from pynput.keyboard import Key

map_height, map_width = int(input('Введите высоту поля: ')), int(input('Введите ширину поля: '))
map_ = [['_' for _ in range(map_width)] for _ in range(map_height)]
x_snake = [random.randint(0, map_width - 1)]
y_snake = [random.randint(0, map_height - 1)]
x_apple, y_apple = random.randint(0, map_width - 1), random.randint(0, map_height - 1)
vector = random.choice(['w', 'a', 's', 'd'])

for x, y in zip(x_snake, y_snake):
    map_[y][x] = '0'

map_[y_apple][x_apple] = 'A'


def print_map():
    clear_cmd = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(clear_cmd)
    for row in map_:
        print(*row)


exclude_command = {
    'w': 's',
    'a': 'd',
    's': 'w',
    'd': 'a'
}
command = {
    Key.up: 'w',
    Key.down: 's',
    Key.left: 'a',
    Key.right: 'd',
}


def on_press(key):
    global vector
    if isinstance(key, Key):
        # new_vector = command.get(key)
        # exclude_vector = exclude_command.get(vector)
        # if exclude_vector != new_vector:
        #     vector = new_vector
        new_vector = command.get(key)
        vector = new_vector if exclude_command.get(vector) != new_vector else vector
    else:
        pass
        # if key.char == 'a':


with keyboard.Listener(on_press=on_press) as listener:
    while listener.running:
        print_map()
        time.sleep(0.2)
        for x, y in zip(x_snake, y_snake):
            map_[y][x] = '_'

        for i in reversed(range(len(x_snake) - 1)):
            x_snake[i + 1] = x_snake[i]
            y_snake[i + 1] = y_snake[i]

        if vector == 'w':
            y_snake[0] = y_snake[0] - 1 if y_snake[0] != 0 else (map_height - 1)
        elif vector == 's':
            y_snake[0] = y_snake[0] + 1 if y_snake[0] != (map_height - 1) else 0
        elif vector == 'd':
            x_snake[0] = x_snake[0] + 1 if x_snake[0] != (map_width - 1) else 0
        elif vector == 'a':
            x_snake[0] = x_snake[0] - 1 if x_snake[0] != 0 else (map_width - 1)

        if x_snake[0] == x_apple and y_snake[0] == y_apple:
            # TODO спаунить яблоко нужно только там где змейки нет
            x_apple, y_apple = random.randint(0, map_width - 1), random.randint(0, map_height - 1)
            x_snake.append(x_snake[0]), y_snake.append(y_snake[0])
            map_[y_apple][x_apple] = 'A'

        # TODO проверить на столкновение с хвостом
        # TODO добавить условие победы

        for x, y in zip(x_snake, y_snake):
            map_[y][x] = '0'
