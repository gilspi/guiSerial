import sys
import json

import serial
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGroupBox,
    QPlainTextEdit, QRadioButton, QCheckBox,
    QWidget
)
from ui_main import Ui_MainWindow

from data.transport_serial import available_ports, serial_init, packet_sender


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.selected_port = None
        self.ser = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__add_ports()
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.send_data)

    def __add_ports(self):
        self.ui.comboBox.addItems([tport for tport in available_ports[:3]])
        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.ui.pushButton_2.clicked.connect(self.connect_to_port)

    def on_combo_box_changed(self, index):
        self.selected_port = available_ports[index-1]
        print("Selected:", self.selected_port)

    def connect_to_port(self):
        if self.selected_port:
            print("Connection to port:", self.selected_port)
            self.ui.pushButton.setEnabled(True)
            self.ser = serial.Serial(self.selected_port, baudrate=115200, bytesize=8, timeout=0.1)
            serial_init(self.ser)
        else:
            print("No selected.")

    def closeEvent(self, event):
        try:
            if self.ser.isOpen():
                self.ser.close()
                print("Port closed.")
        except AttributeError:
            print("Non port selected. App closed.")
        finally:
            event.accept()

    def __get_data(self, exclude_list: list):
        data = {}

        all_widgets = self.findChildren(QWidget)
        for widget in all_widgets:
            if widget.objectName() not in exclude_list:  # and startswith('input_')
                widget_name = widget.objectName()
                if isinstance(widget, QPlainTextEdit):
                    value = widget.toPlainText()
                    print(f"Widget Name: {widget_name}, Value: {value}")
                    data[widget_name] = value
                elif isinstance(widget, QCheckBox):
                    value = widget.isChecked()
                    print(f"Widget Name: {widget_name}, Value: {value}")
                    data[widget_name] = value
                elif isinstance(widget, QRadioButton):
                    if widget.isChecked():
                        value = widget.text()
                        print(f"Widget Name: {widget_name}, Value: {value}")
                        data[widget_name] = value

        return data

    def send_data(self):
        if self.ui.pushButton.isEnabled():
            exclude_list = ["qt_scrollarea_viewport", "qt_scrollarea_hcontainer", "qt_scrollarea_vcontainer", ""]
            data = self.__get_data(exclude_list)
            packet_sender(data)
            print("Data send:\n", json.dumps(data, indent=4))
        else:
            print("Port not selected. Cannot send data.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    sys.exit(app.exec())
