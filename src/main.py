import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from ui_main import Ui_MainWindow

import serial
from data.transport_serial import available_ports, serial_init


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.selected_port = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__add_ports()
        self.ui.pushButton.clicked.connect(self.get_data)

    def __add_ports(self):
        self.ui.comboBox.addItems([tport for tport in available_ports[:3]])
        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)

    def on_combo_box_changed(self, index):
        self.selected_port = available_ports[index]
        print(self.selected_port)
        selected_text = self.ui.comboBox.currentText()
        print("Выбран элемент:", selected_text)

    def get_data(self):
        # Получение текста из LineEdit
        text_from_lineedit = self.ui.lineEdit.text()
        print(f'Text from LineEdit: {text_from_lineedit}')

        # Получение выбранного текста из RadioButton
        for button in self.ui.groupRadioButtons.buttons():
            if button.isChecked():
                print(f'Selected RadioButton: {button.text()}')

        # Получение состояния CheckBox
        checkbox_state = self.ui.checkBox.isChecked()
        print(f'CheckBox state: {checkbox_state}')

        # Получение текста из ComboBox
        selected_text = self.ui.comboBox.currentText()
        print(f'Selected text in ComboBox: {selected_text}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    ser = serial.Serial(window.selected_port, baudrate=115200, bytesize=8, timeout=0.1)
    serial_init(ser)

    window.show()
    sys.exit(app.exec())
