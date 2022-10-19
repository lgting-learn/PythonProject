import os
import glob
lst=os.listdir()
print('all',lst)
for item in lst:
    if item.endswith('.py'):
        print('py',item)
    elif item.startswith('n') and item.endswith('.txt'):
        print('txt',item)
