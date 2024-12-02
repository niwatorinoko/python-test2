# Read file line by line

fin = open('poem.txt','rt', encoding='utf-8')
# =============================================================================
# for line in fin:
#     print(line.rstrip())
# =============================================================================

lines = fin.readlines() # Read all lines as a list
print(type(lines))
for l in lines:
    print(l.rstrip())

fin.close()