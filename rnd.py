from random import randrange


#def inside(ship):


def check_ship(s, start, dirr):
    ship = []
    if dirr == 1:
        for i in range(s):
            ship.append(start - i*10)
            print(ship_start - i * 10)
    elif dirr == 2:
        for i in range(s):
            ship.append(start + i)
            print(start + i)
    elif dirr == 3:
        for i in range(s):
            ship.append(start + i*10)
            print(start - i*10)
    elif dirr == 4:
        for i in range(s):
            ship.append(start - i)
            print(start - i)


ships = [5]  #, 4, 3, 3, 2, 2]

for s in ships:
    ship_start = randrange(99)
    ship_direction = randrange(1, 4)
    print(s, ship_start, ship_direction)
    check_ship(s, ship_start, ship_direction)

