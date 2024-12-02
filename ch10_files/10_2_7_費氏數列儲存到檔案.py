
# print to file
fout = open('fib.txt','wt')

def fib(num):
    count = 1
    a = 1
    b = 1
    print(f'{count:3d} {a}', file=fout)
    while(count < num):
        a, b = b, a+b
        count += 1
        print(f'{count:3d} {a}', file=fout)

fib(100)
fout.close()