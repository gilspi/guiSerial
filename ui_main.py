# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(120, 120, 120)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(400, 90, 111, 51))
        self.layoutWidget.setMaximumSize(QSize(111, 95))
        self.att_in_iq_layout = QVBoxLayout(self.layoutWidget)
        self.att_in_iq_layout.setObjectName(u"att_in_iq_layout")
        self.att_in_iq_layout.setContentsMargins(0, 0, 0, 0)
        self.att_in_iq = QLabel(self.layoutWidget)
        self.att_in_iq.setObjectName(u"att_in_iq")
        self.att_in_iq.setMaximumSize(QSize(109, 16))

        self.att_in_iq_layout.addWidget(self.att_in_iq)

        self.att_in_iq_value = QPlainTextEdit(self.layoutWidget)
        self.att_in_iq_value.setObjectName(u"att_in_iq_value")
        self.att_in_iq_value.setMaximumSize(QSize(109, 71))
        self.att_in_iq_value.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.att_in_iq_value.setStyleSheet(u"background-color: white")

        self.att_in_iq_layout.addWidget(self.att_in_iq_value)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(400, 140, 111, 51))
        self.layoutWidget_2.setMaximumSize(QSize(111, 95))
        self.hmc_freq_0_layout = QVBoxLayout(self.layoutWidget_2)
        self.hmc_freq_0_layout.setObjectName(u"hmc_freq_0_layout")
        self.hmc_freq_0_layout.setContentsMargins(0, 0, 0, 0)
        self.hmc_freq_0 = QLabel(self.layoutWidget_2)
        self.hmc_freq_0.setObjectName(u"hmc_freq_0")
        self.hmc_freq_0.setMaximumSize(QSize(109, 16))

        self.hmc_freq_0_layout.addWidget(self.hmc_freq_0)

        self.hmc_freq_0_value = QPlainTextEdit(self.layoutWidget_2)
        self.hmc_freq_0_value.setObjectName(u"hmc_freq_0_value")
        self.hmc_freq_0_value.setMaximumSize(QSize(109, 71))
        self.hmc_freq_0_value.setStyleSheet(u"background-color: white")

        self.hmc_freq_0_layout.addWidget(self.hmc_freq_0_value)

        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(520, 40, 111, 51))
        self.layoutWidget_3.setMaximumSize(QSize(111, 95))
        self.hmc_freq_1_layout = QVBoxLayout(self.layoutWidget_3)
        self.hmc_freq_1_layout.setObjectName(u"hmc_freq_1_layout")
        self.hmc_freq_1_layout.setContentsMargins(0, 0, 0, 0)
        self.hmc_freq_1 = QLabel(self.layoutWidget_3)
        self.hmc_freq_1.setObjectName(u"hmc_freq_1")
        self.hmc_freq_1.setMaximumSize(QSize(109, 16))

        self.hmc_freq_1_layout.addWidget(self.hmc_freq_1)

        self.hmc_freq_1_value = QPlainTextEdit(self.layoutWidget_3)
        self.hmc_freq_1_value.setObjectName(u"hmc_freq_1_value")
        self.hmc_freq_1_value.setMaximumSize(QSize(109, 71))
        self.hmc_freq_1_value.setStyleSheet(u"background-color: white")

        self.hmc_freq_1_layout.addWidget(self.hmc_freq_1_value)

        self.layoutWidget_4 = QWidget(self.centralwidget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(520, 90, 111, 51))
        self.layoutWidget_4.setMaximumSize(QSize(111, 95))
        self.hmc_freq_2_layout = QVBoxLayout(self.layoutWidget_4)
        self.hmc_freq_2_layout.setObjectName(u"hmc_freq_2_layout")
        self.hmc_freq_2_layout.setContentsMargins(0, 0, 0, 0)
        self.hmc_freq_2 = QLabel(self.layoutWidget_4)
        self.hmc_freq_2.setObjectName(u"hmc_freq_2")
        self.hmc_freq_2.setMaximumSize(QSize(109, 16))

        self.hmc_freq_2_layout.addWidget(self.hmc_freq_2)

        self.hmc_freq_2_value = QPlainTextEdit(self.layoutWidget_4)
        self.hmc_freq_2_value.setObjectName(u"hmc_freq_2_value")
        self.hmc_freq_2_value.setMaximumSize(QSize(109, 71))
        self.hmc_freq_2_value.setStyleSheet(u"background-color: white")

        self.hmc_freq_2_layout.addWidget(self.hmc_freq_2_value)

        self.layoutWidget_5 = QWidget(self.centralwidget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(520, 140, 111, 51))
        self.layoutWidget_5.setMaximumSize(QSize(111, 95))
        self.hmc_freq_3_layout = QVBoxLayout(self.layoutWidget_5)
        self.hmc_freq_3_layout.setObjectName(u"hmc_freq_3_layout")
        self.hmc_freq_3_layout.setContentsMargins(0, 0, 0, 0)
        self.hmc_freq_3 = QLabel(self.layoutWidget_5)
        self.hmc_freq_3.setObjectName(u"hmc_freq_3")
        self.hmc_freq_3.setMaximumSize(QSize(109, 16))

        self.hmc_freq_3_layout.addWidget(self.hmc_freq_3)

        self.hmc_freq_3_value = QPlainTextEdit(self.layoutWidget_5)
        self.hmc_freq_3_value.setObjectName(u"hmc_freq_3_value")
        self.hmc_freq_3_value.setMaximumSize(QSize(109, 71))
        self.hmc_freq_3_value.setStyleSheet(u"background-color: white")

        self.hmc_freq_3_layout.addWidget(self.hmc_freq_3_value)

        self.layoutWidget_6 = QWidget(self.centralwidget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(640, 40, 111, 51))
        self.layoutWidget_6.setMaximumSize(QSize(111, 95))
        self.cmp_th_low_layout = QVBoxLayout(self.layoutWidget_6)
        self.cmp_th_low_layout.setObjectName(u"cmp_th_low_layout")
        self.cmp_th_low_layout.setContentsMargins(0, 0, 0, 0)
        self.cmp_th_low = QLabel(self.layoutWidget_6)
        self.cmp_th_low.setObjectName(u"cmp_th_low")
        self.cmp_th_low.setMaximumSize(QSize(109, 16))

        self.cmp_th_low_layout.addWidget(self.cmp_th_low)

        self.cmp_th_low_value = QPlainTextEdit(self.layoutWidget_6)
        self.cmp_th_low_value.setObjectName(u"cmp_th_low_value")
        self.cmp_th_low_value.setMaximumSize(QSize(109, 71))
        self.cmp_th_low_value.setStyleSheet(u"background-color: white")

        self.cmp_th_low_layout.addWidget(self.cmp_th_low_value)

        self.layoutWidget_7 = QWidget(self.centralwidget)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(640, 90, 111, 51))
        self.layoutWidget_7.setMaximumSize(QSize(111, 95))
        self.cmp_th_high_layout = QVBoxLayout(self.layoutWidget_7)
        self.cmp_th_high_layout.setObjectName(u"cmp_th_high_layout")
        self.cmp_th_high_layout.setContentsMargins(0, 0, 0, 0)
        self.cmp_th_high = QLabel(self.layoutWidget_7)
        self.cmp_th_high.setObjectName(u"cmp_th_high")
        self.cmp_th_high.setMaximumSize(QSize(109, 16))

        self.cmp_th_high_layout.addWidget(self.cmp_th_high)

        self.cmp_th_high_value = QPlainTextEdit(self.layoutWidget_7)
        self.cmp_th_high_value.setObjectName(u"cmp_th_high_value")
        self.cmp_th_high_value.setMaximumSize(QSize(109, 71))
        self.cmp_th_high_value.setStyleSheet(u"background-color: white")

        self.cmp_th_high_layout.addWidget(self.cmp_th_high_value)

        self.input_name = QLabel(self.centralwidget)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setGeometry(QRect(230, 10, 101, 16))
        self.output_name = QLabel(self.centralwidget)
        self.output_name.setObjectName(u"output_name")
        self.output_name.setGeometry(QRect(20, 320, 101, 16))
        self.layoutWidget_10 = QWidget(self.centralwidget)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(390, 350, 111, 51))
        self.layoutWidget_10.setMaximumSize(QSize(111, 95))
        self.att_in_com_2_layout = QVBoxLayout(self.layoutWidget_10)
        self.att_in_com_2_layout.setObjectName(u"att_in_com_2_layout")
        self.att_in_com_2_layout.setContentsMargins(0, 0, 0, 0)
        self.att_in_com_2 = QLabel(self.layoutWidget_10)
        self.att_in_com_2.setObjectName(u"att_in_com_2")
        self.att_in_com_2.setMaximumSize(QSize(109, 16))

        self.att_in_com_2_layout.addWidget(self.att_in_com_2)

        self.att_in_com_2_value = QPlainTextEdit(self.layoutWidget_10)
        self.att_in_com_2_value.setObjectName(u"att_in_com_2_value")
        self.att_in_com_2_value.setMaximumSize(QSize(109, 71))
        self.att_in_com_2_value.setStyleSheet(u"background-color: white")

        self.att_in_com_2_layout.addWidget(self.att_in_com_2_value)

        self.layoutWidget_11 = QWidget(self.centralwidget)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(510, 400, 111, 51))
        self.layoutWidget_11.setMaximumSize(QSize(111, 95))
        self.cmp_th_high_2_layout = QVBoxLayout(self.layoutWidget_11)
        self.cmp_th_high_2_layout.setObjectName(u"cmp_th_high_2_layout")
        self.cmp_th_high_2_layout.setContentsMargins(0, 0, 0, 0)
        self.cmp_th_high_2 = QLabel(self.layoutWidget_11)
        self.cmp_th_high_2.setObjectName(u"cmp_th_high_2")
        self.cmp_th_high_2.setMaximumSize(QSize(109, 16))

        self.cmp_th_high_2_layout.addWidget(self.cmp_th_high_2)

        self.cmp_th_high_2_value = QPlainTextEdit(self.layoutWidget_11)
        self.cmp_th_high_2_value.setObjectName(u"cmp_th_high_2_value")
        self.cmp_th_high_2_value.setMaximumSize(QSize(109, 71))
        self.cmp_th_high_2_value.setStyleSheet(u"background-color: white")

        self.cmp_th_high_2_layout.addWidget(self.cmp_th_high_2_value)

        self.layoutWidget_12 = QWidget(self.centralwidget)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(390, 400, 111, 51))
        self.layoutWidget_12.setMaximumSize(QSize(111, 95))
        self.att_in_iq_2_layout = QVBoxLayout(self.layoutWidget_12)
        self.att_in_iq_2_layout.setObjectName(u"att_in_iq_2_layout")
        self.att_in_iq_2_layout.setContentsMargins(0, 0, 0, 0)
        self.att_in_iq_2 = QLabel(self.layoutWidget_12)
        self.att_in_iq_2.setObjectName(u"att_in_iq_2")
        self.att_in_iq_2.setMaximumSize(QSize(109, 16))

        self.att_in_iq_2_layout.addWidget(self.att_in_iq_2)

        self.att_in_iq_2_value = QPlainTextEdit(self.layoutWidget_12)
        self.att_in_iq_2_value.setObjectName(u"att_in_iq_2_value")
        self.att_in_iq_2_value.setMaximumSize(QSize(109, 71))
        self.att_in_iq_2_value.setStyleSheet(u"background-color: white")

        self.att_in_iq_2_layout.addWidget(self.att_in_iq_2_value)

        self.layoutWidget_14 = QWidget(self.centralwidget)
        self.layoutWidget_14.setObjectName(u"layoutWidget_14")
        self.layoutWidget_14.setGeometry(QRect(510, 450, 111, 51))
        self.layoutWidget_14.setMaximumSize(QSize(111, 95))
        self.vdet_rx_maxpwr_2_layout = QVBoxLayout(self.layoutWidget_14)
        self.vdet_rx_maxpwr_2_layout.setObjectName(u"vdet_rx_maxpwr_2_layout")
        self.vdet_rx_maxpwr_2_layout.setContentsMargins(0, 0, 0, 0)
        self.vdet_rx_maxpwr_3 = QLabel(self.layoutWidget_14)
        self.vdet_rx_maxpwr_3.setObjectName(u"vdet_rx_maxpwr_3")
        self.vdet_rx_maxpwr_3.setMaximumSize(QSize(109, 16))

        self.vdet_rx_maxpwr_2_layout.addWidget(self.vdet_rx_maxpwr_3)

        self.vdet_rx_maxpwr_2_value = QPlainTextEdit(self.layoutWidget_14)
        self.vdet_rx_maxpwr_2_value.setObjectName(u"vdet_rx_maxpwr_2_value")
        self.vdet_rx_maxpwr_2_value.setMaximumSize(QSize(109, 71))
        self.vdet_rx_maxpwr_2_value.setStyleSheet(u"background-color: white")

        self.vdet_rx_maxpwr_2_layout.addWidget(self.vdet_rx_maxpwr_2_value)

        self.layoutWidget_15 = QWidget(self.centralwidget)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(390, 450, 111, 51))
        self.layoutWidget_15.setMaximumSize(QSize(111, 95))
        self.hmc_freq_0_2_layout = QVBoxLayout(self.layoutWidget_15)
        self.hmc_freq_0_2_layout.setObjectName(u"hmc_freq_0_2_layout")
        self.hmc_freq_0_2_layout.setContentsMargins(0, 0, 0, 0)
        self.hmc_freq_0_2 = QLabel(self.layoutWidget_15)
        self.hmc_freq_0_2.setObjectName(u"hmc_freq_0_2")
        self.hmc_freq_0_2.setMaximumSize(QSize(109, 16))

        self.hmc_freq_0_2_layout.addWidget(self.hmc_freq_0_2)

        self.hmc_freq_0_2_value = QPlainTextEdit(self.layoutWidget_15)
        self.hmc_freq_0_2_value.setObjectName(u"hmc_freq_0_2_value")
        self.hmc_freq_0_2_value.setMaximumSize(QSize(109, 71))
        self.hmc_freq_0_2_value.setStyleSheet(u"background-color: white")

        self.hmc_freq_0_2_layout.addWidget(self.hmc_freq_0_2_value)

        self.layoutWidget_17 = QWidget(self.centralwidget)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(510, 350, 111, 51))
        self.layoutWidget_17.setMaximumSize(QSize(111, 95))
        self.cmp_th_low_2_layout = QVBoxLayout(self.layoutWidget_17)
        self.cmp_th_low_2_layout.setObjectName(u"cmp_th_low_2_layout")
        self.cmp_th_low_2_layout.setContentsMargins(0, 0, 0, 0)
        self.cmp_th_low_2 = QLabel(self.layoutWidget_17)
        self.cmp_th_low_2.setObjectName(u"cmp_th_low_2")
        self.cmp_th_low_2.setMaximumSize(QSize(109, 16))

        self.cmp_th_low_2_layout.addWidget(self.cmp_th_low_2)

        self.cmp_th_low_2_value = QPlainTextEdit(self.layoutWidget_17)
        self.cmp_th_low_2_value.setObjectName(u"cmp_th_low_2_value")
        self.cmp_th_low_2_value.setMaximumSize(QSize(109, 71))
        self.cmp_th_low_2_value.setStyleSheet(u"background-color: white")

        self.cmp_th_low_2_layout.addWidget(self.cmp_th_low_2_value)

        self.send_btn = QPushButton(self.centralwidget)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setGeometry(QRect(600, 280, 161, 51))
        self.send_btn.setStyleSheet(u"background-color: white\n"
"")
        self.da28_control = QGroupBox(self.centralwidget)
        self.da28_control.setObjectName(u"da28_control")
        self.da28_control.setGeometry(QRect(20, 80, 91, 111))
        self.verticalLayout_29 = QVBoxLayout(self.da28_control)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.da28_control_value_auto = QRadioButton(self.da28_control)
        self.da28_control_value_auto.setObjectName(u"da28_control_value_auto")
        self.da28_control_value_auto.setEnabled(True)
