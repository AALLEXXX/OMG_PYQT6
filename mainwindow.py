from PyQt6.QtWidgets import QMainWindow, QMessageBox

from database import Database
from ui_base.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle('ALEX')
        self.db = db
        self.positions = {}
        self.__load_combobox()
        first_key = next(iter(self.positions))
        salary = self.positions[first_key]
        self.ui.salary_lable.setText(salary)
        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)


    def __load_combobox(self):
        data = self.db.get_position()
        for pos in data:
            title = pos[1]
            salary = pos[2]
            self.positions[title] = str(salary)
            self.ui.comboBox.addItem(title)

    def on_combo_box_changed(self, index):
        selected_text = self.ui.comboBox.currentText()
        salary = self.positions[selected_text]
        self.ui.salary_lable.setText(salary)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение выхода', 'Вы уверены, что хотите закрыть приложение?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()