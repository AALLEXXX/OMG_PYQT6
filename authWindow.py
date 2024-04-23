
from PyQt6.QtWidgets import QWidget

from database import Database
from mainwindow import MainWindow
from regwindow import RegWindow
from ui_base.ui_auth import Ui_Form
from PyQt6.QtWidgets import QMessageBox


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Авторизация')
        self.db = Database()
        self.show()
        self.ui.pushButton.clicked.connect(self.click_auth_but)
        self.ui.open_reg_but.clicked.connect(self.click_open_reg_but)


    def click_auth_but(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        auth_list = self.db.auth_user(login, password)
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Заголовок сообщения")
        msg_box.setText(auth_list[0])
        msg_box.exec()
        if auth_list[1]:
            self.main_window = MainWindow(self.db)
            self.close()


    def click_open_reg_but(self):
       self.reg_win = RegWindow(self.db)