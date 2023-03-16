import csv
import os.path


class VocBook:
    def __init__(self):
        self.header_list = ["序号", "英语词汇", "中文翻译"]
        self.csv_path = '../data/voc_Book.csv'  # csv 文件路径
        self.vb_data = []
        self.vb_init()

    def vb_init(self):
        """初始化单词本"""

        # csv文件不存在则创建；存在则加载
        if not os.path.exists(self.csv_path):
            self.create_new_csv()
        else:
            self.vb_data=self.read_csv()

    def create_new_csv(self):
        """创建新的csv文件"""
        with open(self.csv_path, mode="w", encoding="utf-8-sig", newline="") as wf:
            # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
            writer = csv.DictWriter(wf, self.header_list)
            # 写入 header
            writer.writeheader()

    def read_csv(self):
        """读取已有的csv文件"""
        lst = []
        with open(self.csv_path, encoding="utf-8-sig", mode="r") as rf:
            # 基于打开的文件，创建csv.DictReader实例
            reader = csv.DictReader(rf)
            # 输出信息
            for row in reader:
                lst.append(dict(row))
            print(lst)
        return lst


    def get_current_rows(self):
        """获取csv文件总行数"""
        return sum(1 for line in open(self.csv_path, encoding='utf-8'))

    def add(self, word, trans):
        """收藏单词"""
        with open(self.csv_path, mode="a", encoding="utf-8-sig", newline="") as wf:
            # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
            writer = csv.DictWriter(wf, self.header_list)
            row = {'序号': f'{self.get_current_rows()}', '英语词汇': f'{word}', '中文翻译': f'{trans}'}
            writer.writerow(row)
            self.vb_data.append(row)

    def clear_vb_data(self):
        """清空单词本"""
        self.vb_data.clear()
        with open(self.csv_path, mode="w", encoding="utf-8-sig", newline="") as wf:
            # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
            writer = csv.DictWriter(wf, self.header_list)
            # 写入 header
            writer.writeheader()

    def delete_one_row(self,row):
        self.vb_data.pop(row)
        self.load_data()

    def reload_data(self):
        for i in range(len(self.vb_data)):
            self.vb_data[i]['序号'] = f'{i+1}'
        self.load_data()

    def load_data(self):
        with open(self.csv_path, mode="w", encoding="utf-8-sig", newline="") as wf:
            # 基于打开的文件，创建 csv.DictWriter 实例，将 header 列表作为参数传入。
            writer = csv.DictWriter(wf, self.header_list)
            # 写入 header
            writer.writeheader()
            writer.writerows(self.vb_data)



voc_book = VocBook()


