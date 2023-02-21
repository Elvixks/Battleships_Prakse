
def shoot(guesses):

    x = "n"
    while x == "n":
        try:
            shot = input("Your guess:")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("From 0-99 only!")
            elif shot in guesses:
                print("Already guessed!")
            else:
                x = "y"
                break
        except:
            print("Try again!")
    return shot
def board(hit, miss, sink):
    print("Battleships")
    print("X    A  B  C  D  E  F  G  H  I  J")

    tile = 0
    for x in range(10):
        row = ""
        for y in range(10):
            sym = " . "
            if tile in miss:
                sym = " X "
            elif tile in hit:
                sym = " o "
            elif tile in sink:
                sym = " 0 "

            row = row + sym
            tile = tile + 1
        print(x," ",row)

def check(shot, ship1, ship2, hit, miss, sink ):
    if shot in ship1:
        ship1.remove(shot)
        if len(ship1) > 0:
            hit.append(shot)
        else:
            sink.append(shot)
    elif shot in ship2:
        ship2.remove(shot)
        if len(ship2) > 0:
            hit.append(shot)
        else:
            sink.append(shot)
    else:
        miss.append(shot)




    return ship1, ship2, hit, miss, sink

ship1 = [45, 46, 47]
ship2 = [75,76,77]
ship3 = []
ship4 = []
ship5 = []

hit = []
miss = []
sink = []

for i in range(10):

    guesses = hit + miss + sink
    shot = shoot(guesses)
    ship1, ship2, hit, miss, sink = check(shot, ship1, ship2, hit, miss, sink)
    board(hit, miss, sink)

    if len(ship1) < 1 and len(ship2) < 1:
        print("Victory")
        break
print("Game over")

