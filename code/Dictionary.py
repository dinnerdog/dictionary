import os
import random
import sys
import time
import shutil
import xlrd


class Dictionary:
    """字典类"""
    def __init__(self):
        self.excel_path = r'../data/vocabulary.xls'
        self.excel = xlrd.open_workbook(self.excel_path)
        self.book = self.excel.sheet_by_index(0)
        self.col, self.row = self.book.ncols, self.book.nrows
        self.data = []
        self.dictionary = dict()
        self.word_num = 0
        self.init_data()

    def init_data(self):
        """初始化字典数据"""
        for row in range(self.row):
            self.data.append([i for i in self.book.row_values(row)][0:2])
        self.dictionary = {item[0]: item[1] for item in self.data}
        self.word_num = len(self.data)

dictionary = Dictionary()
