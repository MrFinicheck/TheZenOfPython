#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys


if __name__ == '__main__':
    # Список личностей.
    persons = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        match command:
            case 'exit':
                break

            case 'add':
                # Запросить данные о личности.
                name = input("Фамилия и имя? ")
                zodiac_sign = input("Знак Зодиака? ")
                birth_date = input("Дата рождения? ")

                # Создать словарь.
                person = {
                    'name': name,
                    'zodiac_sign': zodiac_sign,
                    'birth_date': birth_date
                }

                # Добавить словарь в список.
                persons.append(person)

                # Отсортировать список в случае необходимости.
                if len(persons) > 1:
                    persons.sort(key=lambda item: item.get('zodiac_sign', ''))

            case 'list':
                # Заголовок таблицы.
                line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
                )
                print(line)

                # Вывести данные о всех личностях.
                for idx, person in enumerate(persons, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                            idx,
                            person.get('name', ''),
                            person.get('zodiac_sign', ''),
                            person.get('birth_date', 0)
                        )
                    )
                print(line)

            case 'select':

                # Разбить команду на части для выделения месяца.
                parts = command.split(' ', maxsplit=1)

                # Получить требуемый месяц.
                month = int(parts[1])

                # Инициализировать счетчик.
                count = 0

                # Проверить сведения личностей из списка.
                for person in persons:
                    if month == int(person.get("birth_date").split('.')[1]):
                        count += 1
                        print(
                            '{:>4}: {}, {}, {}'.format(count, person.get('name', ''), person.get("zodiac_sign", ''), person.get("birth_date", ''))
                        )

                # Если счетчик равен 0, то личности не найдены.
                if count == 0:
                    print("Личности с этим месяцем не найдены.")

            case 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить личность;")
                print("list - вывести список личностей;")
                print("select <стаж> - запросить личностей с этим месяцем;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)




