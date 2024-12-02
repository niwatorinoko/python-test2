# -*- coding: utf-8 -*-
# 9 * 9 Multiplcation table

for x in range(1, 10):
    for y in range(1, 10):
        #print('%d*%d=%2d ' % (y, x, x*y), end=' ')
        print(f'{y}*{x}={x*y:2d}', end='\t')
    print()
    