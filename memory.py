"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
#Replace 32 numbers for 32 emojis
emojis = ['🍎', '🍌', '🍉', '🍇', '🍒', '🍓', '🥝', '🥕', '🌽', '🍕',
          '🍔', '🍩', '🎈', '🚗', '🚌', '🚀', '🐶', '🐱', '🐭', '🐹', '⚓️',
          '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐸', '🐵']

#duplicate the emoji list
tiles = emojis * 2

state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# variable para guardar los taps
taps =0
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # mientras todos estén destapados
    if all(not h for h in hide):
        goto(-100, 0)
        color('green')
        write("Yei, ganaste!", font=('Arial', 30, 'bold'))
        update()
        return

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Remove offset logic
        goto(x + 15, y + 10)
        color('black')
        #Reduce the size of the font
        write(tiles[mark], font=('Arial', 20, 'normal'))
    
    # se muestran los taps en la pantalla
    goto(-180, 150)
    write(f"Taps: {taps}", font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
