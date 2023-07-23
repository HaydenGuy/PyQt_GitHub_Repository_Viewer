# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repo_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_repo_viewer(object):
    def setupUi(self, repo_viewer):
        if not repo_viewer.objectName():
            repo_viewer.setObjectName(u"repo_viewer")
        repo_viewer.resize(735, 362)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(22, 34, 35, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(33, 50, 52, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(27, 42, 43, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(11, 17, 17, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(15, 22, 23, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(27, 39, 43, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(249, 202, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush10 = QBrush(QColor(255, 255, 255, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        brush11 = QBrush(QColor(11, 17, 17, 127))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        repo_viewer.setPalette(palette)
        repo_viewer.setStyleSheet(u"")
        self.centralwidget = QWidget(repo_viewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.repo_name = QLabel(self.centralwidget)
        self.repo_name.setObjectName(u"repo_name")
        self.repo_name.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.repo_name)

        self.le_repo_name = QLineEdit(self.centralwidget)
        self.le_repo_name.setObjectName(u"le_repo_name")

        self.horizontalLayout_2.addWidget(self.le_repo_name)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.username = QLabel(self.centralwidget)
        self.username.setObjectName(u"username")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.username)

        self.le_username = QLineEdit(self.centralwidget)
        self.le_username.setObjectName(u"le_username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_username.sizePolicy().hasHeightForWidth())
        self.le_username.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.le_username)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 715, 68))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.repo_details = QLabel(self.scrollAreaWidgetContents)
        self.repo_details.setObjectName(u"repo_details")
        self.repo_details.setMaximumSize(QSize(16777215, 16777215))
        self.repo_details.setStyleSheet(u"color:white;")
        self.repo_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.repo_details)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 8, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_ok = QPushButton(self.centralwidget)
        self.pb_ok.setObjectName(u"pb_ok")

        self.horizontalLayout_3.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(self.centralwidget)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout_3.addWidget(self.pb_cancel)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.welcome_text = QLabel(self.centralwidget)
        self.welcome_text.setObjectName(u"welcome_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.welcome_text.sizePolicy().hasHeightForWidth())
        self.welcome_text.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.welcome_text, 1, 0, 1, 1)

        repo_viewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(repo_viewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 735, 23))
        repo_viewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(repo_viewer)
        self.statusbar.setObjectName(u"statusbar")
        repo_viewer.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.le_username, self.le_repo_name)
        QWidget.setTabOrder(self.le_repo_name, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)
        QWidget.setTabOrder(self.pb_cancel, self.scrollArea)

        self.retranslateUi(repo_viewer)

        QMetaObject.connectSlotsByName(repo_viewer)
    # setupUi

    def retranslateUi(self, repo_viewer):
        repo_viewer.setWindowTitle(QCoreApplication.translate("repo_viewer", u"GitHub Repository Viewer", None))
        self.repo_name.setText(QCoreApplication.translate("repo_viewer", u"Repo Name:", None))
        self.username.setText(QCoreApplication.translate("repo_viewer", u"Username:", None))
        self.repo_details.setText("")
        self.pb_ok.setText(QCoreApplication.translate("repo_viewer", u"OK", None))
        self.pb_cancel.setText(QCoreApplication.translate("repo_viewer", u"Cancel", None))
        self.welcome_text.setText(QCoreApplication.translate("repo_viewer", u"Please enter the GitHub 'Username' and 'Repo Name' to view it's details:", None))
    # retranslateUi

