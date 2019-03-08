from pathlib import Path
import csv


#新建csv文件并且写入内容
p = Path("/tmp/csvtest/test.csv")

csv_body = '''\
id,name,age,comment
1,zs,18,"I am 31"
2,ls,20,"This is a csv txt"
3,www,28,"hello

sunny
"
'''

p.parent.mkdir(parents=True,exist_ok=True) #新建csv目录
p.write_text(csv_body) # 将内容写入csv文件


#显示csv文件里的内容
csvname = "/tmp/csvtest/test.csv"
with open(csvname,newline='') as f:
    reader = csv.reader(f)
    print(reader)
    for row in reader:
        print(row)

        
#将数据追加写入csv文件        
rows = [
    ['4', 'cat', '18', 'I am 31'],
    ['5', 'll', '20', 'This is a csv txt'],
    ['6', 'http', '28', 'hello\n\nsunny\n'],
    (7,),
    [(1,2,3),(1,5,9)]
]

row = rows[0]

p = Path(csvname)
with open(str(p),'a',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row) #这里是仅写入一行row[0]
    writer.writerows(rows) # 这里是将rows的全部内容写入到csv文件里
