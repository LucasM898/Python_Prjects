import keyboard
x = 2
while True:
    x += x
    print(x)
    if keyboard.is_pressed('space'):
        break
print('\n')
print(x)
