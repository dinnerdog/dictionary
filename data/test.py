# 导入 csv 库
import csv

# 创建 header 列表
header_list = ["编号", "英语词汇", "中文翻译"]

# 创建数据列表，列表的每个元素都是字典
data_list = [
    {"编号": "1","英语词汇": 'a',"中文翻译": 'A'},
    {"编号": "2","英语词汇": 'b',"中文翻译": 'B'},
    {"编号": "3", "英语词汇": 'c', "中文翻译": 'C'},
]

# 以写方式打开文件。注意添加 newline=""，否则会在两行数据之间都插入一行空白。
with open("voc_Book.csv", mode="w", encoding="utf-8-sig", newline="") as f:
    # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
    writer = csv.DictWriter(f, header_list)

    # 写入 header
    writer.writeheader()

    # 写入数据
    writer.writerow(data_list[0])

with open("voc_Book.csv", encoding="utf-8-sig", mode="r") as f:

    # 基于打开的文件，创建csv.DictReader实例
    reader = csv.DictReader(f)

    # 输出信息
    for row in reader:
        print(f'编号:{row["编号"]}, 英语词汇:{row["英语词汇"]}, 中文翻译:{row["中文翻译"]}')


