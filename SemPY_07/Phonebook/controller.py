from view import get_info

data = get_info()
def write_csv ():
    file = 'Database.csv'
    with open (file, 'a', encoding = 'utf-8') as bd:
        bd.write(f'{data[0]};{data[1]};{data[2]};{data[3]}\n')
    return 'Телефон добавлен'

def write_txt ():
    file = 'Database.txt'
    with open (file, 'a', encoding = 'utf-8') as bd:
        bd.write(f'Фамилия: {data[0]}\nИмя: {data[1]}\nНомер телефона: {data[2]}\nОписание: {data[3]}\n\n')
    return 'ok'