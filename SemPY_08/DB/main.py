import os
os.system('clear')

from os.path import exists
from model import db
from controller import write_csv
from controller import write_txt

path = 'Database.csv'
valid = exists(path)
if not valid:
    db()

write_csv()
write_txt()