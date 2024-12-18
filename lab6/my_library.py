import random

def task6_1(file_name):
    '''
    Задание
    Багаж пассажира характеризуется количеством и общим весом вещей. Дан файл f,
    содержащий сведения о багаже нескольких пассажиров. Сведения о багаже каждого
    пассажира представляют собой запись вида:
    «Код пассажира (целое число), количество вещей (целое) вес (в кг, вещественное)»
    Найти число пассажиров, имеющих более двух вещей и число пассажиров, количество
    вещей которых превосходит среднее число вещей. Предусмотреть обработку всех
    возможных исключительных ситуаций.

    :param file_name: Имя файла с клавиатуры
    :return: None
    '''
    number_passenger = int(input('Введите количество пассажиров: '))                        # Устанавливаем количество пассажиров

    def create_file():
        '''
        Функция создает файл в котором хранятся рандомные данные о пассажире - код(от 0 до кол-во пассажиров), кол-во вещей(от 0 до 1000), вес багажа(от 1 до 100 кг)
        :param: None
        :return: None
        '''
        # Создаем файл
        with open(file_name, "w+", encoding='utf-8') as f:
            # Заполняем файл рандомными данными для каждого пассажира
            for _ in range(number_passenger):

                code_passenger = random.randint(0, number_passenger)                     # Генерируем код пассажира
                number_of_things = random.randint(0, 1000)                            # Генерируем количество вещей
                weight = random.uniform(1, 100)                                       # Генерируем вес от 1 до 100 кг

                # Записываем данные о пассажире в файл, вес с точностью до двух знаков после запятой
                f.write(f'{code_passenger} {number_of_things} {weight:.2f}\n')


    def open_file(file_name):
        '''
        Функция открывает файл для чтения, удаляет пустые строки, выводит количество пассажиров с более чем двумя вещами и количество пассажиров с количеством вещей выше среднего

        :param file_name: имя файла
        :return: None
        '''
        total_things = 0               # Переменная для хранения общего количества вещей
        count_passengers = 0           # Счетчик пассажиров
        count_more_than_two = 0        # Счетчик пассажиров с более чем двумя вещами
        passengers = []                # Список для хранения количества вещей каждого пассажира

        try:
            # Открываем файл для чтения данных
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.readlines()  # Читаем все строки из файла

            # Удаляем пустые строки и собираем данные
            for line in data:

                if line.strip():                            # Проверяем, что строка не пустая

                    parts = line.split()                    # Разделяем строку на части
                    number_of_things = int(parts[1])        # Получаем количество вещей
                    passengers.append(number_of_things)     # Добавляем количество вещей в список
                    total_things += number_of_things        # Увеличиваем общее количество вещей
                    count_passengers += 1                   # Увеличиваем счетчик пассажиров

                    if number_of_things > 2:                # Проверяем, больше ли количество вещей двух

                        count_more_than_two += 1            # Увеличиваем счетчик для пассажиров с более чем двумя вещами

            # среднее количество вещей
            average_things = total_things / max(count_passengers, 1)


            # Считаем количество пассажиров, у которых количество вещей больше среднего

            count_above_average = 0                 # Счетчик для пассажиров с количеством вещей выше среднего

            for num_things in passengers:           # Проходим по списку пассажиров
                if num_things > average_things:     # Проверяем, больше ли количество вещей среднего
                    count_above_average += 1        # Увеличиваем счетчик


            print(f'Количество пассажиров с более чем двумя вещами: {count_more_than_two}')
            print(f'Количество пассажиров с количеством вещей выше среднего: {count_above_average}')

        except FileNotFoundError:                   # Обработка исключения, если файл не найден
            print("Файл не найден")
        except Exception as e:                      # Обработка других возможных исключений
            print(f"Произошла ошибка: {e}")

    create_file()
    open_file(file_name)





def task6_2(filename):
    '''
    Задание
    Дан текстовый файл f, содержащий буквы и цифры. Вывести на экран все числа (все
    подряд идущие цифры) из этого файла, и их сумму.
    Пример содержимого файла «фываы23оаввла фав 5 рку 675ые89фт й895»
    Вывод: 23 5 675 89 895, Сумма 1687
    Предусмотреть обработку всех возможных исключительных ситуаций.

    :param filename: имя файла
    :return: None
    '''
    import random
    import string
    # Функция для создания файла с рандомным текстом

    def create_file(filename):
        '''
        Функция создает файл с рандомным текстом

        :param filename:
        :return: None
        '''
        # Генерируем случайный текст
        text_length = random.randint(50, 100)                                                      # Длина текста от 50 до 100 символов
        random_text = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=text_length)) # string.ascii_letters - содержит все буквы латинского алфавита
                                                                                                         # string.digits - содержит все цифры от 0 до 9

        # Записываем текст в файл
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(random_text)  # Запись текста в файл


    # Функция для открытия файла и обработки его содержимого
    def open_file(filename):
        '''
        Функция открывает файл на чтение, ищет числа в файле, выводит их и выводит сумму

        :param filename:
        :return: None
        '''
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Содержимое файла: {content}")

                numbers = []              # Список для хранения найденных чисел
                current_number = ''       # Переменная для формирования текущего числа

                # Проходим по каждому символу в содержимом файла
                for char in content:
                    if char.isdigit():          # Если символ - цифра
                        current_number += char  # Добавляем цифру к текущему числу
                    else:
                        if current_number:                       # Если текущее число не пустое
                            numbers.append(int(current_number))  # Добавляем число в список
                            current_number = ''                  # Сбрасываем текущее число

                # Проверяем, не осталось ли число в конце строки
                if current_number:
                    numbers.append(int(current_number))  # Добавляем последнее число в список

                # Выводим найденные числа и их сумму
                if numbers:                                                 # Если список чисел не пуст
                    print("Найденные числа:", ' '.join(map(str, numbers)))  # Выводим числа
                    print("Сумма:", sum(numbers))                           # Выводим сумму чисел
                else:
                    print("Чисел не найдено.")  # Если чисел нет

        except FileNotFoundError:                           # Обработка исключения, если файл не найден
            print(f"Ошибка: Файл '{filename}' не найден.")
        except Exception as e:                              # Обработка других исключений
            print(f"Произошла ошибка: {e}")



    create_file(filename)
    open_file(filename)




