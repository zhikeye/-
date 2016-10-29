# -*- coding: utf-8 -*-
"""
第一个Qt程序
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    #每个PyQt5应用都必须首先创建一个application对象。sys.argv 可以但不强制 接受一组命令行参数列表，通过这种方式，我们就可以在命令行中控制我们的应用了。
    app = QApplication(sys.argv)
    #在PyQt5中，QWidget 是所有面向用户界面的组件的继承类（base class），在这里，我们为QWidget 类提供默认的构造方法，所以没有父类，我们把这种形式构建的小部件称作一个 “窗口”。
    w = QWidget()
    #resize 方法可以改变默认的窗口大小，在这里，“小窗口”的宽是250像素，高是150像素：}。
    w.resize(250, 150)
    #move方法将“小窗口”在屏幕上基于二维坐标移动（或摆放），以屏幕的底边为x轴，左侧边为y轴，值域 >=0 ，在这里，坐标为x=300，y=300。
    w.move(100, 300)
    #setWindowTitle方法，顾名思义设置小窗口的标题。为simple。
    w.setWindowTitle('Simple')
    #show方法将小部件在屏幕上显示，在PyQt中，一个widget小部件首先被创建于内存中，然后通过show方法显示于屏幕。
    w.show()
    #最后，我们创建本应用程序主体的循环（mainloop），程序由此操作开始处理 “事件”，程序主体从窗口界面接收事件，并将它们分派给应用程序的 widget 对象。如果我们调用exit() 方法，那么窗口的主体循环将结束，内存中的widget对象也即被销毁，sys.exit() 方法确保了退出与清理的可靠性，系统环境将被告知该应用程序应该如何结束。
    sys.exit(app.exec_())