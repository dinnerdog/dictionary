import os

from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from Dictionary import dictionary
import random
import sys
import time
import shutil
import xlrd

class Recite_Thread(QThread):
    mysignal = QtCore.pyqtSignal()
    mysignal_button_pink = QtCore.pyqtSignal()
    mysignal_button_white = QtCore.pyqtSignal()
    mysignal_button_yellow = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.data = dictionary.data
        self.right_answer = -1
        self.given_answer = -1
        self.current_num = 0
        self.selected_titles = []


    def run(self):
        while True:
            self.update_titiles()
            while True:
                time.sleep(0.2)
                if self.given_answer >= 0:
                    if self.given_answer == self.right_answer:
                        self.answer_correctly()
                    else:
                        self.answer_wrongly()
                    break

    def update_titiles(self):
        self.selected_titles = random.sample(self.data, k=4)
        self.given_answer = -1
        self.right_answer = random.randint(0, 3)
        self.mysignal.emit()

    def answer_correctly(self):
        self.current_num += 1
        self.mysignal_button_pink.emit()
        time.sleep(0.2)
        self.mysignal_button_white.emit()


    def answer_wrongly(self):
        self.mysignal_button_yellow.emit()
        time.sleep(2)
        self.mysignal_button_white.emit()


