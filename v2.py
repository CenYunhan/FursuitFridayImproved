from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox
from framework import Ui_MainWindow
from dialog_about import Ui_Dialog
from dialog_URL import Ui_Dialog as Ui_URL
from core_utilities import interface
from urllib.request import urlretrieve
import urllib.error
import sys
import os
import shutil


class MainWindow(QMainWindow):
    @Slot()
    def load_image(self):
        topic_id = ""
        if global_URL and self.changeURL:
            if "t.bilibili.com" in global_URL:
                topic_id = global_URL[global_URL.find("topic") + len("topic") + 1: -1]
                shutil.rmtree("temp")
                self.names_without_ext = self.names = self.data = None
                self.total_count = 0
                self.changeURL = False
        if not self.ui.prev_button.isEnabled():
            self.ui.prev_button.setEnabled(True)
        self.up = self.total_count + 9
        try:
            thumbnails, self.data, self.names_without_ext, self.names = interface(topic_id, self.up)
        except ConnectionError:
            self.raise_message("网络未连接")
            sys.exit(app.exit())
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
                urlretrieve(item, file_name)
            # print(file_name)
            image_label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            status = "self.ui.label_" + str(index) + ".setEnabled(False)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(False)"
            order = "self.ui.label_" + str(index) + ".setAlignment(Qt.AlignCenter)"
            change_name = "self.ui.checkBox_" + str(index) + \
                          ".setText('" + self.names_without_ext[self.total_count] + "')"

            commands = [image_label_controller, status, checkbox_controller, order, change_name]
            for command in commands:
                exec(command)
            self.total_count += 1
        self.show()

    @Slot()
    def prev(self):
        self.total_count -= 9
        if self.total_count - 9 == 0:
            self.ui.prev_button.setEnabled(False)
        index = 0
        # print(self.total_count)
        locale_low = self.total_count - 8
        locale_up = self.total_count + 1
        for item in range(locale_low, locale_up):
            index += 1
            # print(item)
            file_name = os.path.join(os.path.abspath("temp"), str(item) + ".webp")
            image_label_controller = "self.ui.label_" + str(index) + '.setPixmap(QPixmap(file_name))'
            status = "self.ui.label_" + str(index) + ".setEnabled(False)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(False)"
            change_name = "self.ui.checkBox_" + str(index) + \
                          ".setText('" + self.names_without_ext[locale_low - 1] + "')"

            # print(image_label_controller)
            commands = [image_label_controller, status, checkbox_controller, change_name]
            for command in commands:
                exec(command)
            locale_low += 1

    def __init__(self):
        super(MainWindow, self).__init__()
        self.names_without_ext = self.names = self.data = self.index = self.up = self.low = self.changeURL = None
        self.save_path = os.getcwd()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messagebox = QMessageBox()
        self.setWindowTitle("毛图")
        self.total_count = 0
        self.load_image()
        self.ui.next_button.clicked.connect(self.load_image)
        self.ui.prev_button.clicked.connect(self.prev)
        for value in range(1, 10):
            command = "self.ui.checkBox_" + str(value) + ".stateChanged.connect(self.checkbox)"
            exec(command)
        self.ui.prev_button.setEnabled(False)
        self.ui.action_about.triggered.connect(self.raise_about)
        self.ui.action_change_folder.triggered.connect(self.open_file_dialog)
        self.ui.action_download.triggered.connect(self.ui_download)
        self.ui.action_exit_app.triggered.connect(self.close)
        self.ui.action_URL.triggered.connect(self.raise_url_change_dialog)
        self.ui.action_select_all.triggered.connect(self.select_all_images)

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
                    try:
                        urlretrieve(target, os.path.join(self.save_path, self.names[photo_index - 1]))
                    except urllib.error.URLError:
                        self.raise_message("网络未连接")
                    requires.pop(0)
                else:
                    break

    @Slot()
    def open_file_dialog(self):
        self.save_path = QFileDialog.getExistingDirectory(self, "", os.getcwd())

    @Slot()
    def select_all_images(self):
        for index in range(1, 10):
            status = "self.ui.label_" + str(index) + ".setEnabled(True)"
            checkbox_controller = "self.ui.checkBox_" + str(index) + ".setChecked(True)"
            commands = [status, checkbox_controller]
            for command in commands:
                exec(command)

    @Slot()
    def raise_about(self):
        dialog = About()
        dialog.setWindowTitle("关于")
        dialog.show()
        dialog.exec()

    @Slot()
    def raise_message(self, message):
        self.messagebox.information(self, "下载器", message)

    @Slot()
    def raise_url_change_dialog(self):
        global global_URL
        dialog = URLDialog()
        dialog.setWindowTitle("更改URL")
        dialog.ui.buttonBox.accepted.connect(dialog.get_text)
        dialog.ui.buttonBox.accepted.connect(self.load_image)
        self.changeURL = True
        dialog.show()
        dialog.exec()


class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class URLDialog(QDialog):
    def __init__(self):
        super(URLDialog, self).__init__()
        self.ui = Ui_URL()
        self.ui.setupUi(self)
        self.ui.label.setText("请输入要载入的URL")

    @Slot()
    def get_text(self):
        global global_URL
        global_URL = self.ui.lineEdit.text()


if __name__ == "__main__":
    global_URL = ""
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    sys.exit()
