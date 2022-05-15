# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import encrypted_images_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(468, 298)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(468, 298))
        Dialog.setMaximumSize(QSize(468, 298))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(205, 274))
        self.label.setMaximumSize(QSize(205, 274))
        self.label.setStyleSheet(u"background-image: url(:/images/About_Background.PNG);")
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_2.setMargin(0)
        self.label_2.setIndent(7)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setMargin(8)
        self.label_3.setIndent(0)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u71a0\u4e91</p><p align=\"center\">\u7a0b\u5e8f</p><p align=\"center\">Copyright \u00a9 2021-2022</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u7d2b\u67ab</p><p align=\"center\">\u7f8e\u5de5(\u786e\u4fe1)</p><p align=\"center\">Copyright \u00a9 Bat Studio 2019-2022</p></body></html>", None))
    # retranslateUi

