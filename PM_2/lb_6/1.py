import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt6.QtCore import Qt

class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генератор случайных чисел")
        self.setGeometry(300, 200, 380, 220)
        
    
        self.label = QLabel("Нажми кнопку!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 36px; font-weight: bold; color: #2c3e50;")
        
        self.button = QPushButton("Сгенерировать число", self)
        self.button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.button.clicked.connect(self.generate_number)
        
        
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.label)
        layout.addStretch(1)
        layout.addWidget(self.button)
        layout.setContentsMargins(30, 20, 30, 30)
        layout.setSpacing(30)
        
        self.setLayout(layout)

    def generate_number(self):
        number = random.randint(1, 1000) 
        self.label.setText(str(number))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomNumberGenerator()
    window.show()
    sys.exit(app.exec())
