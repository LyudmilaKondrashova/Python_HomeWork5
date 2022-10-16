#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def DelABV():
    stroka = input('Введите строку:\n')
    new_str = [word for word in stroka.split() if 'абв' not in word]
    print(f'Новая строка: {" ".join(new_str)}')

#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока,
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты
# у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"

def ManMan(count):
    import random

    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    first = random.randint(1,2)
    if first == 2:
        player1, player2 = player2, player1
    print(f'В результате жеребьевки первым будет ходить игрок {player1}')

    step = 1
    winner = player1
    fl1 = True
    fl2 = True
    while count > 0:
        if fl1 and fl2:
            print(f'ШАГ №{step}: ')
        if fl1:
            candy_choise = int(input(f'Ход игрока {player1}: '))
            if  1 <= candy_choise <= 28:
                if count >= 28:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player1
                    fl1 = False
                elif count <= 28 and candy_choise <= count:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player1
                    fl1 = False
                elif count < 28 and candy_choise > count:
                    print('Введено конфет больше, чем осталось! Попробуйте еще раз!')
                    fl1 = True
            else:
                print('Можно забирать от 1 до 28 конфет! Попробуйте еще раз!')
                fl1 = True
        if not fl1 and fl2:
            if count > 0:
                candy_choise = int(input(f'Ход игрока {player2}: '))
                if  1 <= candy_choise <= 28:
                    if count >= 28:
                        count -= candy_choise
                        print(f'Осталось {count} конфет')
                        winner = player2
                        fl2 = False
                    elif count <= 28 and candy_choise <= count:
                        count -= candy_choise
                        print(f'Осталось {count} конфет')
                        winner = player2
                        fl2 = False
                    elif count < 28 and candy_choise > count:
                        print('Введено конфет больше, чем осталось! Попробуйте еще раз!')
                        fl2 = True
                else:
                    print('Можно забирать от 1 до 28 конфет! Попробуйте еще раз!')
                    fl2 = True
        if not fl1 and not fl2:
            step += 1
            fl1 = True
            fl2 = True
    print(f'Победитель игрок {winner}! Поздравляем!')

def ManBot(count):
    import random

    player1 = input('Введите имя игрока: ')
    player2 = 'BOT'
    first = random.randint(1,2)
    fl1 = True
    fl2 = True
    if first == 1:
        print(f'В результате жеребьевки первым будет ходить игрок {player1}')
    else:
        print(f'В результате жеребьевки первым будет ходить игрок {player2}')
        fl1 = False
        print('ШАГ №1: ')
    step = 1
    winner = player2
    while count > 0:
        if fl1 and fl2:
            print(f'ШАГ №{step}: ')
        if fl1:
            candy_choise = int(input(f'Ход игрока {player1}: '))
            if  1 <= candy_choise <= 28:
                if count >= 28:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player1
                    fl1 = False
                elif count <= 28 and candy_choise <= count:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player1
                    fl1 = False
                elif count < 28 and candy_choise > count:
                    print('Введено конфет больше, чем осталось! Попробуйте еще раз!')
                    fl1 = True
            else:
                print('Можно забирать от 1 до 28 конфет! Попробуйте еще раз!')
                fl1 = True
        if not fl1 and fl2:
            if count > 0:
                candy_choise = random.randint(1, 28)
                print(f'Ход игрока {player2}: {candy_choise}')
                if count >= 28:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player2
                    fl2 = False
                elif count <= 28 and candy_choise <= count:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player2
                    fl2 = False
                elif count < 28 and candy_choise > count:
                    print('Введено конфет больше, чем осталось! Попробуйте еще раз!')
                    fl2 = True
        if not fl1 and not fl2:
            step += 1
            fl1 = True
            fl2 = True
    print(f'Победитель игрок {winner}! Поздравляем!')


