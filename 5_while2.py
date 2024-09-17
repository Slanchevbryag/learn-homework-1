"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Привет': 'Привет',
                         'Как дела': 'Хорошо',
                         'Что делаешь': 'Программирую'}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        
        bla_bla = input('Поболтаем? ')
        bla_bla = bla_bla.capitalize() # добавила регистор

        if bla_bla == 'Пока':
            print('Ариведерчи')
            break
        print(questions_and_answers.get(bla_bla, 'Спроси, что-нибудь другое')) # добавила значение по умолчанию
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
