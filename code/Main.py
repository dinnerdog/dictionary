import csv
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QWidget, QAbstractItemView
from window1 import Ui_HomePage
from window2_recite import Ui_ChildWindow_2
from window3_search import Ui_ChildWindow_3
from window4_vbook import Ui_ChildWindow_4

### 导入爬虫函数-爬取翻译网站
from Crawler_BaiDu import crawler_search_BaiDu
from Crawler_WangYi import crawler_search_WangYi

from Dictionary import dictionary
from ReciteThread import Recite_Thread
from VocBook import voc_book


class MainWindow(QMainWindow, Ui_HomePage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.setWindowFlags(Qt.Qt.CustomizeWindowHint)  # 去掉标题栏的

        # 一定要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗,可能会出现子窗口闪退的问题!!!
        self.ChildWindow_2 = ChildWindow_2()
        self.ChildWindow_3 = ChildWindow_3()
        self.ChildWindow_4 = ChildWindow_4()

        self.pushButtonRecite.clicked.connect(self.slot_Open_ChildWin_2)
        self.pushButtonSearch.clicked.connect(self.slot_Open_ChildWin_3)
        self.pushButtonWBook.clicked.connect(self.slot_Open_ChildWin_4)
        self.pushButtonQuit.clicked.connect(self.close)

    def slot_Open_ChildWin_2(self):
        self.hide()
        self.ChildWindow_2.show()

    def slot_Open_ChildWin_3(self):
        self.hide()
        self.ChildWindow_3.show()

    def slot_Open_ChildWin_4(self):
        self.hide()
        self.ChildWindow_4.re_init()
        self.ChildWindow_4.show()


class ChildWindow_2(QMainWindow, Ui_ChildWindow_2):
    """背单词窗口"""

    def __init__(self):
        super().__init__()
        self.qss_ori = """
        QPushButton{background-color:rgb(225, 225, 225);border: 1px solid rgb(173, 173, 173);border-radius: 5px}
        QPushButton:hover{background-color:rgb(229, 241, 251);border: 1px solid rgb(0, 120, 215);border-radius: 5px}
        """
        self.qss_change_pink = """
        QPushButton{background-color:rgb(255, 146, 181);border: 1px solid rgb(173, 173, 173);border-radius: 5px}
        QPushButton:hover{background-color:rgb(255, 146, 181);border: 1px solid rgb(173, 173, 173);border-radius: 5px}
        """
        self.qss_change_yellow = """
        QPushButton{background-color:rgb(240, 255, 97);border: 1px solid rgb(173, 173, 173);border-radius: 5px}
        QPushButton:hover{background-color:rgb(240, 255, 97);border: 1px solid rgb(173, 173, 173);border-radius: 5px}
        """
        self.setupUi(self)
        self.recite_thread = Recite_Thread()

        self.my_init()
        self.qss_init()
        self.recite_thread.start()

    def my_init(self):
        self.recite_thread.mysignal.connect(self.slot_update_title)
        self.recite_thread.mysignal_button_pink.connect(self.slot_button_pink)
        self.recite_thread.mysignal_button_white.connect(self.slot_button_white)
        self.recite_thread.mysignal_button_yellow.connect(self.slot_buttom_yellow)

        self.label_2.setText(str(dictionary.word_num))
        self.comboBox.activated.connect(self.slot_print)
        self.pushButton.clicked.connect(self.slot_GiveAnswer_0)
        self.pushButton_2.clicked.connect(self.slot_GiveAnswer_1)
        self.pushButton_3.clicked.connect(self.slot_GiveAnswer_2)
        self.pushButton_4.clicked.connect(self.slot_GiveAnswer_3)

    def qss_init(self):
        self.pushButton.setStyleSheet(self.qss_ori)
        self.pushButton_2.setStyleSheet(self.qss_ori)
        self.pushButton_3.setStyleSheet(self.qss_ori)
        self.pushButton_4.setStyleSheet(self.qss_ori)

    def slot_buttom_yellow(self):
        temp = self.recite_thread.given_answer
        if temp == 0:
            self.pushButton.setStyleSheet(self.qss_change_yellow)
        if temp == 1:
            self.pushButton_2.setStyleSheet(self.qss_change_yellow)
        if temp == 2:
            self.pushButton_3.setStyleSheet(self.qss_change_yellow)
        if temp == 3:
            self.pushButton_4.setStyleSheet(self.qss_change_yellow)

    def slot_button_pink(self):
        self.label_3.setText(str(self.recite_thread.current_num))
        temp = self.recite_thread.right_answer
        if temp == 0:
            self.pushButton.setStyleSheet(self.qss_change_pink)
        if temp == 1:
            self.pushButton_2.setStyleSheet(self.qss_change_pink)
        if temp == 2:
            self.pushButton_3.setStyleSheet(self.qss_change_pink)
        if temp == 3:
            self.pushButton_4.setStyleSheet(self.qss_change_pink)

    def slot_button_white(self):
        self.pushButton.setStyleSheet(self.qss_ori)
        self.pushButton_2.setStyleSheet(self.qss_ori)
        self.pushButton_3.setStyleSheet(self.qss_ori)
        self.pushButton_4.setStyleSheet(self.qss_ori)

    def slot_GiveAnswer_0(self):
        self.recite_thread.given_answer = 0

    def slot_GiveAnswer_1(self):
        self.recite_thread.given_answer = 1

    def slot_GiveAnswer_2(self):
        self.recite_thread.given_answer = 2

    def slot_GiveAnswer_3(self):
        self.recite_thread.given_answer = 3

    def slot_update_title(self):
        self.label_5.setText(str(self.recite_thread.selected_titles[self.recite_thread.right_answer][0]))
        self.pushButton.setText(str(self.recite_thread.selected_titles[0][1]))
        self.pushButton_2.setText(str(self.recite_thread.selected_titles[1][1]))
        self.pushButton_3.setText(str(self.recite_thread.selected_titles[2][1]))
        self.pushButton_4.setText(str(self.recite_thread.selected_titles[3][1]))

    def slot_print(self):
        self.label_5.setText(self.comboBox.currentText())

    # # 退出系统窗口 X 绑定函数事件
    # def closeEvent(self, e):
    #     self.box = QMessageBox(QMessageBox.Warning, "系统提示信息", "是否退出？")
    #     qyes = self.box.addButton(self.tr("是"), QMessageBox.YesRole)
    #     qno = self.box.addButton(self.tr("否"), QMessageBox.NoRole)
    #     self.box.exec_()
    #     if self.box.clickedButton() == qyes:
    #         e.accept()
    #         QWidget.closeEvent(self, e)
    #         MainWindow.show()
    #         # sys.exit().accept()
    #     else:
    #         e.ignore()

    def closeEvent(self, e):

        MainWindow.show()


class ChildWindow_3(QMainWindow, Ui_ChildWindow_3):
    """查单词窗口"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.re_init()
        self.voc_book = voc_book
        self.source = 0

    def re_init(self):
        self.pushButton.clicked.connect(self.slot_clear)
        self.pushButton_2.clicked.connect(self.slot_Search)
        self.comboBox.activated.connect(self.slot_ChangeSource)
        self.pushButton_3.clicked.connect(self.slot_collect_into_vocBook)

    def slot_ChangeSource(self):
        if self.comboBox.currentText() == "有道翻译":
            self.source = 0
        if self.comboBox.currentText() == "百度翻译":
            self.source = 1

    def slot_clear(self):
        """清楚文本内容"""
        self.textEdit.clear()
        self.lineEdit.clear()

    def slot_collect_into_vocBook(self):
        """收藏单词接口"""
        if self.lineEdit.text() and self.textEdit.toPlainText()!='查询失败':
            self.voc_book.add(word=self.lineEdit.text(),trans=self.textEdit.toPlainText().rstrip())


    def slot_Search(self):
        """查单词接口"""
        self.textEdit.setText(self.crawler_Search(self.source))  # 获取lineEdit内容

    def crawler_Search(self,source):
        """选择爬虫网站"""
        if source == 0:
            return crawler_search_WangYi(self.lineEdit.text())  # 网易有道翻译
        if source == 1:
            return crawler_search_BaiDu(self.lineEdit.text())   # 百度翻译

    def closeEvent(self, e):
        """关闭窗口动作"""
        MainWindow.show()


class ChildWindow_4(QMainWindow, Ui_ChildWindow_4):
    """单词本窗口"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.voc_book = voc_book
        self.delete_item_row = 0
        self.re_init()
        # 信号与槽连接
        self.pushButton.clicked.connect(self.slot_delete_one_row)
        self.pushButton_2.clicked.connect(self.slot_clear_vbdata)
        self.tableWidget.itemClicked.connect(self.slot_change_delete_num)


    def re_init(self):
        self.label_3.setText(str(self.voc_book.get_current_rows()-1))
        # 设置表格行数和列数
        self.tableWidget.setRowCount(self.voc_book.get_current_rows()-1)
        self.tableWidget.setColumnCount(3)
        # 添加列的标题
        self.tableWidget.setHorizontalHeaderLabels(self.voc_book.header_list)

        # 设置列宽度
        self.tableWidget.setColumnWidth(0, 90)
        self.tableWidget.setColumnWidth(1, 160)
        self.tableWidget.setColumnWidth(2, 188)
        # 添加内容
        # self.voc_book.vb_data=self.voc_book.read_csv()
        if self.voc_book.get_current_rows() > 1:
            for row in range(0,self.voc_book.get_current_rows()-1):
                item0 = QTableWidgetItem(self.voc_book.vb_data[row]['序号'])
                item0.setTextAlignment(Qt.AlignCenter)
                item1 = QTableWidgetItem(self.voc_book.vb_data[row]['英语词汇'])
                item1.setTextAlignment(Qt.AlignCenter)
                item2 = QTableWidgetItem(self.voc_book.vb_data[row]['中文翻译'])
                item2.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row, 0, item0)
                self.tableWidget.setItem(row, 1, item1)
                self.tableWidget.setItem(row, 2, item2)

                # 设置禁止编辑
                self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

                # 点击一行选整行
                self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

                # 调整行列大小和内容自动匹配
                # self.tableWidget.resizeColumnsToContents()
                # self.tableWidget.resizeRowsToContents()

                # 可以控制表格头行和列显示和隐藏
                # self.tableWidget.horizontalHeader().setVisible(False)
                self.tableWidget.verticalHeader().setVisible(False)


    def slot_clear_vbdata(self):
        self.voc_book.clear_vb_data()
        self.re_init()

    def slot_change_delete_num(self,item):
        row = item.row()  # 获取行数
        self.delete_item_row = row


    def slot_delete_one_row(self):
        self.voc_book.delete_one_row(self.delete_item_row)
        self.voc_book.reload_data()
        self.re_init()

    def closeEvent(self, e):
        """关闭该窗口，显示主窗口"""
        MainWindow.show()


if __name__ == '__main__':
    # 主界面
    app = QApplication(sys.argv)
    # 创建主窗口
    MainWindow = MainWindow()
    # 显示窗口
    MainWindow.show()
    # 退出主程序
    sys.exit(app.exec_())









