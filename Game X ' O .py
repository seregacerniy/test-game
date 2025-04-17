def greetings():
    print("---------------------")
    print("Вас приветствует игра")
    print("   Крестики Нолики")
    print(" введите координаты:")
    print("---------------------")

field = [[""] * 3 for i in range(3)]
def matrix_():
    print()
    print(f"     |0 | 1| 2|")
    print("  --------------")
    for i, row in enumerate(field):
        row_str = f"  {i}  | {' | '.join(row)} |"
        print(row_str)
        print("  --------------")
    print()
matrix_()
def step_():
    while True:
        cords = input("Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите два числа !")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа !")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("координаты вне диапазона!")
            continue
        if field[x][y] != "":
            print("Клетка занята !")
            continue

        return x,y

def chec_win():
    win_cord = [((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
            ((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),
            ((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["x","x","x"]:
            print("Выйграл Х !!!!")
            return True
        if symbols == ["0","0","0"]:
            print("Выйграл 0 !!!!")
            return True
    return False
greetings()
num_step = 0
while True:
    num_step += 1
    matrix_()
    if num_step % 2 == 1:
        print("ходит крестик")
    else:
        print("ходит нолик")

    X, Y = step_()

    if num_step % 2 == 1:
        field[X][Y] = "x"
    else:
        field[X][Y] = "o"

    if chec_win():
        break

    if num_step == 9:
        print("ничья")
        break






