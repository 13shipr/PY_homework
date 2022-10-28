import os
os.system('clear')

# text = 'Съешь ещёабв этих мягабвких французских булок, да выпей жеабв чаю'
# lst = text.split()
# for item in lst:
#     if 'абв' in item:
#         lst.remove(item)
# print(lst)

text = 'Съешь ещёабв этих мягабвких французских булок, да выпей жеабв чаю'
print(text, '\n =>', *filter(lambda x: "абв" not in x, [i for i in text.split()]))
