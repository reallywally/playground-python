import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6 App')
window.setGeometry(100, 100, 280, 80)

helloMsg = QLabel('<h1>Hello, PyQt5!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec())
