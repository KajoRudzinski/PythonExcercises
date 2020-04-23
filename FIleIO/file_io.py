jabber = open(
    'E:\Projekty\GitHub\PythonExcercises\FIleIO\original.txt','r'
)   # 'r' stands for read only

for line in jabber:
    if 'jabberwock' in line.casefold():
        print(line, end='')

jabber.close()  # ALWAYS close the file

# we can also use relative path if this is in the program
# like: open(original.txt)