from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
from browser import Ui_MainWindow
from remater import interface, download
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
        thumbnails, data = interface(self.up)
        if not os.path.exists("temp"):
            os.mkdir("temp")
        current_thumbnail = []
        images_temp = []
        index = 0
        for member in thumbnails:
            for thumbnail in member["images"]:
                current_thumbnail.append(thumbnail)
        for item in data:
            print(item)
            user_name = item["name"]
            time = item["time"]
            for image in item["images"]:
                profile = {
                    "name": user_name,
                    "time": time,
                    "images": image
                }
                self.images_ready_for_download.append(profile)
            index += 1

        current_thumbnail = current_thumbnail[self.count:]

        # print(self.count, self.up, current_thumbnail)
        index = 0
        for item in current_thumbnail:
            index += 1
            file_name = os.path.join(os.path.abspath("temp"), str(self.count + 1) + ".webp")
            if not os.path.exists(file_name):
                urlretrieve(item, file_name)
            # print(file_name)
            label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            status = "self.ui.label_" + str(index) + ".setEnabled(False)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(False)"
            order = "self.ui.label_" + str(index) + ".setAlignment(Qt.AlignCenter)"
            exec(label_controller)
            exec(status)
            exec(checkbox_controller)
            exec(order)
            self.count += 1
            # exec(order)
        self.show()

    @Slot()
    def prev_(self):
        self.count -= 9
        if self.count - 9 == 0:
            self.ui.prev_button.setEnabled(False)
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
        self.up = None
        self.images_ready_for_download = []
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
        self.ui.action_download.triggered.connect(self.ui_download)

    @Slot()
    def checkbox(self):
        for value in range(1, 10):
            photo_status = ("self.ui.label_" + str(value) + ".setEnabled(True) if self.ui.checkBox_" +
                            str(value) + ".isChecked() else self.ui.label_" + str(value) + ".setEnabled(False)")
            exec(photo_status)

    @Slot()
    def ui_download(self):
        print(self.images_ready_for_download)
        for value in range(1, 10):
            photo_status = ("download(self.images_ready_for_download) if self.ui.checkBox_" +
                            str(value) + ".isChecked() else self.ui.label_" + str(value) + ".setEnabled(False)")
            exec(photo_status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    app.exec()
    sys.exit(shutil.rmtree("temp"))
