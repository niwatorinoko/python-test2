# Read file
# rt:  read a file as text 

# open(filepath, mode, encoding=...)
fin = open('poem.txt','rt', encoding='utf-8')
s = fin.read() # read all as string
print(f'{type(s)} => {s}')

# file point already went to the end of last read
s10 = fin.read(10)
print(s10)

fin.close()
