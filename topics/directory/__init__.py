from pathlib import Path

'''
path = Path("emails")
# print(path.exists())
# print(path.mkdir())
# print(path.rmdir())
# print(path.glob('*.py'))
'''

path = Path()

for file in path.glob('*.py'):
    print(file)
