import os
os.system('clear')

import view as v
import model as m
import os.path

path = 'Database.csv'
valid = os.path.exists(path)
if not valid:
    m.create_db()

data = ['','','','','','']
res = []

v.start_menu()
li = int(input('Выберите действие: '))
while li != 0:
    if li == 1:
        # m.search()
        print(*data)
    elif li == 2:
        os.system('clear')
        # m.get_info()
        # m.write_csv()
        m.write_json()
        break
    elif li == 3:
        # m.export_json()
        # m.read_json()
        print(m.load_json())
        break
    else:
        print('\nНеверный ввод, укажите номер действия: ')
    print()

# v.start_full_menu()
# li = int(input('Выберите действие: '))
# while li != 0:
#     if li == 1:
#         os.system('clear')
#     elif li == 2:
#         os.system('clear')
#         data = m.get_info()
#         m.write_csv()
#         break
#     elif li == 3:
#         os.system('clear')
#         v.export_menu()
#         li = int(input('Выберите действие: '))
#         if li == 1:
#             #exp json
#             pass
#         elif li == 2:
#             #exp csv
#             pass
#         elif li == 3:
#             os.system('clear')
#             m.write_txt()
#         else:
#             print('wrong')


# v.start_full_menu()
# li = int(input('Выберите действие: '))


# menu = ''
# while not menu == '0':
#     if os.path.isfile('Database.csv'):
#         v.start_full_menu()
#     else:
#         v.start_menu()
#         if menu == '1':
#             v.import_menu()
#         elif menu == '2':
#             v.get_info()
#         elif menu == '3':
#             exit()












# from view import get_info

# data = get_info()
# def write_csv ():
#     file = 'Database.csv'
#     with open (file, 'a', encoding = 'utf-8') as bd:
#         bd.write(f'{data[0]};{data[1]};{data[2]};{data[3]}\n')
#     return 'Телефон добавлен'

# def write_txt ():
#     file = 'Database.txt'
#     with open (file, 'a', encoding = 'utf-8') as bd:
#         bd.write(f'Фамилия: {data[0]}\nИмя: {data[1]}\nНомер телефона: {data[2]}\nОписание: {data[3]}\n\n')
#     return 'ok'