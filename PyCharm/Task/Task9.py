#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Заполняем список классов.
    school = {
        '1а': 25,
        '1б': 20,
        '2б': 18,
        '6а': 30,
        '7в': 22
    }

    # В одном из классов изменилось количество учащихся.
    school['6а'] = 29

    # В школе появился новый класс.
    school['9г'] = 27

    # В школе был расформирован (удален) другой класс.
    del school['7в']

    # Находим сумму.
    all_students = sum(school.values())

    # Вывод полученной суммы.
    print(f"Общее количество учащихся в школе: {total_students}")



