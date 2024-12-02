import unicodedata

"""
unicodedata.name() を使うと、文字のUnicode名が取得できます。
unicodedata.lookup() を使うと、Unicode名から元の文字を復元できます。
"""

def unicode_name(value):
    name = unicodedata.name(value)
    print('value=', value, 'name=', name)
    return name
def unicode_lookup(name):
    value = unicodedata.lookup(name)
    print('name=', name, 'value=', value)
    return value

name = unicode_name('我')
value = unicode_lookup(name)

name = unicode_name('\u6211')
value = unicode_lookup(name)

name = unicode_name('\U00006211')
value = unicode_lookup(name)

name = unicode_name('\N{CJK UNIFIED IDEOGRAPH-6211}')
value = unicode_lookup(name)
