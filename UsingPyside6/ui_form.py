# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 120, 281, 261))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.spinBox_all = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_all.setObjectName(u"spinBox_all")
        self.spinBox_all.setFont(font)
        self.spinBox_all.setMaximum(99999)
        self.spinBox_all.setSingleStep(1000)
        self.spinBox_all.setValue(10000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_all)

        self.spinBox_position = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_position.setObjectName(u"spinBox_position")
        self.spinBox_position.setEnabled(True)
        self.spinBox_position.setFont(font)
        self.spinBox_position.setMaximum(99999)
        self.spinBox_position.setSingleStep(1000)
        self.spinBox_position.setValue(6000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_position)

        self.spinBox_base = QSpinBox(self.verticalLayoutWidget)
        self.spinBox_base.setObjectName(u"spinBox_base")
        self.spinBox_base.setEnabled(False)
        self.spinBox_base.setFont(font)
        self.spinBox_base.setMaximum(2000)
        self.spinBox_base.setValue(1920)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_base)

        self.spinBox_day = QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinBox_day.setObjectName(u"spinBox_day")
        self.spinBox_day.setFont(font)
        self.spinBox_day.setValue(31.750000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBox_day)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayoutWidget_2 = QWidget(Widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(420, 120, 311, 401))
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.out_0 = QLabel(self.verticalLayoutWidget_2)
        self.out_0.setObjectName(u"out_0")
        self.out_0.setFont(font)

        self.verticalLayout_2.addWidget(self.out_0)

        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.out_1 = QLabel(self.verticalLayoutWidget_2)
        self.out_1.setObjectName(u"out_1")
        self.out_1.setFont(font)

        self.verticalLayout_2.addWidget(self.out_1)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_9)

        self.out_2 = QLabel(self.verticalLayoutWidget_2)
        self.out_2.setObjectName(u"out_2")
        self.out_2.setFont(font)

        self.verticalLayout_2.addWidget(self.out_2)

        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_12)

        self.out_3 = QLabel(self.verticalLayoutWidget_2)
        self.out_3.setObjectName(u"out_3")
        self.out_3.setFont(font)

        self.verticalLayout_2.addWidget(self.out_3)

        self.label_11 = QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.out_4 = QLabel(self.verticalLayoutWidget_2)
        self.out_4.setObjectName(u"out_4")
        self.out_4.setFont(font)

        self.verticalLayout_2.addWidget(self.out_4)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.out_5 = QLabel(self.verticalLayoutWidget_2)
        self.out_5.setObjectName(u"out_5")
        self.out_5.setFont(font)

        self.verticalLayout_2.addWidget(self.out_5)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_13)

        self.out_6 = QLabel(self.verticalLayoutWidget_2)
        self.out_6.setObjectName(u"out_6")
        self.out_6.setFont(font)

        self.verticalLayout_2.addWidget(self.out_6)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u8f93\u5165", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u5165\u804c\u5e94\u627f\u5de5\u8d44", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u5c97\u4f4d\u5de5\u8d44", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u57fa\u672c\u5de5\u8d44", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u5f53\u6708\u4e0a\u73ed\u5929\u6570_\u6362\u7b97\u540e", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u8f93\u51fa", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u5f53\u6708\u5e94\u53d1\u5de5\u8d44", None))
        self.out_0.setText("")
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u8d85\u8fc733.75\u5929\u540e\uff0c\u6bcf\u5929\u80fd\u62ff\u7684\u5de5\u8d44", None))
        self.out_1.setText("")
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u4e0a\u6ee122\u5929\u80fd\u62ff\u5230\u7684\u5de5\u8d44", None))
        self.out_2.setText("")
        self.label_12.setText(QCoreApplication.translate("Widget", u"\u8bf7\u5047\u4e00\u5929\u6263\u7684\u5de5\u8d44", None))
        self.out_3.setText("")
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u8bf7\u5047\u4e00\u665a\u6263\u7684\u5de5\u8d44", None))
        self.out_4.setText("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u6ee133.75\u5929\u80fd\u5f97\u5230\u7684\u5de5\u8d44", None))
        self.out_5.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"\u6ee131.75\u5929\u80fd\u5f97\u5230\u7684\u5de5\u8d44", None))
        self.out_6.setText("")
    # retranslateUi