def ManBotIntellect(count):
    import random

    player1 = input('Введите имя игрока: ')
    player2 = 'BOT Intellectual'
    first = random.randint(1,2)
    print(f'Первым будет ходить игрок {player2}')
    fl1 = False
    fl2 = True
    print('ШАГ №1: ')
    step = 1
    winner = player1
    while count > 0:
        if fl1 and fl2:
            print(f'ШАГ №{step}: ')
        if fl1:
            candy_choise = int(input(f'Ход игрока {player1}: '))
            if  1 <= candy_choise <= 28:
                if count >= 28:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player1
                    fl1 = False
                elif count <= 28 and candy_choise <= count:
                    count -= candy_choise
                    print(f'Осталось {count} конфет')
                    winner = player1
                    fl1 = False
                elif count < 28 and candy_choise > count:
                    print('Введено конфет больше, чем осталось! Попробуйте еще раз!')
                    fl1 = True
            else:
                print('Можно забирать от 1 до 28 конфет! Попробуйте еще раз!')
                fl1 = True
        if not fl1 and fl2:
            if count == 2021:
                candy_choise_bot = 20
                print(f'Ход игрока {player2}: {candy_choise_bot}')
                count -= candy_choise_bot
                print(f'Осталось {count} конфет')
                winner = player2
                fl2 = False
            elif count > 0:
                if count < 28:
                    candy_choise_bot = count
                    count -= candy_choise_bot
                    print(f'Ход игрока {player2}: {candy_choise_bot}')
                    winner = player2
                    fl2 = False
                else:
                    candy_choise_bot = 29 - candy_choise
                    print(f'Ход игрока {player2}: {candy_choise_bot}')
                    winner = player2
                    fl2 = False
                if 56 <= count <= 29:
                    candy_choise_bot = 47 - count
                    count -= candy_choise_bot
                    print(f'Ход игрока {player2}: {candy_choise_bot}')
                    print(f'Осталось {count} конфет')
                    winner = player2
                    fl2 = False
                elif count >= 28:
                    count -= candy_choise_bot
                    print(f'Осталось {count} конфет')
                    winner = player2
                    fl2 = False
                elif count <= 28 and candy_choise_bot <= count:
                    count -= candy_choise_bot
                    print(f'Осталось {count} конфет')
                    winner = player2
                    fl2 = False
                elif count == 0:
                    print(f'Осталось {count} конфет')
                    winner = player2
        if not fl1 and not fl2:
            step += 1
            fl1 = True
            fl2 = True
    print(f'Победитель игрок {winner}! Поздравляем!')

#3. Создайте программу для игры в ""Крестики-нолики"".
def PrintTickTackToe(r1, r2, r3): # Печатаем Крестики-нолики
    print(f'|{r1[0]}|{r1[1]}|{r1[2]}|')
    print(f'|{r2[0]}|{r2[1]}|{r2[2]}|')
    print(f'|{r3[0]}|{r3[1]}|{r3[2]}|')

def Krestick(r1, r2, r3, row_kr, col_kr): #Заносим крестик
    fl = False
    if row_kr == 1:
        if r1[col_kr - 1] == '-':
            r1[col_kr - 1] = 'X'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения!')
    if row_kr == 2:
        if r2[col_kr - 1] == '-':
            r2[col_kr - 1] = 'X'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения!')
    if row_kr == 3:
        if r3[col_kr - 1] == '-':
            r3[col_kr - 1] = 'X'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения!')
    return fl

def Win(r1, r2, r3):    #Определяем, является текущая ситуация выигрышной
    winner = ''
    if r1 == ['X', 'X', 'X']:
        winner = 'Победили крестики!'
    if r1 == ['O', 'O', 'O']:
        winner = 'Победили нолики!'
    if r2 == ['X', 'X', 'X']:
        winner = 'Победили крестики!'
    if r2 == ['O', 'O', 'O']:
        winner = 'Победили нолики!'
    if r3 == ['X', 'X', 'X']:
        winner = 'Победили крестики!'
    if r3 == ['O', 'O', 'O']:
        winner = 'Победили нолики!'
    if r1[0] == 'X' and r2[0] == 'X' and r3[0] == 'X':
        winner = 'Победили крестики!'
    if r1[0] == 'O' and r2[0] == 'O' and r3[0] == 'O':
        winner = 'Победили нолики!'
    if r1[1] == 'X' and r2[1] == 'X' and r3[1] == 'X':
        winner = 'Победили крестики!'
    if r1[1] == 'O' and r2[1] == 'O' and r3[1] == 'O':
        winner = 'Победили нолики!'
    if r1[2] == 'X' and r2[2] == 'X' and r3[2] == 'X':
        winner = 'Победили крестики!'
    if r1[2] == 'O' and r2[2] == 'O' and r3[2] == 'O':
        winner = 'Победили нолики!'  
    if r1[0] == 'X' and r2[1] == 'X' and r3[2] == 'X':
        winner = 'Победили крестики!'
    if r1[0] == 'O' and r2[1] == 'O' and r3[2] == 'O':
        winner = 'Победили нолики!'
    if r1[2] == 'X' and r2[1] == 'X' and r3[0] == 'X':
        winner = 'Победили крестики!'
    if r1[2] == 'O' and r2[1] == 'O' and r3[0] == 'O':
        winner = 'Победили нолики!'
    if len(winner) > 0:
        return winner
    else:
        return 'Next step'

