# -*- coding: utf-8 -*-
"""
PyQt 2 应用程序图标
python 支持面向对象的编码模式，在PyQt5中，我们需要使用这种模式。
面向对象的三个要素是类、数据和方法，在上述代码中，我们创建了一个名为 Example 的新类，Example 继承于 QWidget
类，我们需要调用两个构造函数：第一个定义 Example 类，第二个定义父类。super() 方法返回 Example 的超类对象。__init__（）方法是Python中的构造方法。
"""
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        #我们把创建 GUI 的工作交给 initUI 方法
        self.initUI()

    def initUI(self):
        """
        以上的三个方法已经从 QWidget 类继承了。setGeometry() 方法负责两件事：它定义窗口在屏幕上的位置，并设置窗口大小。
        前两个参数是窗口相对于屏幕的 x，y 轴坐标，第三个参数是宽度，第四个参数是高度，实际上 它集成了resize() 和 move() 函数于一个方法内。
        最后一个方法设置应用程序的图标，为了实现它，我们必须创建一个 QIcon 对象，QIcon 函数接受图标文件的路径用于显示。
        """
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('sdnayus9.jpg'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())