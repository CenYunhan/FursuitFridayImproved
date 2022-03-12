from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from murasakibat import Ui_MainWindow
import sys
import traceback
from main import start


class MainWindow(QMainWindow):
    @Slot()
    def hello(self):
        check = self.ui.userInput.text()
        r = []
        if check:
            try:
                r = start(check)
                a = ""
                for items in r:
                    a = a + items + "\n"
                self.ui.textEdit.setText(a)
                self.ui.excuteButton.setText("Done")
            except:
                self.ui.textEdit.setText(traceback.format_exc())
                self.ui.excuteButton.setText("Error")
            self.ui.excuteButton.setEnabled(False)
        else:
            self.ui.MessageBox.critical(QMessageBox(), "错误", "焯")

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
