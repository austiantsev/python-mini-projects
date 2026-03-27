import sys


def check_crypt(answer):
    while answer != 'ш' and answer != 'д':
        answer = input('Шифрование или Дешифрование? Введите: Ш или Д\n').lower()
    return answer


def check_lang(answer):
    while answer != 'а' and answer != 'р':
        answer = input('Английский или Русский язык? Введите: А или Р\n').lower()
    return answer


def check_number(answer):
    while not answer.isdigit() or int(answer) <= 0:
        answer = input('Пожалуйста, введите целое число больше нуля!\n')
    answer = int(answer)
    return answer


def check_text_en(answer):
    while answer.isspace() or answer == '':
        answer = input('Введите данные для шифрования на английском языке.\n')
    for i in answer:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            continue
        elif 1040 <= ord(i) <= 1071 or 1072 <= ord(i) <= 1103:
            print('Внимание! Несоответствие данных.')
            check_answers(crypt, lang, step)
        else:
            continue
    return answer


def check_text_ru(answer):
    while answer.isspace() or answer == '':
        answer = input('Введите данные для шифрования на русском языке.\n')
    for i in answer:
        if 1040 <= ord(i) <= 1071 or 1072 <= ord(i) <= 1103:
            continue
        elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            print('Внимание! Несоответствие данных.')
            check_answers(crypt, lang, step)
        else:
            continue
    return answer


def enc_en(step):
    words = check_text_en(input('Введите данные для шифрования на английском языке.\n'))
    st = ''
    for j in words:
        if j.islower():
            c = ord(j) + step
            if c > 122:
                c -= 26
            st += chr(c)
        elif j.isupper():
            c = ord(j) + step
            if c > 90:
                c -= 26
            st += chr(c)
        else:
            st += j
    print(f'Ваш шифр: {st}')
    repeat_cipher()


def dec_en(step):
    words = check_text_en(input('Введите данные для дешифрования на английском языке.\n'))
    st = ''
    for j in words:
        if j.islower():
            c = ord(j) - step
            if c < 97:
                c += 26
            st += chr(c)
        elif j.isupper():
            c = ord(j) - step
            if c < 65:
                c += 26
            st += chr(c)
        else:
            st += j
    print(f'Ваш дешифр: {st}')
    repeat_cipher()


def enc_rus(step):
    words = check_text_ru(input('Введите данные для шифрования на русском языке.\n'))
    st = ''
    for j in words:
        if j.islower():
            c = ord(j) + step
            if c > 1103:
                c -= 32
            st += chr(c)
        elif j.isupper():
            c = ord(j) + step
            if c > 1071:
                c -= 32
            st += chr(c)
        else:
            st += j
    print(f'Ваш шифр: {st}')
    repeat_cipher()


def dec_rus(step):
    words = check_text_ru(input('Введите данные для дешифрования русском языке.\n'))
    st = ''
    for j in words:
        if j.islower():
            c = ord(j) - step
            if c < 1072:
                c += 32
            st += chr(c)
        elif j.isupper():
            c = ord(j) - step
            if c < 1040:
                c += 32
            st += chr(c)
        else:
            st += j
    print(f'Ваш дешифр: {st}')
    repeat_cipher()


print('Добро пожаловать в программу "Шифр Цезаря"!', 'Это программа шифрует или дешифрует любую введенную фразу.',
      sep='\n')


def check_answers(crypt, lang, step):
    if crypt == 'ш' and lang == 'а':
        enc_en(step)
    elif crypt == 'ш' and lang == 'р':
        enc_rus(step)
    elif crypt == 'д' and lang == 'а':
        dec_en(step)
    elif crypt == 'д' and lang == 'р':
        dec_rus(step)


def caesar_cipher():
    global crypt, lang, step
    crypt = check_crypt(input('Шифрование или Дешифрование? Введите: Ш или Д\n'))
    lang = check_lang(input('Английский или Русский язык? Введите: А или Р\n'))
    step = check_number(input('Введите шаг сдвига.\n'))

    check_answers(crypt, lang, step)


def repeat_cipher():
    while True:
        answer = input('Хотите обработать еще одну фразу или слово?\n').lower()
        while answer != 'да' and answer != 'нет':
            answer = input('Пожалуйста, введите "да" или "нет"\n').lower()
        if answer == 'да':
            caesar_cipher()
        elif answer == 'нет':
            print('Возвращайтесь, как можно скорее!')
            while answer != 'выход':
                answer = input('Для выхода наберите: "выход"\n').lower()
            sys.exit()


caesar_cipher()
