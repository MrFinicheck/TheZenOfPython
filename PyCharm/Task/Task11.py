#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Создание исходного словаря.
    original_dict = {
        40: 'Питон',
        20: 'Уж',
        28: 'Анаконда',
        30: 'Кобра',
        12: 'Удав'
    }

    # Создание нового словаря "обратного" исходному.
    dict_items = {value: key for key, value in original_dict.items()}

    # Вывод перевернутого словаря
    print(f"Перевернутый словарь: {dict_items}")



    




