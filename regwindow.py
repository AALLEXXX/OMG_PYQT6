from PyQt6.QtWidgets import QWidget

from database import Database
from ui_base.ui_reg import Ui_Form


class RegWindow(QWidget):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.reg_but.clicked.connect(self.click_reg_but)
        self.show()


    def click_reg_but(self):
        login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        mail = self.ui.mail_line.text()
        phone = self.ui.phone_line.text()

        answer = self.db.reg_new_user(login, password, mail, phone)

        response = 'успешно' if answer else 'не успешно'
        return self.ui.exeption_label.setText(response)

