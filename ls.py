import glob
import pathlib
from datetime import datetime
'''
folder = pathlib.Path('C:/Users/mario/Downloads')
folder.glob('*.txt')
list(folder.glob('*.txt'))



items = []
folder = glob.glob('C:\Program Files (x86)\Samsung\Samsung Magician\*.dll')
items.append(folder)
print(items)'''

p = pathlib.Path('.')
items = p.glob('**/*')
print(f'Mode\tLastWriteTime          \tLength   \tName')
print(f'----\t-------------          \t------   \t----')
for idx, item in enumerate(items):
    if '.git' in item.parts:
        continue
    name = item.name
    last_write_time = item.stat().st_mtime
    dt = datetime.fromtimestamp(int(last_write_time))
    dt_str = dt.strftime('%m/%d/%Y %H:%M %p')
    
    length = item.stat().st_size
    attribute = item.stat().st_mode
    print(f'{attribute}\t{dt_str}\t{length:8}\t{name}')

import math
message = 'Hello world'
fill = ' '
align = '<'
width = 20
print(f'{message:{fill}{align}{width}}')
 
'''
items = pathlib.Path().glob(**)
for item in items:
    print(item)'''


