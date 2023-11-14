from dadata import Dadata
from settings import *
import sqlite3

def start():
    #function that renders a main menu
    global dadata
    print("\nДобро пожаловать в систему main.py, введите номер действия которое хотите совершить")
    print("1. Узнать координаты по адресу")
    print("2. Настройки")
    print("3. Выход")
        
    answer = input()
        
    if answer == "3":
        return 0
    elif answer == "2":
        show_settings()
    elif answer == "1":
        get_adress()
    else:
        start()

def get_adress():
    #function that uses api to send a get request and show the result
    global dadata
    data = dadata.suggest("address", input("\nВведите адрес:\n"), language=get_lang(), count=get_count())
    if len(data) > 1:
        print("\nМы нашли несколько адресов с похожим названием, пожалуйста введите цифру вашего адреса")
        for i in range(1, len(data) + 1):
            print(f"{i}. {data[i - 1]['unrestricted_value']}")
        result = data[int(input()) - 1]
        if input(f"\nВыбранный адрес: {result['unrestricted_value']}\nВерно? (Да/Нет)\n").lower() == 'да':
            print('\n' + result['unrestricted_value'])
            print(f"Координаты широты: {result['data']['geo_lat']}")
            print(f"Координаты долготы: {result['data']['geo_lon']}")
            print('\n')
        else:
            print('Вероятно в введённом ранее адресе есть ошибка\n')
    else:
        print('\nКажется такого адреса не существует\n ')
    print('Желаете попробовать ещё раз или перейти на главный экран?')
    print('1. Ещё раз')
    print('2. На главную')
    if input() == '1':
        get_adress()
    else:
        start()

def input_data():
    #function that searching api and secret key in database. If haven't found, than requesting them from user
    #also works as a data validator
    if get_api() is None or get_secret_key() is None:
        print('Введите ваш API:')
        change_api(input())
        print('Секретный ключ:')
        change_secret_key(input())
        connection.commit()
        input_data()
    else:
        try:
            global dadata
            dadata = Dadata(get_api(), get_secret_key())
            data = dadata.clean('address', 'Москва Красная Площадь 1')
            if data['result'] == 'г Москва, пл Красная, д 1':
                start()
        except:
            print('Кажется во введённых ранее данных есть ошибка, попробуйте ещё раз')
            del_api()
            del_secret_key()
            input_data()

def set_lang():
    #function to choose a language in which data will be shown
    print('\nВыберите язык:')
    print('1. Русский')
    print('2. Английский')
    print('3. Выход')
    answer = input()
    if answer == '1':
        change_lang('ru')
        print('Язык был изменён на Русский')
        show_settings()
    elif answer == '2':
        change_lang('en')
        print('Язык был изменён на Английский')
        show_settings()
    elif answer == '3':
        show_settings()
    else:
        set_lang()
    connection.commit()

def set_api():
    #function to change API by settings
    print(f'\nТекущий API: {get_api()}')
    print(f'\nТекущий секретный ключ: {get_secret_key()}')
    print('\nЖелаете поменять? (Да/Нет)')
    answer = input()
    if answer.lower() == 'да':
        print('Введите новый API:')
        change_api(input())
        print('Введите новый секретный ключ')
        change_secret_key(input())
        input_data()
    elif answer.lower() == 'нет':
        input_data()
    else:
        set_api()
    connection.commit()

def set_count():
    #function to set how many variants will be shown
    print(f"\nТекущее количество вариантов выбора: {get_count()}")
    print(f"Введите сколько вариантов вы хотите отображать (от 10 до 20)")
    try:
        count = int(input())
        if count >= 20:
            count = 20
            print('Вы ввели слишком большое число, оно было сокращено до 20')
        elif count <= 10:
            count = 10
            print('Вы ввели слишком маленькое число, оно было увеличено до 10')
        change_count(count)
        connection.commit()
        show_settings()
    except:
        print('\nОШИБКА! Кажется вы ввели не число, попробуйте ещё раз\n')
        set_count()
    
def show_settings():
    #just showing general settings
    print('\nНастройки:')
    if get_lang() == 'ru':
        print('Текущий язык: Русский')
    else:
        print('Текущий язык: Английский')
    print(f"API: {get_api()}")
    print(f"Secret Key: {get_secret_key()}")
    print(f"Количество вариантов выбора: {get_count()}")
    settings()

def settings():
    #function that asking user which settings to change
    print('\nВыберите цифру настроек которые хотите поменять:')
    print('1. Изменить язык вывода')
    print('2. Изменить api и секретный ключ')
    print('3. Изменить количество вариантов выбора')
    print('4. Выход из настроек')
    
    answer = input()
    if answer == '4':
        start()
    elif answer == '1':
        set_lang()
    elif answer == '2':
        set_api()
    elif answer == '3':
        set_count()
    else:
        settings()
    

def main():
    set_db()
    input_data()

if __name__ == '__main__':
    main()