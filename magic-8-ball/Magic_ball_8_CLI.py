import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


def text(word):     #проверяем на ввод хоть чего-то, что содержит буквы или цифры
    return not word.isspace() and not word == ''


def ask_question():
    print('Введите свой вопрос:')
    question = input()
    while text(question) is False:
        print('Пожалуйста, введите свой вопрос!')
        question = input()
    print('Ответ:', random.choice(answers))

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как вас зовут?')

while True:
    name = input()
    if text(name) is False:
        print('Пожалуйста, введите имя!')
    else:
        print('Привет,', name)
        ask_question()
        while True:
            print('Хотите задать еще один вопрос? Введите "да" или "нет"')
            answer = input().lower()
            while answer != 'да' and answer != 'нет':
                print('Пожалуйста, введите "да" или "нет"')
                answer = input().lower()
            if answer == 'да':
                ask_question()
            elif answer == 'нет':
                print('Возвращайтесь, если возникнут вопросы!')
                while answer != 'выход':
                    print('Для выхода наберите: "выход"')
                    answer = input().lower()
                break
        break
