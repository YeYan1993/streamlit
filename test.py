"""Test scripts to see if the server is working."""

from tiny_notebook import Notebook

print('Notebook')
print(Notebook)
notebook = Notebook()

import time # debug

with Notebook() as write:
    print('Created a Notebook.')
    print('Got write object:', write)
    print('Sleeping for 3 seconds.')
    import time
    time.sleep(3)
print('Sleeping for another second...')
time.sleep(1)