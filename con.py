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
        if not self.ui.prev_button.isEnabled():
            self.ui.prev_button.setEnabled(True)
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
        # print(current_thumbnail)
        # print(self.count)
        current_thumbnail = current_thumbnail[self.count:]
        # print(self.count, self.up, current_thumbnail)
        for item in current_thumbnail:
            index += 1
            file_name = os.path.join(os.path.abspath("temp"), str(self.count + 1) + ".webp")
            if not os.path.exists(file_name):
                urlretrieve(item, file_name)
            # print(file_name)
            label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            status = "self.ui.label_" + str(index) + ".setEnabled(False)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(False)"
            # order = "self.ui.label_" + str(i) + ".setAlignment(Qt.AlignCenter)"
            exec(label_controller)
            exec(status)
            exec(checkbox_controller)
            self.count += 1
            # exec(order)
        self.show()

    @Slot()
    def prev_(self):
        self.count -= 9
        if self.count - 9 == 0:
            self.ui.prev_button.setEnabled(False)
        current_thumbnail = []
        index = 0
        # print(self.count)
        for item in range(self.count - 8, self.count):
            index += 1
            # print(item)
            file_name = os.path.join(os.path.abspath("temp"), str(item) + ".webp")
            label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            status = "self.ui.label_" + str(index) + ".setEnabled(False)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(False)"
            # print(label_controller)
            exec(label_controller)
            exec(status)
            exec(checkbox_controller)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.index = 0
        self.count = 0
        self.load_image()
        self.ui.next_button.clicked.connect(self.load_image)
        self.ui.prev_button.clicked.connect(self.prev_)
        # self.ui.checkBox_1
        for value in range(1, 10):
            command = "self.ui.checkBox_" + str(value) + ".stateChanged.connect(self.checkbox)"
            exec(command)
        self.ui.prev_button.setEnabled(False)

    @Slot()
    def checkbox(self):
        for value in range(1, 10):
            photo_status = ("self.ui.label_" + str(value) + ".setEnabled(True) if self.ui.checkBox_" +
                            str(value) + ".isChecked() else self.ui.label_" + str(value) + ".setEnabled(False)")
            exec(photo_status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    app.exec()
    sys.exit(shutil.rmtree("temp"))
