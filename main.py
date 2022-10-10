import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setCentralWidget(QLabel("Hello, world!"))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
