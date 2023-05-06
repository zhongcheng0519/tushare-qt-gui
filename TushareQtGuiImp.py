import sys

from TushareQtGui import *
from GUI.basic.BasicPageImp import BasicPageImp


class TushareQtGuiImp(QMainWindow):

    def __init__(self):
        super(TushareQtGuiImp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon.png"))
        # ================ Tab ==============================
        self.ui.tabWidget.currentChanged.connect(self.onTabWidgetCurrentChanged)
        self.basic_page = BasicPageImp()
        self.ui.tabWidget.addTab(self.basic_page, "基本面")
        self.ui.tabWidget.setCurrentIndex(0)

    def onTabWidgetCurrentChanged(self, index):
        print("onTabWidgetCurrentChanged: ", index)
        self.ui.tabWidget.widget(index).refresh()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tushare_qt_gui = TushareQtGuiImp()
    tushare_qt_gui.show()
    sys.exit(app.exec_())