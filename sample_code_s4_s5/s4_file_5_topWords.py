# -*- coding: utf-8 -*-
"""
Count lines, words, and characters and
Find top five most occurred words

"""

in_filename = 's4_read.txt'

line_cnt = word_cnt = char_cnt = 0
word_dict=  {}

with open(in_filename , 'r') as f:
    for line in f:
        line_cnt += 1
        words = line.strip('\n').split(' ')
        word_cnt += len(words)
        char_cnt += sum([len(w) for w in words])
        for w in words:
            word_dict[w] = word_dict.setdefault(w, 0) + 1
            # if w not in word_dict:
            #     word_dict[w] = 1
            # else:
            #     word_dict[w] += 1
#print(word_dict)
        
print('\n%d line(s)' % (line_cnt))
print('%d word(s)' % (word_cnt))
print('%d character(s)\n' % (char_cnt))

w_sorted = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
print(w_sorted[0:5])

"""
stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
"""