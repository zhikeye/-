# -*- coding: utf-8 -*-
"""
QListWidget
"""
import sys
from PyQt5.QtWidgets import QApplication, QListWidget,QWidget,QVBoxLayout



class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        items = []
        for i in range(1,50):
            items.append("Application %d" % i)

        listBox = QListWidget()
        listBox.insertItems(0,items)
        listBox.insertItem(1,'insert %d' % listBox.__len__())
        listBox.resize(200,150)
        listBox.move(10,10)
        layout = QVBoxLayout()
        layout.addWidget(listBox)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = mainWindow()
    sys.exit(app.exec_())
