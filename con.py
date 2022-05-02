from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from browser import Ui_MainWindow
from remater import interface
from urllib.request import urlretrieve
import sys
import os
import shutil


class MainWindow(QMainWindow):
    @Slot()
    def load_image(self):
        data = interface(9)
        if not os.path.exists("temp"):
            os.mkdir("temp")
        print(data)
        index = 0
        for member in data:
            for thumbnail in member["images"]:
                index += 1
                file_name = os.path.join(os.path.abspath("temp"), str(index) + ".webp")
                urlretrieve(thumbnail, file_name)
                label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
                # order = "self.ui.label_" + str(i) + ".setAlignment(Qt.AlignCenter)"
                exec(label_controller)
            # exec(order)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit(shutil.rmtree("temp"))
