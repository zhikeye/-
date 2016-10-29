# -*- coding: utf-8 -*-
"""
显示一个窗口提示框，我们可以为任何部件添加一个气泡状的帮助信息。
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont, QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #这一静态方法用于设置呈现在提示框内的文字字体和大小，在这里我们使用 10px 的 Sans Serif 字体。
        QToolTip.setFont(QFont('SansSerif', 10))
        #setToolTip 方法创建了一个提示，这里可以使用 RTF 格式
        self.setToolTip('This is a <b>QWidget</b> widget')
        #我们创建了一个按钮控件（push button），并为它设置了一条提示信息
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #我们使用上面两条语句设置按钮的大小，调整按钮在窗口里的摆放位置，sizeHint 方法给定按钮空间建议的尺寸
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())