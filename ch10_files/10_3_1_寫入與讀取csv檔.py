import csv

with open('99.csv', 'wt', newline='') as fout:
    writer = csv.writer(fout) # 設定一個csv寫入器
    for i in range(1,10):
        for j in range(1,10):
            # writer.writerows([(str(i)+' * '+str(j),str(i*j))])
            writer.writerow([str(i) + ' * ' + str(j), str(i*j)])

with open('99.csv', 'rt') as fin:
    reader = csv.reader(fin) # 設定一個csv讀取器
    rows = [row for row in reader]
    print(rows)