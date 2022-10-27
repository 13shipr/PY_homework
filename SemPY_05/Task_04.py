# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

import os
os.system('clear')

def rle_encode(string):
    encoding = ''
    left_elem = ''
    count = 1
    if not string: return ''
    for elem in string:
        if elem != left_elem:
            if left_elem: encoding += str(count) + left_elem
            count = 1
            left_elem = elem
        else: count += 1
    else: encoding += str(count) + left_elem
    return encoding

def rle_decode(string):
    decode = ''
    count = ''
    for elem in string:
        if elem.isdigit(): count += elem
        else:
            decode += elem * int(count)
            count = ''
    return decode

string = 'aaaabbbeeeerttwiimssst'
print(f'String => {string}\nEncode => {rle_encode(string)}\nDecode => {rle_decode(rle_encode(string))}')