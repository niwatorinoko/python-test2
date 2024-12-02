import string
print('ascii_letters為', string.ascii_letters) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print('ascii_lowercase為', string.ascii_lowercase) #abcdefghijklmnopqrstuvwxyz
print('ascii_uppercase為', string.ascii_uppercase) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
print('digits為', string.digits) #0123456789
print('hexdigits為', string.hexdigits) #0123456789abcdefABCDEF
print('octdigits為', string.octdigits) #01234567
print('punctuation為', string.punctuation) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print("printable.encode('ascii')為", string.printable.encode('ascii')) #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c
print("whitespace.encode('ascii')為", string.whitespace.encode('ascii')) #\t\n\r\x0b\x0c