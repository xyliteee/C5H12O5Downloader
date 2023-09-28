# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Xylit\Desktop\Spider\Mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 480)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 720, 480))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 720, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/1675871369526.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 720, 480))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0.5);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Logpage = QtWidgets.QWidget(self.frame)
        self.Logpage.setGeometry(QtCore.QRect(10, 50, 160, 420))
        self.Logpage.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.Logpage.setObjectName("Logpage")
        self.label_3 = QtWidgets.QLabel(self.Logpage)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 160, 421))
        self.label_3.setStyleSheet("background-color: rgb(212, 97, 131);\n"
"border-radius: 8px")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.QRcodeGet = PushButton(self.Logpage)
        self.QRcodeGet.setGeometry(QtCore.QRect(30, 160, 100, 32))
        self.QRcodeGet.setObjectName("QRcodeGet")
        self.QRcode = QtWidgets.QLabel(self.Logpage)
        self.QRcode.setGeometry(QtCore.QRect(20, 20, 120, 120))
        self.QRcode.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.QRcode.setText("")
        self.QRcode.setPixmap(QtGui.QPixmap(":/img/qrcode.png"))
        self.QRcode.setScaledContents(True)
        self.QRcode.setObjectName("QRcode")
        self.cookies = LineEdit(self.Logpage)
        self.cookies.setGeometry(QtCore.QRect(15, 240, 130, 33))
        self.cookies.setMinimumSize(QtCore.QSize(0, 0))
        self.cookies.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.cookies.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")
        self.cookies.setText("")
        self.cookies.setObjectName("cookies")
        self.Login = PushButton(self.Logpage)
        self.Login.setGeometry(QtCore.QRect(30, 310, 100, 32))
        self.Login.setObjectName("Login")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(190, 50, 520, 420))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 520, 420))
        self.label_4.setStyleSheet("border-radius: 8px;\n"
"background-color: rgba(255, 255, 255,0.6);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Cover = QtWidgets.QLabel(self.widget_2)
        self.Cover.setGeometry(QtCore.QRect(30, 30, 240, 135))
        self.Cover.setStyleSheet("background-color: rgb(212, 97, 131);")
        self.Cover.setText("")
        self.Cover.setPixmap(QtGui.QPixmap(":/img/1675871369526.png"))
        self.Cover.setScaledContents(True)
        self.Cover.setObjectName("Cover")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(30, 178, 481, 231))
        self.widget_3.setObjectName("widget_3")
        self.Maintitle = TitleLabel(self.widget_3)
        self.Maintitle.setGeometry(QtCore.QRect(10, 10, 320, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Maintitle.setFont(font)
        self.Maintitle.setWordWrap(True)
        self.Maintitle.setObjectName("Maintitle")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(340, 10, 5, 210))
        self.label_5.setStyleSheet("background-color: rgb(212, 97, 131);\n"
"border-radius: 8px")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.IndeterminateProgressBar = IndeterminateProgressBar(self.widget_3)
        self.IndeterminateProgressBar.setGeometry(QtCore.QRect(10, 70, 311, 4))
        self.IndeterminateProgressBar.setOrientation(QtCore.Qt.Vertical)
        self.IndeterminateProgressBar.setObjectName("IndeterminateProgressBar")
        self.Favorite = SubtitleLabel(self.widget_3)
        self.Favorite.setGeometry(QtCore.QRect(360, 100, 161, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Favorite.setFont(font)
        self.Favorite.setStyleSheet("background-color: rgba(85, 255, 255,0);")
        self.Favorite.setObjectName("Favorite")
        self.Like = SubtitleLabel(self.widget_3)
        self.Like.setGeometry(QtCore.QRect(360, 70, 161, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Like.setFont(font)
        self.Like.setStyleSheet("background-color: rgba(85, 255, 255,0);")
        self.Like.setObjectName("Like")
        self.Coin = SubtitleLabel(self.widget_3)
        self.Coin.setGeometry(QtCore.QRect(360, 40, 161, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Coin.setFont(font)
        self.Coin.setStyleSheet("background-color: rgba(85, 255, 255,0);")
        self.Coin.setObjectName("Coin")
        self.View = SubtitleLabel(self.widget_3)
        self.View.setGeometry(QtCore.QRect(360, 10, 161, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.View.setFont(font)
        self.View.setStyleSheet("background-color: rgba(85, 255, 255,0);")
        self.View.setObjectName("View")
        self.Description = QtWidgets.QLabel(self.widget_3)
        self.Description.setGeometry(QtCore.QRect(10, 89, 171, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.Description.setFont(font)
        self.Description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Description.setWordWrap(True)
        self.Description.setObjectName("Description")
        self.CoverSave = PushButton(self.widget_3)
        self.CoverSave.setGeometry(QtCore.QRect(350, 140, 111, 32))
        self.CoverSave.setStyleSheet("PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitToolButton:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 224, 223),\n"
"            stop:1 rgb(225, 224, 223));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:disabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToolButton:hover,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:checked:hover,\n"
"PillPushButton:checked:pressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.CoverSave.setObjectName("CoverSave")
        self.VideoDownload = PushButton(self.widget_3)
        self.VideoDownload.setGeometry(QtCore.QRect(350, 180, 111, 32))
        self.VideoDownload.setObjectName("VideoDownload")
        self.down_choice = ComboBox(self.widget_3)
        self.down_choice.setGeometry(QtCore.QRect(200, 130, 130, 32))
        self.down_choice.setObjectName("down_choice")
        self.page_choice = ComboBox(self.widget_3)
        self.page_choice.setGeometry(QtCore.QRect(200, 90, 130, 32))
        self.page_choice.setObjectName("page_choice")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setGeometry(QtCore.QRect(300, 30, 211, 135))
        self.widget_6.setObjectName("widget_6")
        self.ProfilePic = QtWidgets.QLabel(self.widget_6)
        self.ProfilePic.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.ProfilePic.setStyleSheet("background-color: rgb(212, 97, 131);")
        self.ProfilePic.setText("")
        self.ProfilePic.setPixmap(QtGui.QPixmap(":/img/default.png"))
        self.ProfilePic.setScaledContents(True)
        self.ProfilePic.setObjectName("ProfilePic")
        self.UPID = SubtitleLabel(self.widget_6)
        self.UPID.setGeometry(QtCore.QRect(10, 100, 161, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.UPID.setFont(font)
        self.UPID.setStyleSheet("background-color: rgba(85, 255, 255,0);")
        self.UPID.setObjectName("UPID")
        self.Alpha = QtWidgets.QLabel(self.widget_6)
        self.Alpha.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.Alpha.setStyleSheet("")
        self.Alpha.setText("")
        self.Alpha.setPixmap(QtGui.QPixmap(":/img/alpha.png"))
        self.Alpha.setScaledContents(True)
        self.Alpha.setObjectName("Alpha")
        self.Zone = PushButton(self.widget_6)
        self.Zone.setGeometry(QtCore.QRect(110, 20, 91, 32))
        self.Zone.setObjectName("Zone")
        self.downloadpagebutton = PushButton(self.widget_6)
        self.downloadpagebutton.setGeometry(QtCore.QRect(110, 60, 91, 32))
        self.downloadpagebutton.setObjectName("downloadpagebutton")
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setGeometry(QtCore.QRect(645, 10, 65, 31))
        self.widget_5.setStyleSheet("border-radius: 8px;\n"
"background-color: rgba(255, 255, 255,0.6);")
        self.widget_5.setObjectName("widget_5")
        self.Min = QtWidgets.QPushButton(self.widget_5)
        self.Min.setGeometry(QtCore.QRect(5, 3, 25, 25))
        self.Min.setStyleSheet("QPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: rgb(181, 181, 181);\n"
"    border: 1px solid rgb(181, 181, 181);\n"
"    border-bottom: 1px solid rgb(161, 161, 161);\n"
"border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: rgb(161, 161, 161);\n"
"    border: 1px solid rgb(161, 161, 161);\n"
"    border-bottom: 1px solid rgb(141, 141, 141);\n"
"border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: rgb(141, 141, 141);\n"
"    border: 1px solid rgb(141, 141, 141);\n"
"border-radius: 8px\n"
"}")
        self.Min.setText("")
        self.Min.setObjectName("Min")
        self.Shutdown = QtWidgets.QPushButton(self.widget_5)
        self.Shutdown.setGeometry(QtCore.QRect(35, 3, 25, 25))
        self.Shutdown.setStyleSheet("QPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: rgb(212, 12, 48);\n"
"    border: 1px solid rgb(212, 12, 48);\n"
"    border-bottom: 1px solid rgb(192, 6, 32);\n"
"    border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: rgb(192, 6, 32);\n"
"    border: 1px solid rgb(192, 6, 32);\n"
"    border-bottom: 1px solid rgb(162, 0, 11);\n"
"    border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: rgb(162, 0, 11);\n"
"    border: 1px solid rgb(162, 0, 11);\n"
"    border-radius: 8px\n"
"}")
        self.Shutdown.setText("")
        self.Shutdown.setObjectName("Shutdown")
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.widget_4.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget_4.setObjectName("widget_4")
        self.Bvlink = LineEdit(self.widget_4)
        self.Bvlink.setGeometry(QtCore.QRect(0, 0, 161, 33))
        self.Bvlink.setMinimumSize(QtCore.QSize(0, 0))
        self.Bvlink.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.Bvlink.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")
        self.Bvlink.setText("")
        self.Bvlink.setObjectName("Bvlink")
        self.Search = QtWidgets.QPushButton(self.widget_4)
        self.Search.setGeometry(QtCore.QRect(130, 3, 25, 25))
        self.Search.setStyleSheet("QPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: rgb(212, 97, 131);\n"
"    border: 1px solid rgb(212, 97, 131);\n"
"    border-bottom: 1px solid rgb(192, 87, 121);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: rgb(192, 87, 121);\n"
"    border: 1px solid rgb(192, 87, 121);\n"
"    border-bottom: 1px solid rgb(172, 77, 108);\n"
"    border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color:rgb(172, 77, 108);\n"
"    border: 1px solid rgb(172, 77, 108);\n"
"    border-radius: 8px\n"
"}\n"
"\n"
"QPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}")
        self.Search.setText("")
        self.Search.setObjectName("Search")
        self.PersonPage = QtWidgets.QWidget(self.frame)
        self.PersonPage.setGeometry(QtCore.QRect(10, 50, 160, 420))
        self.PersonPage.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.PersonPage.setObjectName("PersonPage")
        self.label_6 = QtWidgets.QLabel(self.PersonPage)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 160, 420))
        self.label_6.setStyleSheet("background-color: rgb(212, 97, 131);\n"
"border-radius: 8px")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.Profileface = QtWidgets.QLabel(self.PersonPage)
        self.Profileface.setGeometry(QtCore.QRect(20, 20, 120, 120))
        self.Profileface.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Profileface.setText("")
        self.Profileface.setPixmap(QtGui.QPixmap(":/img/default.png"))
        self.Profileface.setScaledContents(True)
        self.Profileface.setObjectName("Profileface")
        self.Name = SubtitleLabel(self.PersonPage)
        self.Name.setGeometry(QtCore.QRect(20, 160, 119, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.Logout = PushButton(self.PersonPage)
        self.Logout.setGeometry(QtCore.QRect(30, 310, 100, 32))
        self.Logout.setObjectName("Logout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.QRcodeGet.setText(_translate("Form", "刷新"))
        self.cookies.setPlaceholderText(_translate("Form", "或者用cookie登录也可以"))
        self.Login.setText(_translate("Form", "登录"))
        self.Maintitle.setText(_translate("Form", "这里是标题巴拉巴拉吧"))
        self.Favorite.setText(_translate("Form", "收藏：114514"))
        self.Like.setText(_translate("Form", "点赞：114514"))
        self.Coin.setText(_translate("Form", "投币：114514"))
        self.View.setText(_translate("Form", "播放：114514"))
        self.Description.setText(_translate("Form", "这里是简介"))
        self.CoverSave.setText(_translate("Form", "保存封面"))
        self.VideoDownload.setText(_translate("Form", "开始下载"))
        self.UPID.setText(_translate("Form", "这里是UPID"))
        self.Zone.setText(_translate("Form", "个人主页"))
        self.downloadpagebutton.setText(_translate("Form", "下载页面"))
        self.Bvlink.setPlaceholderText(_translate("Form", "输入连接或者BV号"))
        self.Name.setText(_translate("Form", "Username"))
        self.Logout.setText(_translate("Form", "登出"))
from qfluentwidgets import ComboBox, IndeterminateProgressBar, LineEdit, PushButton, SubtitleLabel, TitleLabel
import res_rc
