def right_num():
    print('Добро пожаловать в числовую угадайку.')
    print('Введите целое число больше нуля, в пределах которого будем угадывать:')
    right = input()
    while True:
        if not right.isdigit() or int(right) < 1:
            print('Пожалуйста, введите целое число больше нуля!')
            right = input()
            continue
        return int(right)


def rand_num():
    import random
    num = random.randrange(1, right + 1)

    return num


def logarithm():
    from math import ceil, log2
    res = ceil(log2(right))
    print('Начнём!', 'Количество попыток:', res)

    return res


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= right


right = right_num()
num = rand_num()
loga = logarithm()

count = 0
while True:
    print('Введите число от 1 до', right)
    n = input()
    if is_valid(n) is False:
        print('А может быть все-таки введем целое число от 1 до', right, '?')
    else:
        n = int(n)
        if n < num:
            count += 1
            loga -= 1
            print('Ваше число меньше загаданного, оставшиеся попытки:', loga)
            if loga == 0:
                print('К сожалению, у вас закончились попытки!')
                print('Хотите сыграть еще раз?', 'Введите "да" или "нет"')
                answer = input().lower()
                while answer != 'да' and answer != 'нет':
                    print('Пожалуйста, введите "да" или "нет"')
                    answer = input().lower()
                if answer == 'да':
                    count = 0
                    right = right_num()
                    num = rand_num()
                    loga = logarithm()
                else:
                    print('Спасибо, что играли в числовую угадайку! Еще увидимся...')
                    while answer != 'выход':
                        print('Для выхода наберите: "выход"')
                        answer = input().lower()
                    break
            else:
                continue
        elif n > num:
            count += 1
            loga -= 1
            print('Ваше число больше загаданного, оставшиеся попытки:', loga)
            if loga == 0:
                print('К сожалению, у вас закончились попытки!')
                print('Хотите сыграть еще раз?', 'Введите "да" или "нет"')
                answer = input().lower()
                while answer != 'да' and answer != 'нет':
                    print('Пожалуйста, введите "да" или "нет"')
                    answer = input().lower()
                if answer == 'да':
                    count = 0
                    right = right_num()
                    num = rand_num()
                    loga = logarithm()
                else:
                    print('Спасибо, что играли в числовую угадайку! Еще увидимся...')
                    while answer != 'выход':
                        print('Для выхода наберите: "выход"')
                        answer = input().lower()
                    break
            else:
                continue
        elif n == num:
            count += 1
            print('Вы угадали число за', count, 'попыток, поздравляем!')
            print('Спасибо, что играли в числовую угадайку.')
            print('Хотите сыграть еще раз?', 'Введите "да" или "нет"')
            answer = input().lower()
            while answer != 'да' and answer != 'нет':
                print('Пожалуйста, введите "да" или "нет"')
                answer = input().lower()
            if answer == 'да':
                count = 0
                right = right_num()
                num = rand_num()
                loga = logarithm()
            elif answer == 'нет':
                print('Спасибо, что играли в числовую угадайку! Еще увидимся...')
                while answer != 'выход':
                    print('Для выхода наберите: "выход"')
                    answer = input().lower()
                break
