# jabber = open(
# #     'E:\Projekty\GitHub\PythonExcercises\FIleIO\original.txt','r'
# # )   # 'r' stands for read only
# #
# # for line in jabber:
# #     if 'jabberwock' in line.casefold():
# #         print(line, end='')
# #
# # jabber.close()  # ALWAYS close the file
# #
# # # we can also use relative path if this is in the program
# # # like: open(original.txt)

with open("original.txt","r") as jabber:
    for line in jabber:
        if 'JAB' in line.upper():
            print(line, end='')

# with statement ensures file closing

# *******************

# lines of file read to the list
with open("original.txt","r") as jabber2:
    lines = jabber2.readlines()
print(lines)

for line in lines:
    print(line,end='')