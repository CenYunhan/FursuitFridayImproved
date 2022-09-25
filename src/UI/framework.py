# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'framework.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 545)
        self.action_download = QAction(MainWindow)
        self.action_download.setObjectName(u"action_download")
        self.action_change_folder = QAction(MainWindow)
        self.action_change_folder.setObjectName(u"action_change_folder")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_exit_app = QAction(MainWindow)
        self.action_exit_app.setObjectName(u"action_exit_app")
        self.action_URL = QAction(MainWindow)
        self.action_URL.setObjectName(u"action_URL")
        self.action_select_all = QAction(MainWindow)
        self.action_select_all.setObjectName(u"action_select_all")
        self.action_Search = QAction(MainWindow)
        self.action_Search.setObjectName(u"action_Search")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_1_2 = QHBoxLayout()
        self.horizontalLayout_1_2.setObjectName(u"horizontalLayout_1_2")
        self.checkBox_1 = QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy)
        self.checkBox_1.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_1_2.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_1_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_1_2.addWidget(self.checkBox_3)


        self.gridLayout.addLayout(self.horizontalLayout_1_2, 1, 0, 1, 1)

        self.horizontalLayout_1_1 = QHBoxLayout()
        self.horizontalLayout_1_1.setObjectName(u"horizontalLayout_1_1")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy1)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_1_1.addWidget(self.label_1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_1_1.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_1_1.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_1_1, 0, 0, 1, 1)

        self.horizontalLayout_3_1 = QHBoxLayout()
        self.horizontalLayout_3_1.setObjectName(u"horizontalLayout_3_1")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3_1.addWidget(self.label_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3_1.addWidget(self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3_1.addWidget(self.label_9)


        self.gridLayout.addLayout(self.horizontalLayout_3_1, 4, 0, 1, 1)

        self.horizontalLayout_2_1 = QHBoxLayout()
        self.horizontalLayout_2_1.setObjectName(u"horizontalLayout_2_1")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2_1.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2_1.addWidget(self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2_1.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_2_1, 2, 0, 1, 1)

        self.horizontalLayout_2_2 = QHBoxLayout()
        self.horizontalLayout_2_2.setObjectName(u"horizontalLayout_2_2")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_2_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_2_2.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_2_2.addWidget(self.checkBox_6)


        self.gridLayout.addLayout(self.horizontalLayout_2_2, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.prev_button = QPushButton(self.centralwidget)
        self.prev_button.setObjectName(u"prev_button")

        self.horizontalLayout_4.addWidget(self.prev_button)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout_4.addWidget(self.next_button)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)

        self.horizontalLayout_3_2 = QHBoxLayout()
        self.horizontalLayout_3_2.setObjectName(u"horizontalLayout_3_2")
        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        self.checkBox_7.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_3_2.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        self.checkBox_8.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_3_2.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        self.checkBox_9.setMaximumSize(QSize(16777215, 13))

        self.horizontalLayout_3_2.addWidget(self.checkBox_9)


        self.gridLayout.addLayout(self.horizontalLayout_3_2, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 476, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(158, 126, 149, 186))
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_select_all)
        self.menu.addAction(self.action_Search)
        self.menu.addAction(self.action_download)
        self.menu.addAction(self.action_change_folder)
        self.menu.addAction(self.action_URL)
        self.menu.addSeparator()
        self.menu.addAction(self.action_about)
        self.menu.addAction(self.action_exit_app)

        self.retranslateUi(MainWindow)
        self.checkBox_1.toggled.connect(self.label_1.setEnabled)
        self.checkBox_2.toggled.connect(self.label_2.setEnabled)
        self.checkBox_3.toggled.connect(self.label_3.setEnabled)
        self.checkBox_4.toggled.connect(self.label_4.setEnabled)
        self.checkBox_5.toggled.connect(self.label_5.setEnabled)
        self.checkBox_6.toggled.connect(self.label_6.setEnabled)
        self.checkBox_7.toggled.connect(self.label_7.setEnabled)
        self.checkBox_8.toggled.connect(self.label_8.setEnabled)
        self.checkBox_9.toggled.connect(self.label_9.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.action_download.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d", None))
#if QT_CONFIG(shortcut)
        self.action_download.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_change_folder.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u4e0b\u8f7d\u4f4d\u7f6e\u2026\u2026", None))
#if QT_CONFIG(shortcut)
        self.action_change_folder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_exit_app.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u2026\u2026", None))
#if QT_CONFIG(tooltip)
        self.action_exit_app.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u672c\u5e94\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_exit_app.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.action_URL.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539URL\u2026\u2026", None))
        self.action_select_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
#if QT_CONFIG(shortcut)
        self.action_select_all.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_Search.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
#if QT_CONFIG(shortcut)
        self.action_Search.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
#if QT_CONFIG(accessibility)
        self.menuBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