def Nolick(r1, r2, r3, row_nol, col_nol): #Заносим нолик
    fl = False
    if row_nol == 1:
        if r1[col_nol - 1] == '-':
            r1[col_nol - 1] = 'O'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения!')
    if row_nol == 2:
        if r2[col_nol - 1] == '-':
            r2[col_nol - 1] = 'O'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения!')
    if row_nol == 3:
        if r3[col_nol - 1] == '-':
            r3[col_nol - 1] = 'O'
            fl = True
        else:
            print('Эта позиция уже занята! Введите другие значения!')
    return fl

def TickTackToe():
    row1 = ['-','-', '-']
    row2 = ['-','-', '-']
    row3 = ['-','-', '-']
    
    print('Начало игры:')
    PrintTickTackToe(row1, row2, row3)
    
    count_tick_tack = 0
    flag_game = False
    while not flag_game:
        winner_game = Win(row1, row2, row3)
        if winner_game == 'Next step' and count_tick_tack < 9: 
            flag_krest = False
            while not flag_krest:
                print('Введите позицию крестика:')
                row_krest = int(input('строка (от 1 до 3): \n'))
                col_krest = int(input('столбец (от 1 до 3): \n'))
                if row_krest < 1 or row_krest > 3 or col_krest < 1 or col_krest > 3:
                    print('Введите значения позиции крестика в пределах от 1 до 3!')
                else:
                    if Krestick(row1, row2, row3, row_krest, col_krest):
                        flag_krest = True
                        count_tick_tack += 1
            PrintTickTackToe(row1, row2, row3)
        elif count_tick_tack == 9:
            print('НИЧЬЯ!')
            exit()
        else:
            print(winner_game)
            exit()
                    
        winner_game = Win(row1, row2, row3)
        if winner_game == 'Next step' and count_tick_tack < 9:
            flag_nol = False
            while not flag_nol:
                print('Введите позицию нолика:')
                row_nolick = int(input('строка (от 1 до 3): \n'))
                col_nolick = int(input('столбец (от 1 до 3): \n'))
                if row_nolick < 1 or row_nolick > 3 or col_nolick < 1 or col_nolick > 3:
                    print('Введите значения позиции крестика в пределах от 1 до 3!')
                else:
                    if Nolick(row1, row2, row3, row_nolick, col_nolick):
                        flag_nol = True
                        count_tick_tack += 1
            PrintTickTackToe(row1, row2, row3)
        elif count_tick_tack == 9:
            print('НИЧЬЯ!')
            exit()
        else:
            print(winner_game)
            exit()

#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def CodeText(text):
    index_ch = 0
    code_text = ''
    count_ch = 1
    while index_ch < len(text) - 1:
        if text[index_ch] == text[index_ch + 1]:
            count_ch += 1
        else:
            code_text = code_text + str(count_ch) + text[index_ch]
            count_ch = 1
        index_ch += 1
    if text[index_ch - 1] == text[index_ch]:
        code_text = code_text + str(count_ch) + text[index_ch]
    else:
        code_text = code_text + '1' + text[index_ch]
    return code_text

def DeCodeText(text):
    index_ch = 0
    decode_text = ''
    str_ch = ''
    while index_ch < len(text) - 1:
        if text[index_ch].isdigit():
            str_ch += text[index_ch]
        else:
            if str_ch == '':
                print('Строка не подходит для декодирования')
                return ''
            else:
                for i in range(int(str_ch)):
                    decode_text += text[index_ch]
                str_ch = ''
        index_ch += 1
    if not text[index_ch].isdigit() and str_ch != '':
        for i in range(int(str_ch)):
            decode_text += text[index_ch]
    else:
        print('Строка не подходит для декодирования')
        return ''
    return decode_text

def CodeDecodeText():
    data = input('Введите текст для кодирования: ')
    data = data.rstrip()
    if data == '':
        print('Не введен текст для кодирования!')
    else:
        code_data = CodeText(data)
        print(f'{code_data}')
    data1 = input('Введите текст для декодирования: ')
    if data1 == '':
        print('Не введен текст для декодирования!')
    else:
        decode_data = DeCodeText(data1)
        if decode_data != '':
            print(decode_data)
        else:
            print('Строка не подходит для декодирования')


#DelABV()
#ManMan(2021)
#ManBot(2021)
#ManBotIntellect(2021) #БОТ ходит первым - тогда он выигрывает
#TickTackToe()
CodeDecodeText()