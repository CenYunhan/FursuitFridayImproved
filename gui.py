from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from murasakibat import Ui_MainWindow
import sys
from main import start


class MainWindow(QMainWindow):
    @Slot()
    def hello(self):
        check = self.ui.userInput.text()
        r = []
        if check:
            r = start(check)
            a = ""
            for items in r:
                a = a + items + "\n"
            self.ui.textEdit.setText(a)
            self.ui.excuteButton.setEnabled(False)
            self.ui.excuteButton.setText("Done")
        else:
            self.ui.MessageBox.critical(QMainWindow(), "错误", "输个数字吧.....做个人好吗,debug真的很累的")

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.excuteButton.clicked.connect(self.hello)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
