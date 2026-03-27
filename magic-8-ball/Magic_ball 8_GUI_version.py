from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Магический шар")
root.geometry("400x250")
root.resizable(width=False, height=False)

# варианты ответов шара
answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено',
           'Вероятнее всего','Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
           'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
           'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом',
           'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

# случайное число для выбора предсказания по индексу
def show_message():
    messagebox.showinfo("Ответ", answers[random.randint(1, 20)])
    question_entry.delete("0", END)

# заголовок
label_text = Label(root, text='Задай вопрос', font=("Verdana", 25, 'bold'))
label_text.pack()

# ячейка для вопроса
question = StringVar()
question_entry = Entry(textvariable=question, width=60)
question_entry.place(relx=.5, rely=.25, anchor="c")

# кнопка для вывода ответа
message_button = Button(text="Узнать ответ", font=("Verdana", 13, "bold"), command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")



root.mainloop()