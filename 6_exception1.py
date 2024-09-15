"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:

      try:
        ask_user = input('Как дела? ')
        if ask_user.upper() == 'ХОРОШО':
          break
      except KeyboardInterrupt:
         print('Пока!')
         break
    
if __name__ == "__main__":
    hello_user()
