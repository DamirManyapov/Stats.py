#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import requests
import time
import datetime

def main():
    parser = argparse.ArgumentParser(description='Скачивает новую порцию статистики и добавляет анализ')
    #parser.add_argument('filename', help='Json файл с данными о url', type=str)
    args = parser.parse_args()

########## Собираем URL ##########

now_time = datetime.datetime.now() # Текущая дата со временем

time_start = datetime.timedelta(days=7) # Время начала периода
time_finish = datetime.timedelta(days=1) # Время конца периода

date_start = (now_time-time_start) # Вычисляем необходимое нам время начала периода
date_finish = (now_time-time_finish) # Вычисляем необходимое время конца периода

date_start = date_start.strftime("%d.%m.%Y") # Формируем дату начала в необходимом нам формате 
date_finish = date_finish.strftime("%d.%m.%Y") # Формируем дату конца в необходимом нам формате 

print(date_start)
print(date_finish)

# TODO Учесть временную разницу с МСК, не критично но может повлиять

url = 'https:url'

url = '{url}{date_start}-{date_finish}.xls'.format(url=url, date_start=date_start, date_finish=date_finish)

name_file = 'stats-{date_start}-{date_finish}.xls'.format(date_start=date_start, date_finish=date_finish)
print(name_file)
print(url)

########## Скачиваем файл данных ########## 

# TODO Сделать прогресс бар :)

name_file = 'stats-{date_start}-{date_finish}.xls'.format(date_start=date_start, date_finish=date_finish)

print("Скачиваем новую порцию статистики")
r = requests.get(url)
with open(name_file, "wb") as code:
    code.write(r.content)

########## Работаем с Excel ##########

if __name__ == '__main__':
    main()
