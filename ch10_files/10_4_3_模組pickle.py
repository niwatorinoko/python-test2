import pickle

mylist = [a for a in range(1,10)]

# pickle.dump(data, file): dump data as pickle format to file
with open('data.pickle','wb') as fout:
    pickle.dump(mylist, fout)

# pickle.load(file): read pickled file
with open('data.pickle','rb') as fin:
    p = pickle.load(fin)
    print(p)