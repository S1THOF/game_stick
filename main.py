#  designed by S1THOF

def input_stat():
    name_first_player, name_second_player = input("Введите имя первого игрока: "), input("Введите имя второго игрока: ")
    stick_count = input("Введите кол-во палочек:")
    while int(stick_count) < 5:
        stick_count = input("Введите кол-во палочек (не меньше 5 штук): ")
    while True:
        if stick_count.isdigit():
            print("Итак", name_first_player, "Вы будете ходить первым, а", name_second_player, "вторым.",
                  "Играть будем с", stick_count, "палочками")
            break
        else:
            stick_count = input("Введите кол-во палочек: ")
    step_game(name_first_player, name_second_player, stick_count)


def step_game(name_first_player, name_second_player, stick_count):
    count_round = 1
    while int(stick_count) != 0:
        take_count = int(input("Берите палочки(не больше 3 штук): "))
        if 0 < take_count <= 3:
            stick_count = int(stick_count) - int(take_count)
            if count_round % 2 != 0:
                print(name_first_player, "взял", take_count, "шт. и в банке осталось", int(stick_count))
                count_round += 1
            else:
                print(name_second_player, "взял", take_count, "шт. и в банке осталось", int(stick_count))
                count_round += 1
        else:
            take_count = int(input("Берите палочки(не больше 3 штук): "))
        if int(stick_count) <= 0:
            if count_round % 2 != 0:
                print("Поздравляю с победой", name_first_player, ", игра завершилась через", count_round, "раундов!")
                while True:
                    restart = input("Начнем еще раз? (y/n): ")
                    if restart.lower() == "y":
                        input_stat()
                    elif restart.lower() == "n":
                        break

print("Добро пожаловать в игру 'Палочки'!")
input_stat()

