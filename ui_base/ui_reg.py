# Form implementation generated from reading ui file 'ui_base/ui_reg.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form.resize(700, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 530))
        Form.setMaximumSize(QtCore.QSize(700, 530))
        Form.setStyleSheet("background-color:rgb(255, 237, 164)")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(250, 80, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.password_line = QtWidgets.QLineEdit(parent=Form)
        self.password_line.setGeometry(QtCore.QRect(230, 240, 241, 31))
        self.password_line.setObjectName("password_line")
        self.login_line = QtWidgets.QLineEdit(parent=Form)
        self.login_line.setGeometry(QtCore.QRect(230, 180, 241, 31))
        self.login_line.setText("")
        self.login_line.setMaxLength(32764)
        self.login_line.setObjectName("login_line")
        self.reg_but = QtWidgets.QPushButton(parent=Form)
        self.reg_but.setGeometry(QtCore.QRect(290, 460, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.reg_but.setFont(font)
        self.reg_but.setObjectName("reg_but")
        self.exeption_label = QtWidgets.QLabel(parent=Form)
        self.exeption_label.setGeometry(QtCore.QRect(250, 410, 201, 31))
        self.exeption_label.setText("")
        self.exeption_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.exeption_label.setObjectName("exeption_label")
        self.mail_line = QtWidgets.QLineEdit(parent=Form)
        self.mail_line.setGeometry(QtCore.QRect(230, 300, 241, 31))
        self.mail_line.setObjectName("mail_line")
        self.phone_line = QtWidgets.QLineEdit(parent=Form)
        self.phone_line.setGeometry(QtCore.QRect(230, 360, 241, 31))
        self.phone_line.setReadOnly(False)
        self.phone_line.setObjectName("phone_line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.password_line.setPlaceholderText(_translate("Form", "password"))
        self.login_line.setPlaceholderText(_translate("Form", "login"))
        self.reg_but.setText(_translate("Form", "Далее"))
        self.mail_line.setPlaceholderText(_translate("Form", "mail"))
        self.phone_line.setPlaceholderText(_translate("Form", "phone number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
