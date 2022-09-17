import random
import pickle

__version__ ='0.2'
'''R.Code  13 2022.09.13
Тестовая программа. Осуществляет подсчёт себестоимости, расходов, прибыли и др. для заправки картриджей
для определённых моделей картриджей. 
Заранее введённые данные (аксиомы): вес заправок нужной модели, стандарная (изначальная) цена банки с тонером, 
и вручную введены коэффициенты для формул подсчёта, исходя из фактических реалий, чтобы получались "живые" примеры
цен для применения.
Есть возможность ручного подсчёта прибыли и ручного ввода параметров для подсчёта.
Осуществлена защита от ошибки при отсутствии нужных файлов в момент попытки их открытия.
'''


# Приветствие программы
Hi = ['Привет, красавец!', 'Чё надо, чувырло?', 'Здравствуйте, пользователь программы!',
      'Добры дэн!', 'Внимательно.', 'Снова ты?', 'Кто написал этот R.code??', 'Не ешь тортик...',
      'Слушаюсь и повинуюсь!', 'Да, господин.', 'Готов работать!', 'Программа приветствует вас!']


# Основной класс для автоматического подсчёта рекомендуемой цены заправки.
class ce285a:
    # Представляет расчёты для этих моделей. Переменные класса:
    weight_bottle = 1000        # вес банки в граммах
    weight_cartrige = 90        # средний вес заправки
    refills = 11                # количество заправок на банку
    price_bottle_standart = 665 # Изначальная цена, точка отсчёта формул

    # Рассчитывается:
    price_bottle = 0            # Цена бутылки (вводится)
    price_refueling = 0         # Цена заправки (цель подсчёта)
    income = 0                  # Общий грязный доход
    income_expenses = 0         # Доход - расход от банки
    tax = 0                     # Налог 15%
    cost_cartrige = 0           # Расход денег за картридж без налога
    cost_cartrigeTax = 0        # Расход денег за картридж с налогом
    profit_cartrige = 0         # Прибыль за картридж
    profit = 0                  # Прибыль вся чистая (доход - расход - налог)


# Ручной класс для подсчёта прибыли и расходов от фактически введённых вручную цен покупки и заправки
class manual_counting:
    # Представляет расчёт вручную для банок тонера и продажи картриджей
    price_bottle_standart = 665 # Изначальная цена, точка отсчёта формул
    weight_bottle = 0           # Вес банки (вводится)
    weight_cartridge = 0         # Вес заправки (вводится)
    price_bottle = 0            # Цена банки (вводится)
    price_refueling = 0         # Цена заправки (вводится)

    # Рассчитывается:
    refills = 0                 # Количество заправок на банку
    income = 0                  # Общий грязный доход
    income_expenses = 0         # Доход - расход от банки
    tax = 0                     # Налог 15%
    cost_cartrige = 0           # Расход денег за картридж без налога
    cost_cartrigeTax = 0        # Расход денег за картридж с налогом
    profit_cartrige = 0         # Прибыль за картридж
    profit = 0                  # Прибыль вся чистая (доход - расход - налог)


# Класс для подсчёта прибыли и расходов при перепродаже картриджей
class cartridge:
    # Представляет расчёт прибыли при указанных ценах
    price_cartridge = 0
    sellprice = 0

    # Рассчитывается:
    tax = 0
    cost = 0
    profit = 0


