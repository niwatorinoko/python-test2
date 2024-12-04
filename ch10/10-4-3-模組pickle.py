import pickle


mylist = [a for a in range(1,10)]
#バイト列に変換して保存（シリアライズ）
with open('pickle','wb') as fout:
    pickle.dump(mylist,fout)
#バイト列を元のオブジェクトに復元（デシリアライズ） するために使います。
with open('pickle','rb') as fin:
    p = pickle.load(fin)
    print(p)