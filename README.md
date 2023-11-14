![image](https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/92c18df1-5f32-4ff9-bf16-1c9a4bb357b9)# carbis-address-locator
Как установить Python на Windows, Linux и macOS

Дистрибутивы Python есть для всех популярных операционных систем, они перечислены на официальном сайте [python.org](https://www.python.org). По большому счёту, не так важно, какую конкретно версию Python вы скачаете, — главное, чтобы её номер начинался с цифры 3.


# Установка в Windows 7/10
Скачайте установочный файл, нажав на жёлтую кнопку Download Python, и запустите его.

<img width="1540" alt="08374522032023_e3039f248dd555899a396179b51a05be377f9973" src="https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/ff72485d-962a-477b-afbd-0d26d1c40821">

Выберите путь установки и поставьте обе галочки: во втором пункте мы указываем, что нужно добавить Python в переменную окружения PATH — это позволит вызывать его из любой директории. Затем выбираем «Установка для всех пользователей» (Install for all users), нажимаем Install Now и разрешаем приложению вносить изменения:

<img width="1540" alt="08374622032023_ee673444daa2c4c150863fb4fe2e59385df85324" src="https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/e71f1021-50b4-44a2-af30-9f3adecbcf91">


Когда всё установится, вы увидите окно завершения инсталляции:

<img width="1540" alt="08395922032023_a3e9b924b0c79cb7169afa563a255fa0a5b1cadd" src="https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/e1875fbd-a4b3-46af-97a5-245cd6f9b422">


Теперь проверим, что Python действительно установлен. Для этого откроем окно «Выполнить» сочетанием клавиш Win + R и введём cmd:

<img width="1540" alt="08395922032023_cae856732bd4226855875d839121e46dd85999a9" src="https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/a0b57943-b93f-457b-b001-092b6c8ed669">


Откроется командная строка. Введите в ней команду ```py``` или ```python```, чтобы запустить интерпретатор. На экране появится примерно такое сообщение:

Microsoft Windows [Version 10.0.19043.1889]

(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.


C:\Users\User>py

Python 3.11.2 (tags/v3.11.2:9c7b4bd, Feb 2 2023, 18:38:48) [MSC v.1932 64 bit (AMD64)] on win 32

Type "help", "copyright", "credits" or "license" for more information.

>>>


Оно означает, что Python установлен на ваш компьютер и работает.

# Python установлен, теперь можно запускать мой проект
На windows:
1. Открываем командную строку сочетанием клавиш Win + R и введём cmd
![image](https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/1df5c59a-3424-4386-8376-350c90ad57d8)

3. Выбираем папку в которую будем загружать наш проект, выбрать можно при помощи навигации по:

```cd <имя_папки>``` - перейти в папку с именем <имя_папки>

```cd ..``` - подняться на уровень выше / выйти из нынешней папки

```dir``` - посмотреть содержимое в текущей папке (```ls``` на Linux)

```mkdir <имя_папки>``` - создать папку с именем <имя_папки>

![image](https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/549f5660-485e-4579-8b4b-9348ae249793)


3. В командную строку прописываем
```git clone https://github.com/JuicyS8da/carbis-address-locator.git```

![image](https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/488e9376-2757-403b-bf0a-94867cc9f322)


```python -m venv venv```

```venv\Scripts\activate```

Это позволит нам создать виртуальное окружение в котором будут храниться все модули для нашего проекта
5. Затем, убедившись что мы в одной папке с файлом 'requirements.txt', в командную строку прописываем

```pip install -r requirements.txt```

![image](https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/f43ecef5-534b-48e5-a250-033d99564ace)

Тем самым загрузив недостающие для нашего проекта модули

6. И теперь наконец прописываем

```python main.py```

![image](https://github.com/JuicyS8da/carbis-address-locator/assets/118248275/d636f58b-bf0a-4119-a823-b06319015403)


8. Также он потребует API-ключ и Секретный ключ, которые можно найти у себя в личном кабинете зарегестрировавшись здесь: https://dadata.ru/api/
