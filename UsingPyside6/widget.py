# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import nanguang_calculator as c

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.spinBox_all.valueChanged.connect(self.calculate)
        self.ui.spinBox_position.valueChanged.connect(self.calculate)
        self.ui.spinBox_day.valueChanged.connect(self.calculate)


    def calculate(self):
        self.ui.spinBox_position.setMaximum(self.ui.spinBox_all.value() - self.ui.spinBox_base.value())

        [v0, v1, v2, v3, v4, v5, v6] = c.calc(self.ui.spinBox_all.value(), self.ui.spinBox_position.value(), self.ui.spinBox_day.value())

        self.ui.out_0.setText(str(v0))
        self.ui.out_1.setText(str(v1))
        self.ui.out_2.setText(str(v2))
        self.ui.out_3.setText(str(v3))
        self.ui.out_4.setText(str(v4))
        self.ui.out_5.setText(str(v5))
        self.ui.out_6.setText(str(v6))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
