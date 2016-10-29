# -*- coding: utf-8 -*-
"""
退出按钮
"""
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qtBtn = QPushButton('退出',self)
        qtBtn.clicked.connect(QCoreApplication.instance().quit)
        qtBtn.resize(qtBtn.sizeHint())
        qtBtn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('退出')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
