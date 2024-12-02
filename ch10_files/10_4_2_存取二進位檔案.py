bindata = bytes(range(0,32))

with open('binfile','wb') as fout:
    fout.write(bindata)

with open('binfile','rb') as fin:
    binary = fin.read()
    print(binary)
    # convert bytes back to integer (or string)
    print([int(x) for x in binary])
    

# encode() vs decode()
s = 'test中文'

encode_s = s.encode('utf-8')
print(encode_s)

print(encode_s.decode())