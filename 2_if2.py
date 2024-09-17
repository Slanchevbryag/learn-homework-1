"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #было def two_string(one='', two=''):
    def make_two_string(one='', two=''):
        
        if type(one)!=str or type(two)!=str:
          return 0
        
        elif one == two:
          return 1
        
        elif two == 'learn':
           return 3

        elif len(one) > len(two):
           return 2
           
    print(make_two_string(one=4, two=6)) #0
    print(make_two_string(one='раз строка', two=6)) #0
    print(make_two_string(one=4, two='два строка')) #0
    print(make_two_string(one='строка', two='строка')) #1
    print(make_two_string(one='раз строка', two='строка')) #2
    print(make_two_string(one='раз строка', two='learn')) #3
    
if __name__ == "__main__":
    main()
