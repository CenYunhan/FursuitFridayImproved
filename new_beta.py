from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from browser import Ui_MainWindow
from dialog_about import Ui_Dialog
from remater import interface
from urllib.request import urlretrieve
from threading import Thread
import sys
import os
import shutil


class MainWindow(QMainWindow):
    @Slot()
    def load_image(self):
        if not self.ui.prev_button.isEnabled():
            self.ui.prev_button.setEnabled(True)
        self.up = self.total_count + 9
        thumbnails, self.data = interface(self.up)
        if not os.path.exists("temp"):
            os.mkdir("temp")
        current_thumbnail = []
        for member in thumbnails:
            for thumbnail in member["images"]:
                current_thumbnail.append(thumbnail)

        current_thumbnail = current_thumbnail[self.total_count:]

        # print(self.total_count, self.up, current_thumbnail)
        index = 0
        for item in current_thumbnail:
            index += 1
            file_name = os.path.join(os.path.abspath("temp"), str(self.total_count + 1) + ".webp")
            if not os.path.exists(file_name):
                thread = Thread(target=urlretrieve, args=(item, file_name))
                thread.start()
                thread.join()
                # urlretrieve(item, file_name)
            # print(file_name)
            label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            status = "self.ui.label_" + str(index) + ".setEnabled(False)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(False)"
            order = "self.ui.label_" + str(index) + ".setAlignment(Qt.AlignCenter)"
            exec(label_controller)
            exec(status)
            exec(checkbox_controller)
            exec(order)
            self.total_count += 1
        self.show()

    @Slot()
    def prev_(self):
        self.total_count -= 9
        if self.total_count - 9 == 0:
            self.ui.prev_button.setEnabled(False)
        index = 0
        # print(self.total_count)
        for item in range(self.total_count - 8, self.total_count + 1):
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
        self.data = None
        self.index = None
        self.low = None
        self.up = None
        self.save_path = os.getcwd()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("毛图")
        # self.index = 0
        self.total_count = 0
        self.load_image()
        self.ui.next_button.clicked.connect(self.load_image)
        self.ui.prev_button.clicked.connect(self.prev_)
        # self.ui.checkBox_1
        for value in range(1, 10):
            command = "self.ui.checkBox_" + str(value) + ".stateChanged.connect(self.checkbox)"
            exec(command)
        self.ui.prev_button.setEnabled(False)
        self.ui.action_about.triggered.connect(self.raise_about)
        self.ui.action_change_folder.triggered.connect(self.open_file_dialog)
        self.ui.action_download.triggered.connect(self.ui_download)
        self.ui.action_exit_app.triggered.connect(self.close)

    @Slot()
    def checkbox(self):
        for value in range(1, 10):
            photo_status = ("self.ui.label_" + str(value) + ".setEnabled(True) if self.ui.checkBox_" +
                            str(value) + ".isChecked() else self.ui.label_" + str(value) + ".setEnabled(False)")
            exec(photo_status)

    @Slot()
    def ui_download(self):
        requires = []
        count = 0
        self.low = self.total_count - 9
        self.index = None
        for value in range(1, 10):
            photo_status = ("self.index = self.low + " + str(value) + " if self.ui.checkBox_" +
                            str(value) + ".isChecked() else self.ui.label_" + str(value) + ".setEnabled(False)")
            exec(photo_status)
            if self.index is not None:
                requires.append(self.index)
        # print(requires)
        for item in self.data:
            images = item["images"]
            count += len(images)
            while requires:
                photo_index = requires[0]
                if count >= photo_index:
                    # print(self.total_count)
                    target = images[count - photo_index]
                    thread = (Thread(target=urlretrieve,
                                     args=(target, os.path.join(self.save_path,
                                                                item["file_names"][count - photo_index]))))
                    thread.start()
                    # thread.join()
                    requires.pop(0)
                else:
                    break

    @Slot()
    def open_file_dialog(self):
        self.save_path = QFileDialog.getExistingDirectory(self, "", os.getcwd())

    @Slot()
    def raise_about(self):
        dialog = About()
        dialog.show()
        dialog.exec()


class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
    sys.exit(shutil.rmtree("temp"))
