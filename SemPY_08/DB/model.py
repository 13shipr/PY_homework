import json
import csv
from pathlib import Path


def get_info ():
    data = [
        input('Введите фамилию: '),
        input('Введите имя: '),
        input('Введите номер телефона: '),
        input('Введите должность: '),
        input('Введите зарплату: '),
        input('Введите комментарий: ')
    ]
    # last_name = input('Введите фамилию: ')
    # data.append(last_name)
    # first_name = input('Введите имя: ')
    # data.append(first_name)
    # phone_number = input('Введите номер мобильного телефона: ')
    # data.append(phone_number)
    # description = input('Введите описание: ')
    # data.append(description)
    print('Запись сохранена')
    return data

def create_db ():
    file = 'Database.csv'
    with open (file, 'w', encoding = 'utf-8') as csv_file:
        csv_file.write(f'Фамилия;Имя;Номер телефона;Должность;Зарплата;Комментарий\n')

def write_json():
    data = get_info()
    file = 'Database1.json'
    with open(file, 'a', encoding= 'utf-8') as bd:
        base = {
            'Фамилия': data[0],
            'Имя': data[1],
            'Телефон': data[2],
            'Должность': data[3],
            'Зарплата': data[4],
            'Комментарий': data[5],
        }
        add_base = []
        add_base.append(base)
        bd.write(json.dumps(add_base) + '\n')
        bd.close()

def load_json():
    file = 'Database1.json'
    data_base = []
    with open(file, 'r', encoding='utf-8') as bd:
        # json_data = json.load(file)
        for user in bd:
            temp = json.loads(user.strip())
            data_base.append(temp)
            # print('Фамилия: ' + user[0])
            # print('Имя: ' + user[1])
            # print('Телефон: ' + user[2])
            # print('Должность: ' + user[3])
            # print('Зарплата: ' + user[4])
            # print('Комментарий: ' + user[5])
            # print('\n')
    return data_base

def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'Database01.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

def write_csv ():
    data = get_info()
    file = 'Database.csv'
    with open (file, 'a', encoding = 'utf-8') as bd:
        bd.write(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]}\n')
    return data




def search():
    res = []
    with open('Database.csv', "r") as file:
        base = file.read().split('\n')
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if set(lists).issubset(line) and len(line) > 1:
                res.append(line)
    return res


def write_txt ():
    
    file = 'Database.txt'
    with open (file, 'a', encoding = 'utf-8') as bd:
        bd.write(f'Фамилия: {data[0]}\nИмя: {data[1]}\nНомер телефона: {data[2]}\nОписание: {data[3]}\n\n')
    return 'ok'



def edit():
    res = []
    record = 0
    with open('Database.csv', "w") as file:
        base = file.read().split('\n')
        for item in base:
            line = item.split(';')
            if data[0] == line[0] and len(line) > 1:
                res.append(data)
                record +=1
            elif len(line) > 1:
                res.append(line)

def imp_bd(name):
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    count = 0
    if name[0] != '':
        with open(name[0], 'r') as file0in:
            data0 = json.load(file0in)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file0out:
            w = csv.DictWriter(file0out, fieldnames=dict_fields, delimiter=';', lineterminator='\n')
            w.writerows(data0)
        count += len(data0)
    if name[1] != '':  
        with open(name[1], 'r') as file1in:
            csv_reader = csv.reader(file1in, delimiter=';', lineterminator='\n')
            for row in csv_reader:
                temp = {}
                temp['СНИЛС'] = int(row[0])
                temp['Фамилия'] = row[1]
                temp['Имя'] = row[2]
                temp['Отчество'] = row[3]
                temp['Рождение'] = row[4]
                temp['Профессия'] = row[5]
                temp['Оклад'] = int(row[6])
                temp['Адрес'] = row[7]
                temp['Сотовый'] = int(row[8])
                temp['Городской'] = int(row[8])
                data1.append(temp)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file1out:
            w = csv.DictWriter(file1out, fieldnames=dict_fields, delimiter=';', lineterminator='\n')
            w.writerows(data1)
        count += len(data1)
    if name[2] != '':  
        with open(name[2], 'r') as file2in:
            csv_reader = csv.reader(file2in, delimiter=',', lineterminator='\n')
            for row in csv_reader:
                temp = {}
                temp['СНИЛС'] = int(row[0])
                temp['Фамилия'] = row[1]
                temp['Имя'] = row[2]
                temp['Отчество'] = row[3]
                temp['Рождение'] = row[4]
                temp['Профессия'] = row[5]
                temp['Оклад'] = int(row[6])
                temp['Адрес'] = row[7]
                temp['Сотовый'] = int(row[8])
                temp['Городской'] = int(row[8])
                data2.append(temp)
        dict_fields = ['СНИЛС', 'Фамилия', 'Имя', 'Отчество', 'Рождение', 'Профессия', 'Оклад', 'Адрес', 'Сотовый', 'Городской']
        with open(BASE,'a', encoding='cp1251') as file2out:
            w = csv.DictWriter(file2out, fieldnames=dict_fields, delimiter=';', lineterminator='\n')
            w.writerows(data2)
        count += len(data2)





