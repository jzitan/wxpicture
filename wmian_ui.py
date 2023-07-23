# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wmian.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(408, 236)
        icon = QIcon()
        icon.addFile(u"i.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setInputMethodHints(Qt.ImhNone)
        self.down = QPushButton(Form)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(130, 110, 151, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.down.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 170, 291, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.result = QLabel(self.layoutWidget)
        self.result.setObjectName(u"result")
        font1 = QFont()
        font1.setPointSize(12)
        self.result.setFont(font1)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.result)

        self.open = QPushButton(self.layoutWidget)
        self.open.setObjectName(u"open")

        self.horizontalLayout_3.addWidget(self.open)

        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 3)
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 351, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.geturl = QLabel(self.layoutWidget1)
        self.geturl.setObjectName(u"geturl")

        self.horizontalLayout.addWidget(self.geturl)

        self.textEdit = QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.VLine)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setCursorWidth(1)

        self.horizontalLayout.addWidget(self.textEdit)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 60, 351, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.geturl_from_txt = QLabel(self.layoutWidget2)
        self.geturl_from_txt.setObjectName(u"geturl_from_txt")

        self.horizontalLayout_2.addWidget(self.geturl_from_txt)

        self.file = QPushButton(self.layoutWidget2)
        self.file.setObjectName(u"file")

        self.horizontalLayout_2.addWidget(self.file)

        self.dir = QPushButton(self.layoutWidget2)
        self.dir.setObjectName(u"dir")

        self.horizontalLayout_2.addWidget(self.dir)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u516c\u4f17\u53f7\u56fe\u7247\u4e0b\u8f7d", None))
        self.down.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u56fe\u7247", None))
        self.result.setText("")
        self.open.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.geturl.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u7f51\u5740\uff1a", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8bf7\u8f93\u5165\u5305\u542bhttps:\\\\\u7684\u7f51\u5740</p></body></html>", None))
        self.geturl_from_txt.setText(QCoreApplication.translate("Form", u"\u6216  \u9009\u62e9\u6587\u672c\u6587\u4ef6\u8bfb\u53d6", None))
        self.file.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.dir.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
    # retranslateUi

