 #!/usr/bin/python3
import os
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from v1.ui import Ui_MainWindow
import sys
import traceback
from urllib.request import urlretrieve
from main import start
from main import _filter
import qdarkstyle


class MainWindow(QMainWindow):
    @Slot()
    def raise_messagebox(self):
        self.ui.MessageBox.critical(QMessageBox(), "错误", "焯")

    @Slot()
    def main(self):
        required_num = self.ui.userInput.text()
        self.response = []
        if required_num and self.ui.comboBox.currentText() != "--请选择浏览器--":
            try:
                try:
                    check = int(required_num)
                except ValueError:
                    check = 0
                    self.raise_messagebox()
                if check != 0:
                    self.response, ending_status = start(
                        self.ui.comboBox.currentText(), required_num, self.ui.URLAddress.text())
                    output = ""
                    if ending_status:
                        output = output + "指定数量大于网页拥有的图片。\n\n"
                    for items in self.response:
                        output = output + "Up主： " + items["user_name"] + "\n"
                        output = output + "图片地址： "
                        if len(items["image_url"]) > 1:
                            output = output + "\n"
                        for url in items["image_url"]:
                            output = output + url + "\n"
                        output = output + "发布时间： " + items["post_time"] + "\n"
                        output = output + "\n"
                    self.ui.textEdit.setText(output)
                    self.ui.excuteButton.setText("Done")
                    self.ui.downloadButton.setEnabled(True)
                else:
                    pass
            except:
                self.ui.textEdit.setTextColor("#FF0000")
                self.ui.textEdit.setText(traceback.format_exc())
                self.ui.excuteButton.setText("Error")
            finally:
                self.ui.excuteButton.setEnabled(False)
                self.ui.comboBox.setEnabled(False)
        else:
            self.raise_messagebox()

    @Slot()
    def download(self):
        self.ui.downloadButton.setEnabled(False)
        if not os.path.exists("images"):
            os.mkdir("images")
        for combined_item in self.response:
            count = 0
            for url in combined_item["image_url"]:
                count += 1
                if len(combined_item["image_url"]) == (0 or 1):
                    counter = ""
                else:
                    counter = " " + str(count)
                file_extend_name = _filter(response=url, keyword_1=".", reverse=True)
                file_name = combined_item["user_name"] + " " + combined_item[
                    "post_time"] + counter + file_extend_name
                path = os.path.abspath("images")
                urlretrieve(url, os.path.join(path, file_name))
        self.ui.downloadButton.setText("Done")

    def __init__(self):
        super(MainWindow, self).__init__()
        self.driver = None
        self.response = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.MessageBox = QMessageBox()
        self.ui.downloadButton.setEnabled(False)
        self.ui.excuteButton.clicked.connect(self.main)
        self.ui.downloadButton.clicked.connect(self.download)
        self.ui.userInput.returnPressed.connect(self.main)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
