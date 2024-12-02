import csv

with open('99.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    for i in range(1,10):
        for j in range(1,10):
            # write one row at a time
            writer.writerow([str(i),str(j),str(i*j)])

with open('99.csv', 'r') as fin:
    # 設定有標題列的csv.DictReader物件
    dict_reader = csv.DictReader(fin, fieldnames=['被乘數','乘數','積'])
    dict_rows = [ d for d in dict_reader ]
    print(dict_rows)
    
    fout = open('99b.csv', 'w', newline='', encoding='utf-8-sig')
    # 設定有標題列的csv.DictWriter物件
    dict_writer = csv.DictWriter(fout, fieldnames=['被乘數','乘數','積'])
    dict_writer.writeheader()           # 寫入標題列
    dict_writer.writerows(dict_rows)    # 寫入all data rows
    fout.close()

# Read data rows
print("\nData Rows ... ")
with open('99b.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    # next(csv_reader) # skip first row

    for row in csv_reader:
        print(row) 