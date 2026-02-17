import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFormLayout,
    QHBoxLayout
)
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.correct_login = "admin"
        self.correct_password = "123456"

    def initUI(self):
        self.setWindowTitle("Авторизация")
        self.setGeometry(400, 200, 420, 280)
        self.setFixedSize(420, 280)  

      
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 30, 40, 40)
        main_layout.setSpacing(20)

        title = QLabel("Вход в систему")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        main_layout.addWidget(title)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setSpacing(12)

        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Введите логин")
        self.login_edit.setStyleSheet("font-size: 16px; padding: 8px;")
        form_layout.addRow("Логин:", self.login_edit)

        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Введите пароль")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_edit.setStyleSheet("font-size: 16px; padding: 8px;")
        form_layout.addRow("Пароль:", self.password_edit)

        main_layout.addLayout(form_layout)

        login_button = QPushButton("Войти")
        login_button.setStyleSheet("""
            QPushButton {
                font-size: 18px;
                padding: 12px;
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
        login_button.clicked.connect(self.check_login)
        main_layout.addWidget(login_button)

        main_layout.addStretch()

        self.setLayout(main_layout)

    def check_login(self):
        entered_login = self.login_edit.text().strip()
        entered_password = self.password_edit.text().strip()

        if not entered_login or not entered_password:
            QMessageBox.warning(
                self,
                "Ошибка ввода",
                "Введите логин и пароль!",
                QMessageBox.StandardButton.Ok
            )
            return

        if (entered_login == self.correct_login and 
            entered_password == self.correct_password):
            QMessageBox.information(
                self,
                "Успех",
                "Вход выполнен успешно!",
                QMessageBox.StandardButton.Ok
            )

        else:
            QMessageBox.critical(
                self,
                "Ошибка авторизации",
                "Неверный логин или пароль!",
                QMessageBox.StandardButton.Ok
            )
            self.password_edit.clear()         
            self.password_edit.setFocus()      


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
  
    app.setStyle("Fusion")
    
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
