import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt6.QtCore import Qt

class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Кликер")
        self.setGeometry(400, 200, 400, 280)
        
        
        self.label = QLabel("0", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 72px; 
            font-weight: bold; 
            color: #e74c3c;
            background-color: #ecf0f1;
            border-radius: 15px;
            padding: 20px;
        """)
        
       
        self.button = QPushButton("Клик!", self)
        self.button.setStyleSheet("""
            font-size: 28px; 
            padding: 18px; 
            background-color: #3498db; 
            color: white; 
            border-radius: 12px;
            font-weight: bold;
        """)
        self.button.clicked.connect(self.click)
        
       
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.label)
        layout.addStretch(1)
        layout.addWidget(self.button)
        layout.setContentsMargins(40, 30, 40, 40)
        layout.setSpacing(40)
        
        self.setLayout(layout)

    def click(self):
        self.count += 1
        self.label.setText(str(self.count))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClickerGame()
    window.show()
    sys.exit(app.exec())
