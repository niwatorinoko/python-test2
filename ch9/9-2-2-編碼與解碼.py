print('我'.encode('unicode-escape'))

def utf8(data):
    data_byte=data.encode('utf-8') # 引数 data を UTF-8形式のバイト列にエンコードします。
    data2=data_byte.decode('utf-8') # エンコードされたバイト列 data_byte を再び文字列に戻します。
    print('將', data, '經由utf-8編碼後為', data_byte) 
    print('將', data_byte, '經由utf-8解碼後為', data2)
    print(data, '的長度為', len(data)) # len() を用いて、元の文字列とエンコード後のバイト列の長さを比較します。
    print(data_byte, '的長度為', len(data_byte)) 

utf8('我')
utf8("\u6211")