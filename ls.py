import glob
import pathlib


'''folder = pathlib.Path('C:/Users/mario/Downloads')
folder.glob('*.txt')
print(folder.glob('*.txt'))'''



items = []
folder = glob.glob('C:\Program Files (x86)\Samsung\Samsung Magician\*.dll')
items.append(folder)
print(items)