#if QT_CONFIG(statustip)
        self.da28_control_value_auto.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.da28_control_value_auto.setChecked(True)

        self.verticalLayout_29.addWidget(self.da28_control_value_auto)

        self.da28_control_value_0 = QRadioButton(self.da28_control)
        self.da28_control_value_0.setObjectName(u"da28_control_value_0")

        self.verticalLayout_29.addWidget(self.da28_control_value_0)

        self.da28_control_value_1 = QRadioButton(self.da28_control)
        self.da28_control_value_1.setObjectName(u"da28_control_value_1")

        self.verticalLayout_29.addWidget(self.da28_control_value_1)

        self.da28_control_value_2 = QRadioButton(self.da28_control)
        self.da28_control_value_2.setObjectName(u"da28_control_value_2")

        self.verticalLayout_29.addWidget(self.da28_control_value_2)

        self.da28_control_value_3 = QRadioButton(self.da28_control)
        self.da28_control_value_3.setObjectName(u"da28_control_value_3")

        self.verticalLayout_29.addWidget(self.da28_control_value_3)

        self.da23_control = QGroupBox(self.centralwidget)
        self.da23_control.setObjectName(u"da23_control")
        self.da23_control.setGeometry(QRect(120, 80, 91, 111))
        self.verticalLayout_30 = QVBoxLayout(self.da23_control)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.da23_control_value_auto = QRadioButton(self.da23_control)
        self.da23_control_value_auto.setObjectName(u"da23_control_value_auto")
        self.da23_control_value_auto.setChecked(True)

        self.verticalLayout_30.addWidget(self.da23_control_value_auto)

        self.da23_control_value_0 = QRadioButton(self.da23_control)
        self.da23_control_value_0.setObjectName(u"da23_control_value_0")

        self.verticalLayout_30.addWidget(self.da23_control_value_0)

        self.da23_control_value_1 = QRadioButton(self.da23_control)
        self.da23_control_value_1.setObjectName(u"da23_control_value_1")

        self.verticalLayout_30.addWidget(self.da23_control_value_1)

        self.da23_control_value_2 = QRadioButton(self.da23_control)
        self.da23_control_value_2.setObjectName(u"da23_control_value_2")

        self.verticalLayout_30.addWidget(self.da23_control_value_2)

        self.da23_control_value_3 = QRadioButton(self.da23_control)
        self.da23_control_value_3.setObjectName(u"da23_control_value_3")

        self.verticalLayout_30.addWidget(self.da23_control_value_3)

        self.da4_control = QGroupBox(self.centralwidget)
        self.da4_control.setObjectName(u"da4_control")
        self.da4_control.setGeometry(QRect(20, 190, 81, 81))
        self.verticalLayout_31 = QVBoxLayout(self.da4_control)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.da4_control_value_auto = QRadioButton(self.da4_control)
        self.da4_control_value_auto.setObjectName(u"da4_control_value_auto")
        self.da4_control_value_auto.setChecked(True)

        self.verticalLayout_31.addWidget(self.da4_control_value_auto)

        self.da4_control_value_0 = QRadioButton(self.da4_control)
        self.da4_control_value_0.setObjectName(u"da4_control_value_0")

        self.verticalLayout_31.addWidget(self.da4_control_value_0)

        self.da4_control_value_1 = QRadioButton(self.da4_control)
        self.da4_control_value_1.setObjectName(u"da4_control_value_1")

        self.verticalLayout_31.addWidget(self.da4_control_value_1)

        self.da7_control = QGroupBox(self.centralwidget)
        self.da7_control.setObjectName(u"da7_control")
        self.da7_control.setGeometry(QRect(220, 190, 81, 81))
        self.verticalLayout_32 = QVBoxLayout(self.da7_control)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.da7_control_value_auto = QRadioButton(self.da7_control)
        self.da7_control_value_auto.setObjectName(u"da7_control_value_auto")
        self.da7_control_value_auto.setChecked(True)

        self.verticalLayout_32.addWidget(self.da7_control_value_auto)

        self.da7_control_value_0 = QRadioButton(self.da7_control)
        self.da7_control_value_0.setObjectName(u"da7_control_value_0")

        self.verticalLayout_32.addWidget(self.da7_control_value_0)

        self.da7_control_value_1 = QRadioButton(self.da7_control)
        self.da7_control_value_1.setObjectName(u"da7_control_value_1")

        self.verticalLayout_32.addWidget(self.da7_control_value_1)

        self.da3_control = QGroupBox(self.centralwidget)
        self.da3_control.setObjectName(u"da3_control")
        self.da3_control.setGeometry(QRect(120, 190, 81, 81))
        self.verticalLayout_33 = QVBoxLayout(self.da3_control)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.da3_control_value_auto = QRadioButton(self.da3_control)
        self.da3_control_value_auto.setObjectName(u"da3_control_value_auto")
        self.da3_control_value_auto.setChecked(True)

        self.verticalLayout_33.addWidget(self.da3_control_value_auto)

        self.da3_control_value_0 = QRadioButton(self.da3_control)
        self.da3_control_value_0.setObjectName(u"da3_control_value_0")

        self.verticalLayout_33.addWidget(self.da3_control_value_0)

        self.da3_control_value_1 = QRadioButton(self.da3_control)
        self.da3_control_value_1.setObjectName(u"da3_control_value_1")

        self.verticalLayout_33.addWidget(self.da3_control_value_1)

        self.da2_control = QGroupBox(self.centralwidget)
        self.da2_control.setObjectName(u"da2_control")
        self.da2_control.setGeometry(QRect(300, 110, 81, 81))
        self.verticalLayout_34 = QVBoxLayout(self.da2_control)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.da2_control_value_auto = QRadioButton(self.da2_control)
        self.da2_control_value_auto.setObjectName(u"da2_control_value_auto")
        self.da2_control_value_auto.setChecked(True)

        self.verticalLayout_34.addWidget(self.da2_control_value_auto)

        self.da2_control_value_0 = QRadioButton(self.da2_control)
        self.da2_control_value_0.setObjectName(u"da2_control_value_0")

        self.verticalLayout_34.addWidget(self.da2_control_value_0)

        self.da2_control_value_1 = QRadioButton(self.da2_control)
        self.da2_control_value_1.setObjectName(u"da2_control_value_1")

        self.verticalLayout_34.addWidget(self.da2_control_value_1)

        self.en_iqmd = QGroupBox(self.centralwidget)
        self.en_iqmd.setObjectName(u"en_iqmd")
        self.en_iqmd.setGeometry(QRect(220, 110, 71, 81))
        self.verticalLayout_35 = QVBoxLayout(self.en_iqmd)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.en_iqmd_value_auto = QRadioButton(self.en_iqmd)
        self.en_iqmd_value_auto.setObjectName(u"en_iqmd_value_auto")
        self.en_iqmd_value_auto.setChecked(True)

        self.verticalLayout_35.addWidget(self.en_iqmd_value_auto)

        self.en_iqmd_value_0 = QRadioButton(self.en_iqmd)
        self.en_iqmd_value_0.setObjectName(u"en_iqmd_value_0")

        self.verticalLayout_35.addWidget(self.en_iqmd_value_0)

        self.en_iqmd_value_1 = QRadioButton(self.en_iqmd)
        self.en_iqmd_value_1.setObjectName(u"en_iqmd_value_1")

        self.verticalLayout_35.addWidget(self.en_iqmd_value_1)

        self.en_iqdmd = QGroupBox(self.centralwidget)
        self.en_iqdmd.setObjectName(u"en_iqdmd")
        self.en_iqdmd.setGeometry(QRect(320, 30, 71, 81))
        self.verticalLayout_36 = QVBoxLayout(self.en_iqdmd)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.en_iqdmd_value_auto = QRadioButton(self.en_iqdmd)
        self.en_iqdmd_value_auto.setObjectName(u"en_iqdmd_value_auto")
        self.en_iqdmd_value_auto.setChecked(True)

        self.verticalLayout_36.addWidget(self.en_iqdmd_value_auto)

        self.en_iqdmd_value_0 = QRadioButton(self.en_iqdmd)
        self.en_iqdmd_value_0.setObjectName(u"en_iqdmd_value_0")

        self.verticalLayout_36.addWidget(self.en_iqdmd_value_0)

        self.en_iqdmd_value_1 = QRadioButton(self.en_iqdmd)
        self.en_iqdmd_value_1.setObjectName(u"en_iqdmd_value_1")

        self.verticalLayout_36.addWidget(self.en_iqdmd_value_1)

        self.en_lo_33 = QGroupBox(self.centralwidget)
        self.en_lo_33.setObjectName(u"en_lo_33")
        self.en_lo_33.setGeometry(QRect(240, 30, 71, 81))
        self.verticalLayout_37 = QVBoxLayout(self.en_lo_33)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.en_lo_33_value_auto = QRadioButton(self.en_lo_33)
        self.en_lo_33_value_auto.setObjectName(u"en_lo_33_value_auto")
        self.en_lo_33_value_auto.setChecked(True)

        self.verticalLayout_37.addWidget(self.en_lo_33_value_auto)

        self.en_lo_33_value_0 = QRadioButton(self.en_lo_33)
        self.en_lo_33_value_0.setObjectName(u"en_lo_33_value_0")

        self.verticalLayout_37.addWidget(self.en_lo_33_value_0)

        self.en_lo_33_value_1 = QRadioButton(self.en_lo_33)
        self.en_lo_33_value_1.setObjectName(u"en_lo_33_value_1")

        self.verticalLayout_37.addWidget(self.en_lo_33_value_1)

        self.en_lo_5 = QGroupBox(self.centralwidget)
        self.en_lo_5.setObjectName(u"en_lo_5")
        self.en_lo_5.setGeometry(QRect(310, 190, 71, 81))
        self.verticalLayout_38 = QVBoxLayout(self.en_lo_5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.en_lo_5_value_auto = QRadioButton(self.en_lo_5)
        self.en_lo_5_value_auto.setObjectName(u"en_lo_5_value_auto")
        self.en_lo_5_value_auto.setChecked(True)

        self.verticalLayout_38.addWidget(self.en_lo_5_value_auto)

        self.en_lo_5_value_0 = QRadioButton(self.en_lo_5)
        self.en_lo_5_value_0.setObjectName(u"en_lo_5_value_0")

        self.verticalLayout_38.addWidget(self.en_lo_5_value_0)

        self.en_lo_5_value_1 = QRadioButton(self.en_lo_5)
        self.en_lo_5_value_1.setObjectName(u"en_lo_5_value_1")

        self.verticalLayout_38.addWidget(self.en_lo_5_value_1)

        self.en_iqdmd_pwr = QGroupBox(self.centralwidget)
        self.en_iqdmd_pwr.setObjectName(u"en_iqdmd_pwr")
        self.en_iqdmd_pwr.setGeometry(QRect(390, 190, 101, 81))
        self.verticalLayout_39 = QVBoxLayout(self.en_iqdmd_pwr)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.en_iqdmd_pwr_auto = QRadioButton(self.en_iqdmd_pwr)
        self.en_iqdmd_pwr_auto.setObjectName(u"en_iqdmd_pwr_auto")
        self.en_iqdmd_pwr_auto.setChecked(True)

        self.verticalLayout_39.addWidget(self.en_iqdmd_pwr_auto)

        self.en_iqdmd_pwr_0 = QRadioButton(self.en_iqdmd_pwr)
        self.en_iqdmd_pwr_0.setObjectName(u"en_iqdmd_pwr_0")

        self.verticalLayout_39.addWidget(self.en_iqdmd_pwr_0)

        self.en_iqdmd_pwr_1 = QRadioButton(self.en_iqdmd_pwr)
        self.en_iqdmd_pwr_1.setObjectName(u"en_iqdmd_pwr_1")

        self.verticalLayout_39.addWidget(self.en_iqdmd_pwr_1)

        self.en_lo_amp = QGroupBox(self.centralwidget)
        self.en_lo_amp.setObjectName(u"en_lo_amp")
        self.en_lo_amp.setGeometry(QRect(500, 190, 81, 81))
        self.verticalLayout_40 = QVBoxLayout(self.en_lo_amp)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.en_lo_amp_value_auto = QRadioButton(self.en_lo_amp)
        self.en_lo_amp_value_auto.setObjectName(u"en_lo_amp_value_auto")
        self.en_lo_amp_value_auto.setChecked(True)

        self.verticalLayout_40.addWidget(self.en_lo_amp_value_auto)

        self.en_lo_amp_value_0 = QRadioButton(self.en_lo_amp)
        self.en_lo_amp_value_0.setObjectName(u"en_lo_amp_value_0")

        self.verticalLayout_40.addWidget(self.en_lo_amp_value_0)

        self.en_lo_amp_value_1 = QRadioButton(self.en_lo_amp)
        self.en_lo_amp_value_1.setObjectName(u"en_lo_amp_value_1")

        self.verticalLayout_40.addWidget(self.en_lo_amp_value_1)

        self.en_rx_amp = QGroupBox(self.centralwidget)
        self.en_rx_amp.setObjectName(u"en_rx_amp")
        self.en_rx_amp.setGeometry(QRect(590, 190, 81, 81))
        self.verticalLayout_41 = QVBoxLayout(self.en_rx_amp)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.en_rx_amp_value_auto = QRadioButton(self.en_rx_amp)
        self.en_rx_amp_value_auto.setObjectName(u"en_rx_amp_value_auto")
        self.en_rx_amp_value_auto.setChecked(True)

        self.verticalLayout_41.addWidget(self.en_rx_amp_value_auto)

        self.en_rx_amp_value_0 = QRadioButton(self.en_rx_amp)
        self.en_rx_amp_value_0.setObjectName(u"en_rx_amp_value_0")

        self.verticalLayout_41.addWidget(self.en_rx_amp_value_0)

        self.en_rx_amp_value_1 = QRadioButton(self.en_rx_amp)
        self.en_rx_amp_value_1.setObjectName(u"en_rx_amp_value_1")

        self.verticalLayout_41.addWidget(self.en_rx_amp_value_1)

        self.hmc_enable = QGroupBox(self.centralwidget)
        self.hmc_enable.setObjectName(u"hmc_enable")
        self.hmc_enable.setGeometry(QRect(680, 190, 81, 81))
        self.verticalLayout_42 = QVBoxLayout(self.hmc_enable)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.hmc_enable_value_auto = QRadioButton(self.hmc_enable)
        self.hmc_enable_value_auto.setObjectName(u"hmc_enable_value_auto")
        self.hmc_enable_value_auto.setChecked(True)

        self.verticalLayout_42.addWidget(self.hmc_enable_value_auto)

        self.hmc_enable_value_0 = QRadioButton(self.hmc_enable)
        self.hmc_enable_value_0.setObjectName(u"hmc_enable_value_0")

        self.verticalLayout_42.addWidget(self.hmc_enable_value_0)

        self.hmc_enable_value_1 = QRadioButton(self.hmc_enable)
        self.hmc_enable_value_1.setObjectName(u"hmc_enable_value_1")

        self.verticalLayout_42.addWidget(self.hmc_enable_value_1)

        self.da23_state = QGroupBox(self.centralwidget)
        self.da23_state.setObjectName(u"da23_state")
        self.da23_state.setGeometry(QRect(20, 450, 81, 101))
        self.verticalLayout_43 = QVBoxLayout(self.da23_state)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.da23_state_value_0 = QRadioButton(self.da23_state)
        self.da23_state_value_0.setObjectName(u"da23_state_value_0")

        self.verticalLayout_43.addWidget(self.da23_state_value_0)

        self.da23_state_value_1 = QRadioButton(self.da23_state)
        self.da23_state_value_1.setObjectName(u"da23_state_value_1")

        self.verticalLayout_43.addWidget(self.da23_state_value_1)

        self.da23_state_value_2 = QRadioButton(self.da23_state)
        self.da23_state_value_2.setObjectName(u"da23_state_value_2")

        self.verticalLayout_43.addWidget(self.da23_state_value_2)

        self.da23_state_value_3 = QRadioButton(self.da23_state)
        self.da23_state_value_3.setObjectName(u"da23_state_value_3")

        self.verticalLayout_43.addWidget(self.da23_state_value_3)

        self.da28_state_2 = QGroupBox(self.centralwidget)
        self.da28_state_2.setObjectName(u"da28_state_2")
        self.da28_state_2.setGeometry(QRect(20, 340, 81, 101))
        self.verticalLayout_44 = QVBoxLayout(self.da28_state_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.da28_state_value_0 = QRadioButton(self.da28_state_2)
        self.da28_state_value_0.setObjectName(u"da28_state_value_0")

        self.verticalLayout_44.addWidget(self.da28_state_value_0)

        self.da28_state_value_1 = QRadioButton(self.da28_state_2)
        self.da28_state_value_1.setObjectName(u"da28_state_value_1")

        self.verticalLayout_44.addWidget(self.da28_state_value_1)

        self.da28_state_value_2 = QRadioButton(self.da28_state_2)
        self.da28_state_value_2.setObjectName(u"da28_state_value_2")

        self.verticalLayout_44.addWidget(self.da28_state_value_2)

        self.da28_state_value_3 = QRadioButton(self.da28_state_2)
        self.da28_state_value_3.setObjectName(u"da28_state_value_3")

        self.verticalLayout_44.addWidget(self.da28_state_value_3)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(640, 140, 134, 48))
        self.checkboxes_ver_layout_2 = QVBoxLayout(self.layoutWidget1)
        self.checkboxes_ver_layout_2.setObjectName(u"checkboxes_ver_layout_2")
        self.checkboxes_ver_layout_2.setContentsMargins(0, 0, 0, 0)
        self.ask_if_power_mode = QCheckBox(self.layoutWidget1)
        self.ask_if_power_mode.setObjectName(u"ask_if_power_mode")

        self.checkboxes_ver_layout_2.addWidget(self.ask_if_power_mode)

        self.force_update = QCheckBox(self.layoutWidget1)
        self.force_update.setObjectName(u"force_update")

        self.checkboxes_ver_layout_2.addWidget(self.force_update)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(400, 40, 111, 51))
        self.layoutWidget2.setMaximumSize(QSize(111, 95))
        self.att_in_com_layout = QVBoxLayout(self.layoutWidget2)
        self.att_in_com_layout.setObjectName(u"att_in_com_layout")
        self.att_in_com_layout.setContentsMargins(0, 0, 0, 0)
        self.att_in_com = QLabel(self.layoutWidget2)
        self.att_in_com.setObjectName(u"att_in_com")
        self.att_in_com.setMaximumSize(QSize(109, 16))

        self.att_in_com_layout.addWidget(self.att_in_com)

        self.att_in_com_value = QPlainTextEdit(self.layoutWidget2)
        self.att_in_com_value.setObjectName(u"att_in_com_value")
        self.att_in_com_value.setMaximumSize(QSize(109, 71))
        self.att_in_com_value.setStyleSheet(u"background-color: white")

        self.att_in_com_layout.addWidget(self.att_in_com_value)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(630, 350, 121, 51))
        self.vdet_out_maxpwr_2_layout_2 = QVBoxLayout(self.layoutWidget3)
        self.vdet_out_maxpwr_2_layout_2.setObjectName(u"vdet_out_maxpwr_2_layout_2")
        self.vdet_out_maxpwr_2_layout_2.setContentsMargins(0, 0, 0, 0)
        self.vdet_rx_maxpwr_2 = QLabel(self.layoutWidget3)
        self.vdet_rx_maxpwr_2.setObjectName(u"vdet_rx_maxpwr_2")

        self.vdet_out_maxpwr_2_layout_2.addWidget(self.vdet_rx_maxpwr_2)

        self.vdet_out_maxpwr_2_value = QPlainTextEdit(self.layoutWidget3)
        self.vdet_out_maxpwr_2_value.setObjectName(u"vdet_out_maxpwr_2_value")
        self.vdet_out_maxpwr_2_value.setStyleSheet(u"background-color: white")

        self.vdet_out_maxpwr_2_layout_2.addWidget(self.vdet_out_maxpwr_2_value)

        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(140, 350, 211, 206))
        self.checkboxes_hor_layout = QHBoxLayout(self.layoutWidget4)
        self.checkboxes_hor_layout.setObjectName(u"checkboxes_hor_layout")
        self.checkboxes_hor_layout.setContentsMargins(0, 0, 0, 0)
        self.checkboxes_ver_layout = QVBoxLayout()
        self.checkboxes_ver_layout.setObjectName(u"checkboxes_ver_layout")
        self.da7_state = QCheckBox(self.layoutWidget4)
        self.da7_state.setObjectName(u"da7_state")
        self.da7_state.setChecked(False)

        self.checkboxes_ver_layout.addWidget(self.da7_state)

        self.da4_state = QCheckBox(self.layoutWidget4)
        self.da4_state.setObjectName(u"da4_state")

        self.checkboxes_ver_layout.addWidget(self.da4_state)

        self.da2_state = QCheckBox(self.layoutWidget4)
        self.da2_state.setObjectName(u"da2_state")

        self.checkboxes_ver_layout.addWidget(self.da2_state)

        self.en_lo_34 = QCheckBox(self.layoutWidget4)
        self.en_lo_34.setObjectName(u"en_lo_34")

        self.checkboxes_ver_layout.addWidget(self.en_lo_34)

        self.en_lo_amp_2 = QCheckBox(self.layoutWidget4)
        self.en_lo_amp_2.setObjectName(u"en_lo_amp_2")

        self.checkboxes_ver_layout.addWidget(self.en_lo_amp_2)

        self.hmc_enable_2 = QCheckBox(self.layoutWidget4)
        self.hmc_enable_2.setObjectName(u"hmc_enable_2")

        self.checkboxes_ver_layout.addWidget(self.hmc_enable_2)

        self.cmp_high = QCheckBox(self.layoutWidget4)
        self.cmp_high.setObjectName(u"cmp_high")

        self.checkboxes_ver_layout.addWidget(self.cmp_high)

        self.hmc_ld = QCheckBox(self.layoutWidget4)
        self.hmc_ld.setObjectName(u"hmc_ld")

        self.checkboxes_ver_layout.addWidget(self.hmc_ld)


        self.checkboxes_hor_layout.addLayout(self.checkboxes_ver_layout)

        self.checkboxes_ver_layout_3 = QVBoxLayout()
        self.checkboxes_ver_layout_3.setObjectName(u"checkboxes_ver_layout_3")
        self.en_iqdmd_2 = QCheckBox(self.layoutWidget4)
        self.en_iqdmd_2.setObjectName(u"en_iqdmd_2")

        self.checkboxes_ver_layout_3.addWidget(self.en_iqdmd_2)

        self.en_iqmd_2 = QCheckBox(self.layoutWidget4)
        self.en_iqmd_2.setObjectName(u"en_iqmd_2")

        self.checkboxes_ver_layout_3.addWidget(self.en_iqmd_2)

        self.da3_state = QCheckBox(self.layoutWidget4)
        self.da3_state.setObjectName(u"da3_state")

        self.checkboxes_ver_layout_3.addWidget(self.da3_state)

        self.en_lo_6 = QCheckBox(self.layoutWidget4)
        self.en_lo_6.setObjectName(u"en_lo_6")

        self.checkboxes_ver_layout_3.addWidget(self.en_lo_6)

        self.en_iqdmd_pwr_2 = QCheckBox(self.layoutWidget4)
        self.en_iqdmd_pwr_2.setObjectName(u"en_iqdmd_pwr_2")

        self.checkboxes_ver_layout_3.addWidget(self.en_iqdmd_pwr_2)

        self.en_rx_amp_2 = QCheckBox(self.layoutWidget4)
        self.en_rx_amp_2.setObjectName(u"en_rx_amp_2")

        self.checkboxes_ver_layout_3.addWidget(self.en_rx_amp_2)

        self.cmp_low = QCheckBox(self.layoutWidget4)
        self.cmp_low.setObjectName(u"cmp_low")

        self.checkboxes_ver_layout_3.addWidget(self.cmp_low)


        self.checkboxes_hor_layout.addLayout(self.checkboxes_ver_layout_3)

        self.select_ports = QGroupBox(self.centralwidget)
        self.select_ports.setObjectName(u"select_ports")
        self.select_ports.setGeometry(QRect(20, 10, 201, 61))
        self.formLayout = QFormLayout(self.select_ports)
        self.formLayout.setObjectName(u"formLayout")
        self.list_ports = QComboBox(self.select_ports)
        self.list_ports.addItem("")
        self.list_ports.setObjectName(u"list_ports")
        self.list_ports.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.list_ports.setEditable(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.list_ports)

        self.btn_connect = QPushButton(self.select_ports)
        self.btn_connect.setObjectName(u"btn_connect")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btn_connect)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.att_in_iq.setText(QCoreApplication.translate("MainWindow", u"ATT_IN_IQ", None))
        self.att_in_iq_value.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.hmc_freq_0.setText(QCoreApplication.translate("MainWindow", u"HMC Freq 0", None))
        self.hmc_freq_0_value.setPlainText(QCoreApplication.translate("MainWindow", u"500", None))
        self.hmc_freq_1.setText(QCoreApplication.translate("MainWindow", u"HMC Freq 1", None))
        self.hmc_freq_1_value.setPlainText(QCoreApplication.translate("MainWindow", u"500", None))
        self.hmc_freq_2.setText(QCoreApplication.translate("MainWindow", u"HMC Freq 2", None))
        self.hmc_freq_2_value.setPlainText(QCoreApplication.translate("MainWindow", u"500", None))
        self.hmc_freq_3.setText(QCoreApplication.translate("MainWindow", u"HMC Freq 3", None))
        self.hmc_freq_3_value.setPlainText(QCoreApplication.translate("MainWindow", u"500", None))
        self.cmp_th_low.setText(QCoreApplication.translate("MainWindow", u"CMP_TH_LOW", None))
        self.cmp_th_low_value.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cmp_th_high.setText(QCoreApplication.translate("MainWindow", u"CMP_TH_HIGH", None))
        self.cmp_th_high_value.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.input_name.setText(QCoreApplication.translate("MainWindow", u"ASK RF -> ASK IF", None))
        self.output_name.setText(QCoreApplication.translate("MainWindow", u"ASK IF -> ASK RF", None))
        self.att_in_com_2.setText(QCoreApplication.translate("MainWindow", u"ATT_IN_COM", None))
        self.cmp_th_high_2.setText(QCoreApplication.translate("MainWindow", u"CMP_TH_HIGH", None))
        self.att_in_iq_2.setText(QCoreApplication.translate("MainWindow", u"ATT_IN_IQ", None))
        self.vdet_rx_maxpwr_3.setText(QCoreApplication.translate("MainWindow", u"VDET_RX_MAXPWR", None))
        self.hmc_freq_0_2.setText(QCoreApplication.translate("MainWindow", u"HMC Freq 0", None))
        self.cmp_th_low_2.setText(QCoreApplication.translate("MainWindow", u"CMP_TH_LOW", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.da28_control.setTitle(QCoreApplication.translate("MainWindow", u"DA28 Control", None))
#if QT_CONFIG(tooltip)
        self.da28_control_value_auto.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.da28_control_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.da28_control_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da28_control_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da28_control_value_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.da28_control_value_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.da23_control.setTitle(QCoreApplication.translate("MainWindow", u"DA23 Control", None))
        self.da23_control_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.da23_control_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da23_control_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da23_control_value_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.da23_control_value_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.da4_control.setTitle(QCoreApplication.translate("MainWindow", u"DA4 Control", None))
        self.da4_control_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.da4_control_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da4_control_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da7_control.setTitle(QCoreApplication.translate("MainWindow", u"DA7 Control", None))
        self.da7_control_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.da7_control_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da7_control_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da3_control.setTitle(QCoreApplication.translate("MainWindow", u"DA3 Control", None))
        self.da3_control_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.da3_control_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da3_control_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da2_control.setTitle(QCoreApplication.translate("MainWindow", u"DA2 Control", None))
        self.da2_control_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.da2_control_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da2_control_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_iqmd.setTitle(QCoreApplication.translate("MainWindow", u"En_IQmd", None))
        self.en_iqmd_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_iqmd_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_iqmd_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_iqdmd.setTitle(QCoreApplication.translate("MainWindow", u"En_IQdmd", None))
        self.en_iqdmd_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_iqdmd_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_iqdmd_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_lo_33.setTitle(QCoreApplication.translate("MainWindow", u"En_LO_33", None))
        self.en_lo_33_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_lo_33_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_lo_33_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_lo_5.setTitle(QCoreApplication.translate("MainWindow", u"En_LO_5", None))
        self.en_lo_5_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_lo_5_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_lo_5_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_iqdmd_pwr.setTitle(QCoreApplication.translate("MainWindow", u"En_IQdmd_PWR", None))
        self.en_iqdmd_pwr_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_iqdmd_pwr_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_iqdmd_pwr_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_lo_amp.setTitle(QCoreApplication.translate("MainWindow", u"En_LO_amp", None))
        self.en_lo_amp_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_lo_amp_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_lo_amp_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.en_rx_amp.setTitle(QCoreApplication.translate("MainWindow", u"En_RX_amp", None))
        self.en_rx_amp_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.en_rx_amp_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.en_rx_amp_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.hmc_enable.setTitle(QCoreApplication.translate("MainWindow", u"HMC_Enable", None))
        self.hmc_enable_value_auto.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.hmc_enable_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.hmc_enable_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da23_state.setTitle(QCoreApplication.translate("MainWindow", u"DA23 State", None))
        self.da23_state_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da23_state_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da23_state_value_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.da23_state_value_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.da28_state_2.setTitle(QCoreApplication.translate("MainWindow", u"DA28 State", None))
        self.da28_state_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.da28_state_value_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.da28_state_value_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.da28_state_value_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.ask_if_power_mode.setText(QCoreApplication.translate("MainWindow", u"ASK_IF_Power_Mode", None))
        self.force_update.setText(QCoreApplication.translate("MainWindow", u"FORCE_UPDATE", None))
        self.att_in_com.setText(QCoreApplication.translate("MainWindow", u"ATT_IN_COM", None))
        self.att_in_com_value.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.vdet_rx_maxpwr_2.setText(QCoreApplication.translate("MainWindow", u"VDET_OUT_MAXPWR", None))
        self.da7_state.setText(QCoreApplication.translate("MainWindow", u"DA7 State", None))
        self.da4_state.setText(QCoreApplication.translate("MainWindow", u"DA4 State", None))
        self.da2_state.setText(QCoreApplication.translate("MainWindow", u"DA2 State", None))
        self.en_lo_34.setText(QCoreApplication.translate("MainWindow", u"En_LO_33", None))
        self.en_lo_amp_2.setText(QCoreApplication.translate("MainWindow", u"En_LO_amp", None))
        self.hmc_enable_2.setText(QCoreApplication.translate("MainWindow", u"HMC_Enable", None))
        self.cmp_high.setText(QCoreApplication.translate("MainWindow", u"CMP_HIGH", None))
        self.hmc_ld.setText(QCoreApplication.translate("MainWindow", u"HMC_LD", None))
        self.en_iqdmd_2.setText(QCoreApplication.translate("MainWindow", u"En_IQdmd", None))
        self.en_iqmd_2.setText(QCoreApplication.translate("MainWindow", u"En_IQmd", None))
        self.da3_state.setText(QCoreApplication.translate("MainWindow", u"DA3 State", None))
        self.en_lo_6.setText(QCoreApplication.translate("MainWindow", u"En_LO_5", None))
        self.en_iqdmd_pwr_2.setText(QCoreApplication.translate("MainWindow", u"En_IQdmd_PWR", None))
        self.en_rx_amp_2.setText(QCoreApplication.translate("MainWindow", u"En_RX_amp", None))
        self.cmp_low.setText(QCoreApplication.translate("MainWindow", u"CMP_LOW", None))
        self.select_ports.setTitle(QCoreApplication.translate("MainWindow", u"Select port", None))
        self.list_ports.setItemText(0, QCoreApplication.translate("MainWindow", u"No selected", None))

        self.list_ports.setCurrentText(QCoreApplication.translate("MainWindow", u"No selected", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
    # retranslateUi

