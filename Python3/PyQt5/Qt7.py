# -*- coding: utf-8 -*-
"""
"""
import sys

from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication, QListView,QWidget,QVBoxLayout

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        QStandardItemModel
        items = []
        for i in range(1,50):
            items.append("Application %d" % i)

        list = QListView(self)
        model = QStandardItemModel(list)
        for i in items:
            row = QStandardItem(i)
            row.setCheckable(True)
            model.appendRow(row)


        list.setWindowTitle('Example List')
        list.resize(200,150)
        list.setModel(model)

        layout = QVBoxLayout()
        layout.addWidget(list)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = mainWindow()
    sys.exit(app.exec_())