import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from ui_main import Ui_MainWindow

from data.transport_serial import test_ports


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__add_ports()

    def __add_ports(self):
        self.ui.comboBox.addItems([tport for tport in test_ports[:3]])
        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)

    def on_combo_box_changed(self, index):
        selected_text = self.ui.comboBox.currentText()
        print("Выбран элемент:", selected_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
