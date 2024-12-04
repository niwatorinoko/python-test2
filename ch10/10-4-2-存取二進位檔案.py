bindata = bytes(range(0,32))
#バイナリ書き込みモード (wb)
with open('binfile','wb') as fout:
    fout.write(bindata)
#バイナリ読み込みモード (rb)
with open('binfile','rb') as fin:
    binary = fin.read()
    print(binary)