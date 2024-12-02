
import re

def count_puncs(s):
  # 找尋標點符號
  puncs = set(re.findall(r"\W", s))
  print(puncs)

  punc_dict = {}
  for p in sorted(puncs, key=s.index):
    punc_dict[p] = s.count(p)

  # print(f"\n總共使用標點符號： {len(puncs)} 種")
  print("\n使用最多次的10種標點符號:")
  for k, v in sorted(punc_dict.items(), key=lambda x: -x[1])[:10]:
    print(f'{k:2s}: {v:>2d}')
  print()
  input("Press any key to continue ...")
  
  
def count_zh_words(s):
  # 找尋標點符號
  puncs = set(re.findall(r"\W", s))
  print(puncs)

  # escape necessary for ( ) [ ] - + *...
  puncs = ''.join(map(re.escape, list(puncs))) + '_'
  pat = r'[%s]+\ *' % puncs  
  print(pat)

  # 移除標點符號,
  s1 = re.sub(pat, "", s)
  s1 = set(re.findall(r"[^\W]", s)) # using regular expressions
  # print(s1)
  word_set = set(s1)
  
  # 照原文中出現順序排序
  word_set = sorted(word_set, key=s.index)
  zh_words = [w for w in word_set if w.isascii() == False]
  # print(zh_words)

  word_dict = {}
  for w in zh_words:
    word_dict[w] = s.count(w)

  print("\n使用最多次的中文字元:")
  for k, v in sorted(word_dict.items(), key=lambda x: -x[1])[:10]:
    print(f'{k}: {v}')
  print()


try:
  with open('test02_Q3_data.txt', 'r', encoding='utf-8') as f:
    input_str = f.read()
    # count_zh_words(input_str)
    count_puncs(input_str)
except Exception as e:
  print(e)

