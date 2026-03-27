import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'


def check_amount(answer):
    while not answer.isdigit() or int(answer) < 1:
        answer = input('Пожалуйста, введите целое число больше нуля!\n')
        continue
    answer = int(answer)
    return answer


def check_len_pass(answer):
    while not answer.isdigit() or int(answer) <= 3:
        answer = input('Пожалуйста, введите целое число больше трёх!\n')
        continue
    answer = int(answer)
    return answer


def check_answer(answer):
    while answer != 'да' and answer != 'нет':
        answer = input('Пожалуйста, введите "да" или "нет"\n').lower()
    if answer == 'да':
        return True
    return False


def repeat_creation():
    while True:
        print('Хотите создать еще пароли?')
        answer = input().lower()
        while answer != 'да' and answer != 'нет':
            print('Пожалуйста, введите "да" или "нет"')
            answer = input().lower()
        if answer == 'да':
            generate_password()
        elif answer == 'нет':
            print('Возвращайтесь, если понадобятся пароли!')
            while answer != 'выход':
                print('Для выхода наберите: "выход"')
                answer = input().lower()
            break


def nothing():
    while True:
        if numbers is False and low_alpha is False and upp_alpha is False and punct is False:
            print('Вы не выбрали ни одну группу символов. Начнём сначала.')
            generate_password()
        else:
            break


def generate_password():
    global numbers, low_alpha, upp_alpha, punct
    amount = check_amount(input('Введите количество паролей для генерации:\n'))
    len_pass = check_len_pass(input('Введите количество символов для пароля:\n'))
    numbers = check_answer(input('Хотите использовать цифры?\n'))
    low_alpha = check_answer(input('Хотите использовать строчные буквы?\n'))
    upp_alpha = check_answer(input('Хотите использовать прописные буквы?\n'))
    punct = check_answer(input('Хотите использовать символы пунктуации?\n'))
    non_symbols = check_answer(input('Использовать, неоднозначные символы: il1Lo0O ?\n'))

    nothing()

    done_passwords = []
    for i in range(amount):
        chars = []
        while len(chars) != len_pass:
            if numbers and len(chars) < len_pass:
                chars.append(random.choice(digits))
            if low_alpha and len(chars) < len_pass:
                chars.append(random.choice(lowercase_letters))
            if upp_alpha and len(chars) < len_pass:
                chars.append(random.choice(uppercase_letters))
            if punct and len(chars) < len_pass:
                chars.append(random.choice(punctuation))
            if non_symbols is False:
                chars = [i for i in chars if i not in 'il1Lo0O']
        random.shuffle(chars)
        chars = ''.join(chars)
        done_passwords.append(chars)
    print(*done_passwords, sep='\n')


generate_password()
repeat_creation()
