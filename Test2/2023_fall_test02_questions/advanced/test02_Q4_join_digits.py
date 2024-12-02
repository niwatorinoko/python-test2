
# Use only list comprehension (no loops) how would you change a list of
# integers such as [-2, 3, 4, 5] and [9, 9, 1, 9] into their actual numbers
# -2345 and 9919

"""
Get get a list of numbers and convert into their actual number
"""
# -1, 3, 4

def join_digits(l):
  n = ''.join([str(x).strip() for x in l])
  return n

def main():

  while True:
    s = input("Enter numbers separated by comma(,): ")
  
    s = s.replace(',', ' ').replace(' ', '')

    #if s.isdigit():
    try: 
      int(s)
      print(f'{s} is  a number')
    except ValueError:
    # not int:
      print(f'{s} not a number')
  
main()

