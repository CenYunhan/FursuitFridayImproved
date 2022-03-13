#!/usr/bin/python3
import os
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from murasakibat import Ui_MainWindow
import sys
import traceback
from main import start
from main import Utilities


class MainWindow(QMainWindow):
    @Slot()
    def driver_select(self, driver):
        self.driver = driver

    @Slot()
    def main(self):
        check = self.ui.userInput.text()
        self.response = []
        if check:
            try:
                try:
                    check = int(check)
                except ValueError:
                    check = 0
                    self.ui.MessageBox.critical(QMessageBox(), "错误", "焯")
                if check != 0:
                    self.response, ending_status = start(self.driver, check)
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
            self.ui.MessageBox.critical(QMessageBox(), "错误", "焯")

    @Slot()
    def download(self):
        self.ui.downloadButton.setEnabled(False)
        self.ui.downloadButton.setText("Done")
        if not os.path.exists("images"):
            os.mkdir("images")
        if os.path.exists("wget.exe"):
            for combined_item in self.response:
                count = 0
                for url in combined_item["image_url"]:
                    count += 1
                    if len(combined_item["image_url"]) == (0 or 1):
                        counter = ""
                    else:
                        counter = " " + str(count)
                    file_extend_name = Utilities()._filter(response=url, keyword_1=".", reverse=True)
                    file_name = combined_item["user_name"] + " " + combined_item[
                        "post_time"] + counter + file_extend_name
                    command = "wget " + url + ' -O "images/' + file_name + '"'
                    os.system(command)

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
        self.ui.comboBox.currentTextChanged.connect(self.driver_select)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