# Основной цикл меню программы
while 1:
    print()  # Пробел, для удобства чтения при работе внутри цикла
    # Основное меню
    print('ПРОГРАММА "РАСЧЁТ ЦЕН.', random.choice(Hi), '''
    ──────▄▀▄─────▄▀▄
    ─────▄█░░▀▀▀▀▀░░█▄
    ─▄▄──█░░░░░░░░░░░█──▄▄
    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█

    1 - Просмотр цен
    2 - Подсчёт цен
    3 - Ручной подсчёт
    
    Для управления нажимайте соответствующие цифры и Enter:''')

    inp = input('Ввод:')
    if inp == '1':
        print('ВЫБЕРИТЕ, ГДЕ СМОТРИМ ЦЕНУ:\n'
              '1 - ce285a\n2 - ручной подсчёт банки\n3 - ручной подсчёт картриджа\n4 - НАЗАД')
        while 1:
            inp = input('Выберите:')
            if inp == '1':
                # Распикливаем БД из файла и подставляем нужные нам данные
                try:
                    op = open('pc.pkl', 'rb')
                    load = pickle.load(op)
                    print('\n\n.....Загружаем цены ce285a из файла:')
                    print(load[1], 'Грамм вес банки')
                    print(load[2], 'Грамм средний вес заправки (85г.)')
                    print(load[3], 'Шт. заправок получится с одной банки')
                    print(load[4], 'Рублей актуальная цена банки\n')
                    print(load[5], 'Рублей цена заправки (рекомендуемая)')
                    print(load[6], 'Рублей чистая прибыль с картриджа')
                    print(load[7], 'Рублей расход на картридж')
                    print(load[8], 'Рублей расход на картридж с налогом\n')
                    print(load[9], 'Рублей 15% налог')
                    print(load[10], 'Рублей общий доход без расходов')
                    print(load[11], 'Рублей доход минус цена банки')
                    print(load[12], 'Рублей чистая прибыль с банки')
                    op.close()
                    break
                except:
                    print('!!!!! Файл "pc.pkl" с ценами ещё не был создан. !!!!!\n'
                          '!!!!! Сначала зайдите в раздел "Редактирование цен" !!!!!')
                break
            if inp == '2':
                # Распикливаем БД из файла и подставляем нужные нам данные
                try:
                    op = open('pc.pkl', 'rb')
                    load = pickle.load(op)
                    print('\n\n.....Загружаем цены ручного подсчёта банки из файла:')
                    print(load[13], 'Грамм вес тонера в банке')
                    print(load[14], 'Грамм средний вес заправки')
                    print(load[15], 'Рубля актуальная цена банки')
                    print(load[16], 'Рублей цена заправки\n')
                    print(load[17], 'Шт. заправок получится с одной банки')
                    print(load[18], 'Рублей прибыль с банки')
                    print(load[19], 'Рублей доход с банки - цена банки')
                    print(load[20], 'Рублей 15% налог\n')
                    print(load[21], 'Рублей стоимость 1 заправки')
                    print(load[22], 'Рублей стоимость 1 заправки с налогом')
                    print(load[23], 'Рублей чистая прибыль с картриджа')
                    print(load[24], 'Рублей чистая прибыль с банки')
                    op.close()
                    break
                except:
                    print('!!!!! Файл "pc.pkl" с ценами ещё не был создан. !!!!!\n'
                          '!!!!! Сначала зайдите в раздел "Редактирование цен" !!!!!')
                break
            if inp == '3':
                # Распикливаем БД из файла 2 и подставляем нужные нам данные
                try:
                    op = open('pc2.pkl', 'rb')
                    load = pickle.load(op)
                    print(load[1], 'Цена покупки')
                    print(load[2], 'Цена продажи')
                    print(load[3], '15% налог')
                    print(load[4], 'Общие расходы')
                    print(load[5], 'Прибыль')
                    break
                except:
                    print('!!!!! Файл "pc2.pkl" с ценами ещё не был создан. !!!!!\n'
                          '!!!!! Сначала зайдите в раздел "Редактирование цен" !!!!!')
                break
            if inp == '4':
                break   # Выходим в меню
            else:
                print('ВВЕДИТЕ ЦИФРЫ ИЗ МЕНЮ')
                continue    # Обрабатываем исключения ввода и возвращаем программу в момент новой попытки ввода
        print('.....Выходим в главное меню')
        continue

    if inp == '2':
        print('ВЫБЕРИТЕ, ГДЕ МЕНЯЕМ ЦЕНУ:\n'
              '1 - ce285a\n2 - НАЗАД')
        while 1:
            inp = input('Выберите:')
            if inp == '1':
                while 1:
                    inp = input('Введите цену:')
                    if not inp.isdigit():
                        print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                    else:
                        print('.....Назначена новая цена:', inp)
                        # Формулы подсчёта. Имеются вручную введённые коэффициенты - число 240 и подсчёт с делением / 6
                        ce285a.price_bottle = int(inp)
                        ce285a.cost_cartrige = ce285a.price_bottle // ce285a.refills
                        ce285a.price_refueling = (ce285a.cost_cartrige + 240) // 1
                        if ce285a.price_bottle > 700:
                            ce285a.price_refueling = (ce285a.cost_cartrige + 240 +
                                                      ((ce285a.price_bottle - ce285a.price_bottle_standart) / 6))
                        ce285a.income = ce285a.price_refueling * ce285a.refills
                        ce285a.income_expenses = ce285a.income - ce285a.price_bottle
                        ce285a.tax = (ce285a.income_expenses * 0.15) // 1
                        ce285a.cost_cartrigeTax = (ce285a.price_bottle + ce285a.tax) // 11
                        ce285a.profit = ce285a.income_expenses - ce285a.tax
                        ce285a.profit_cartrige = ce285a.profit // ce285a.refills

                        # Запикливаем результаты подсчётов в БД файла, сохраняем их и закрываем его
                        database = {1: ce285a.weight_bottle,
                                    2: ce285a.weight_cartrige,
                                    3: ce285a.refills,
                                    4: ce285a.price_bottle,
                                    5: ce285a.price_refueling,
                                    6: ce285a.profit_cartrige,
                                    7: ce285a.cost_cartrige,
                                    8: ce285a.cost_cartrigeTax,
                                    9: ce285a.tax,
                                    10: ce285a.income,
                                    11: ce285a.income_expenses,
                                    12: ce285a.profit,
                                    13: manual_counting.weight_bottle,
                                    14: manual_counting.weight_cartridge,
                                    15: manual_counting.price_bottle,
                                    16: manual_counting.price_refueling,
                                    17: manual_counting.refills,
                                    18: manual_counting.income,
                                    19: manual_counting.income_expenses,
                                    20: manual_counting.tax,
                                    21: manual_counting.cost_cartrige,
                                    22: manual_counting.cost_cartrigeTax,
                                    23: manual_counting.profit_cartrige,
                                    24: manual_counting.profit}
                        Save = open('pc.pkl', 'wb')
                        pickle.dump(database, Save)
                        Save.close()
                        break
                break
            if inp == '2':
                break   # Выход в меню
            else:
                print('ВВЕДИТЕ ЦИФРЫ ИЗ МЕНЮ!')
                continue

        print('.....Выходим в главное меню')
        continue

    # Часть с ручным подсчётом цен
    if inp == '3':
        print('ВЫБЕРИТЕ, ГДЕ ПОДСЧИТАТЬ ЦЕНУ:\n'
              '1 - Банка тонера\n2 - Картридж на продажу\n3 - НАЗАД')
        while 1:
            inp = input('ВЫБЕРИТЕ:')
            if inp == '1':
                while 1:
                    inp_price_bottle = input('Введите цену банки:')
                    if not inp_price_bottle.isdigit():
                        print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                    else:
                        print('.....Назначена цена банки:', inp_price_bottle)
                        inp_weight_bottle = input('Введите вес банки:')
                        if not inp_weight_bottle.isdigit():
                            print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                        else:
                            print('.....Назначен вес банки:', inp_weight_bottle)
                            inp_weight_cartridge = input('Введите вес одной заправки:')
                            if not inp_weight_cartridge.isdigit():
                                print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                            else:
                                print('.....Назначен вес одной заправки:', inp_weight_cartridge)
                                inp_price_refueling = input('Введите цену одной заправки:')
                                if not inp_price_refueling.isdigit():
                                    print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                                else:
                                    print('.....Назначена цена одной заправки:', inp_price_refueling)
                                    # Формулы подсчёта для ручного варианта
                                    manual_counting.weight_cartridge = int(inp_weight_cartridge)
                                    manual_counting.weight_bottle = int(inp_weight_bottle)
                                    manual_counting.price_bottle = int(inp_price_bottle)
                                    manual_counting.price_refueling = int(inp_price_refueling)

                                    manual_counting.refills = (manual_counting.weight_bottle //
                                                               manual_counting.weight_cartridge)
                                    manual_counting.income = manual_counting.refills * manual_counting.price_refueling
                                    manual_counting.income_expenses = (manual_counting.income -
                                                                       manual_counting.price_bottle)
                                    manual_counting.tax = manual_counting.income_expenses * 0.15
                                    manual_counting.cost_cartrige = (manual_counting.price_bottle //
                                                                     manual_counting.refills)
                                    manual_counting.cost_cartrigeTax = ((manual_counting.price_bottle +
                                                                         manual_counting.tax) //
                                                                        manual_counting.refills)
                                    manual_counting.profit = (manual_counting.price_refueling * manual_counting.refills
                                                              - manual_counting.price_bottle - manual_counting.tax)
                                    manual_counting.profit_cartrige = manual_counting.profit // manual_counting.refills

                                    # Запикливаем результаты подсчётов в БД файла, сохраняем их и закрываем его
                                    database = {1: ce285a.weight_bottle,
                                                2: ce285a.weight_cartrige,
                                                3: ce285a.refills,
                                                4: ce285a.price_bottle,
                                                5: ce285a.price_refueling,
                                                6: ce285a.profit_cartrige,
                                                7: ce285a.cost_cartrige,
                                                8: ce285a.cost_cartrigeTax,
                                                9: ce285a.tax,
                                                10: ce285a.income,
                                                11: ce285a.income_expenses,
                                                12: ce285a.profit,
                                                13: manual_counting.weight_bottle,
                                                14: manual_counting.weight_cartridge,
                                                15: manual_counting.price_bottle,
                                                16: manual_counting.price_refueling,
                                                17: manual_counting.refills,
                                                18: manual_counting.income,
                                                19: manual_counting.income_expenses,
                                                20: manual_counting.tax,
                                                21: manual_counting.cost_cartrige,
                                                22: manual_counting.cost_cartrigeTax,
                                                23: manual_counting.profit_cartrige,
                                                24: manual_counting.profit}
                                    Save = open('pc.pkl', 'wb')
                                    pickle.dump(database, Save)
                                    Save.close()
                                    break
                break
            if inp == '2':
                while 1:
                    inp_price_cartridge = input('Введите цену картриджа:')
                    if not inp_price_cartridge.isdigit():
                        print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                    else:
                        print('.....Назначена цена картриджа:', inp_price_cartridge)
                        inp_sellprice = input('Введите, почём хотите продать:')
                        if not inp_sellprice.isdigit():
                            print('ВВОДИТЬ ТОЛЬКО ЧИСЛО:')
                        else:
                            print('.....Назначена цена продажи картриджа:', inp_sellprice)
                            cartridge.price_cartridge = int(inp_price_cartridge)
                            cartridge.sellprice = int(inp_sellprice)
                            cartridge.tax = ((cartridge.sellprice - cartridge.price_cartridge) * 0.15) // 1
                            cartridge.profit = cartridge.sellprice - cartridge.tax - cartridge.price_cartridge
                            cartridge.cost = cartridge.tax + cartridge.price_cartridge

                            # Запикливаем результаты подсчётов в БД файла 2, сохраняем их и закрываем его
                            database2 = {1: cartridge.price_cartridge,
                                         2: cartridge.sellprice,
                                         3: cartridge.tax,
                                         4: cartridge.cost,
                                         5: cartridge.profit}
                            Save = open('pc2.pkl', 'wb')
                            pickle.dump(database2, Save)
                            Save.close()
                            break
                break
            if inp == '3':
                break
            else:
                print('ВВЕДИТЕ ЦИФРЫ ИЗ МЕНЮ!!')

        print('.....Выходим в главное меню')
        continue
    else:
        print('НЕКОРРЕКТНЫЙ ВВОД')
        continue
