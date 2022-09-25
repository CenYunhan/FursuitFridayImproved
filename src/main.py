import os
import shutil
import sys
import urllib.error
from collections import deque
from urllib.request import urlretrieve

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QMainWindow,
                               QMessageBox)

from core_utilities import interface
from UI.dialog_about import Ui_Dialog
from UI.dialog_user_input import Ui_Dialog as Ui_URL
from UI.framework import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        # 设置UI与子窗口
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('FursuitFriday Improved')
        self.messagebox = QMessageBox()
        self.about = About()
        self.about.setWindowTitle('关于')

        # 绑定信号
        self.ui.next_button.clicked.connect(self.load_image)
        self.ui.prev_button.clicked.connect(self.prev)
        self.ui.action_about.triggered.connect(self.raise_about)
        self.ui.action_change_folder.triggered.connect(self.open_file_dialog)
        self.ui.action_download.triggered.connect(self.ui_download)
        self.ui.action_exit_app.triggered.connect(self.close)
        self.ui.action_URL.triggered.connect(self.raise_url_change_dialog)
        self.ui.action_select_all.triggered.connect(self.select_all_images)
        self.ui.action_Search.triggered.connect(self.search_service_helper)

        # 其余初始化操作
        self.names_without_ext = self.names = self.data = self.up = self.low = None
        self.save_path = os.getcwd()
        self.total_count = 0
        self.load_image()
        self.ui.prev_button.setEnabled(False)

        """
        names保存了后端整理后的文件名 用于下载器保存;names_without_ext和names相同 但不带扩展名 用于标题的展示
        self.data保存了整理后图片的url等信息
        self.total_count,self.up对应当前的图片数量,下一次应该加载的数量
        """

    @Slot()  # 加载图像
    def load_image(self):
        global global_URL, changeURL, search_status, keyword
        # 在用户点击下一页后启用上一页按钮
        if not self.ui.prev_button.isEnabled():
            self.ui.prev_button.setEnabled(True)
        # 预先声明topic_id避免unbounded error
        topic_id = ""
        # 判断是否存在新的url 是否请求切换地址
        if global_URL and changeURL:
            # 检查是否为bilibili动态链接
            if "t.bilibili.com" in global_URL:
                if not global_URL.endswith("/"):
                    global_URL += "/"
                # 提取topic_id
                topic_id = global_URL[global_URL.find("topic") + len("topic") + 1: -1]
                # 刷新缓存的变量
                if os.path.exists("temp"):
                    shutil.rmtree("temp")
                self.names_without_ext = self.names = self.data = None
                self.total_count = 0
                # 操作完毕后将请求状态切换为否
                changeURL = False
                keyword = ""
                self.ui.prev_button.setEnabled(False)
        if keyword and search_status:
            if os.path.exists("temp"):
                shutil.rmtree("temp")
            self.names_without_ext = self.names = self.data = None
            self.total_count = 0
            search_status = False
            self.ui.prev_button.setEnabled(False)
        self.up = self.total_count + 9
        if not keyword:
            try:
                thumbnails, self.data, self.names_without_ext, self.names = interface(self.up, topic_id)
            except ConnectionError:
                self.raise_message("网络未连接")
                sys.exit(app.exit())
        else:
            try:
                thumbnails, self.data, self.names_without_ext, self.names = interface(self.up, search_content=keyword)
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
            self.ui.__dict__[f'label_{index}'].setPixmap(QPixmap(file_name))
            self.ui.__dict__[f'checkBox_{index}'].setChecked(False)
            self.ui.__dict__[f'checkBox_{index}'].setText(self.names_without_ext[self.total_count])
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
            self.ui.__dict__[f'label_{index}'].setPixmap(QPixmap(file_name))
            self.ui.__dict__[f'checkBox_{index}'].setChecked(False)
            self.ui.__dict__[f'checkBox_{index}'].setText(self.names_without_ext[locale_low - 1])
            locale_low += 1

    @Slot()
    def ui_download(self):
        requires = deque()
        count = 0
        self.low = self.total_count - 9
        for index in range(1, 10):
            if self.ui.__dict__[f'checkBox_{index}'].isChecked():
                requires.append(self.low + index)
        # print(requires)
        if requires:
            self.raise_message("已经开始下载,请自行检查文件夹\n" + self.save_path)
        for item in self.data:
            images = item["images"]
            temporal_count = count
            count += len(images)
            while requires:
                photo_index = requires.popleft()
                if count >= photo_index:
                    # print(self.total_count)
                    target = images[photo_index - temporal_count - 1]
                    try:
                        urlretrieve(target, os.path.join(self.save_path, self.names[photo_index - 1]))
                    except urllib.error.URLError:
                        self.raise_message("网络未连接")
                else:
                    break

    @Slot()
    def open_file_dialog(self):
        self.save_path = QFileDialog.getExistingDirectory(self, "", os.getcwd())

    @Slot()
    def select_all_images(self):
        for index in range(1, 10):
            self.ui.__dict__[f'checkBox_{index}'].setChecked(True)

    @Slot()
    def search_service_helper(self):
        dialog = URLDialog()
        dialog.setWindowTitle("搜索")
        dialog.ui.label.setText("请输入要搜索的up主")
        dialog.ui.buttonBox.accepted.connect(dialog.get_keyword)
        dialog.ui.buttonBox.accepted.connect(self.load_image)
        dialog.exec()
        dialog.show()

    @Slot()
    def raise_about(self):
        self.about.show()

    @Slot()
    def raise_message(self, message):
        self.messagebox.information(self, "", message)

    @Slot()
    def raise_url_change_dialog(self):
        global global_URL
        dialog = URLDialog()
        dialog.setWindowTitle("更改URL")
        # 绑定信号 获取输入的内容并请求切换
        dialog.ui.buttonBox.accepted.connect(dialog.get_url)
        dialog.ui.buttonBox.accepted.connect(self.load_image)
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
    def get_url(self):
        global global_URL, changeURL
        global_URL = self.ui.lineEdit.text()
        changeURL = True

    @Slot()
    def get_keyword(self):
        global keyword, search_status
        keyword = self.ui.lineEdit.text()
        search_status = True


if __name__ == "__main__":
    global_URL = ""
    keyword = ""
    changeURL = search_status = False
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
    if os.path.exists("temp"):
        shutil.rmtree("temp")
    sys.exit()
