"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phone_sold_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    
    sum_sold_all = 0
    all_items_sold = 0

    def summ_sold_func(phone_sold):
        
        sum_sold = 0
        
        for sold in phone_sold:
            sum_sold += sold
        return sum_sold
    
    for one_phone in phone_sold_list:
        sum_phone_sold = summ_sold_func(one_phone['items_sold'])
        print(f"Продано {one_phone['product']}: {sum_phone_sold} шт.")

    for one_phone in phone_sold_list:
        sum_phone_sold = summ_sold_func(one_phone['items_sold'])
        aver_phone_sold = int(sum_phone_sold/len(one_phone['items_sold']))
        print(f"Продано в среднем {one_phone['product']}: {aver_phone_sold} шт.")

    for one_phone in phone_sold_list:
        sum_phone_sold = summ_sold_func(one_phone['items_sold'])
        sum_sold_all += sum_phone_sold
        all_items_sold += len(one_phone['items_sold'])  
    print(f'Всего телефонов продано: {sum_sold_all}')
    print(f'Среднее число продаж: {sum_sold_all/all_items_sold}')

if __name__ == "__main__":
    main()
