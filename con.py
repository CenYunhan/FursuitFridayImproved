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
        self.up = self.count + 9
        data = interface(self.up)
        if not os.path.exists("temp"):
            os.mkdir("temp")
        print(data)

        index = 0

        current_thumbnail = []
        for member in data:
            for thumbnail in member["images"]:
                current_thumbnail.append(thumbnail)
        print(current_thumbnail)
        print(self.count)
        current_thumbnail = current_thumbnail[self.count:]
        # print(self.count, self.up, current_thumbnail)
        for item in current_thumbnail:
            index += 1
            file_name = os.path.join(os.path.abspath("temp"), str(self.count + 1) + ".webp")
            # print(file_name)
            urlretrieve(item, file_name)
            label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            # order = "self.ui.label_" + str(i) + ".setAlignment(Qt.AlignCenter)"
            exec(label_controller)
            self.count += 1
            # exec(order)
        self.show()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.index = 0
        self.count = 0
        self.load_image()
        self.ui.next_button.clicked.connect(self.load_image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    app.exec()
    sys.exit(shutil.rmtree("temp"))
