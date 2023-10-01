from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon


class ErrorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setWindowIcon(QIcon(r"Rewards\images\application\RewardsIcon.ico"))
        self.setGeometry(780, 220, 500, 630)
        self.initUI()

    def initUI(self):
        self.errorLayout = QVBoxLayout()
        label = QLabel("Error", self)
        self.errorLayout.addWidget(label)
        self.setLayout(self.errorLayout)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    errorPage = ErrorPage()
    errorPage.show()
    sys.exit(app.exec_())